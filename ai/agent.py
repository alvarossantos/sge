import json
from django.conf import settings
from django.core import serializers
import google.generativeai as genai
from ai import prompts
from products.models import Product
from outflows.models import Outflow


class SGEAgent:

    def __init__(self):
        # Configura a API do Gemini
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.__model = genai.GenerativeModel(settings.GEMINI_MODEL)

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()
        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows),
        })

    def invoke(self):
        user_content = prompts.USER_PROMPT.replace('{{data}}', self.__get_data())

        # Envia o prompt para o modelo
        response = self.__model.generate_content(
            [prompts.SYSTEM_PROMPT, user_content]
        )

        try:
            result = response.text
            from ai.models import AIResult
            AIResult.objects.create(result=result)
            return result
        except ValueError:
            result = f"ERRO: Resposta bloqueada. Causa: {response.prompt_feedback.block_reason}."
            from ai.models import AIResult
            AIResult.objects.create(result=result)
            return result
