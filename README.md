SGE - Sistema de Gestão Empresarial com IA
Um sistema robusto para gestão de estoque, produtos, fornecedores e finanças, potencializado por um agente de Inteligência Artificial para gerar insights e análises de negócio.

O SGE é projetado para ser uma solução completa para pequenas e médias empresas, oferecendo:

📊 Dashboard Inteligente: A página inicial apresenta métricas de vendas, status de produtos e um insight gerado por IA sobre a saúde do negócio.

📦 Gestão de Produtos: CRUD completo para produtos, incluindo controle de estoque, preço de custo e preço de venda.

🏢 Gestão de Marcas e Fornecedores: Cadastre e gerencie as marcas dos seus produtos e seus respectivos fornecedores.

📈 Controle de Fluxo de Caixa: Registre todas as entradas (compras) e saídas (vendas) de produtos, atualizando o estoque automaticamente.

🤖 Agente de IA (Gemini): Um assistente inteligente que analisa os dados de vendas e estoque para fornecer relatórios, identificar tendências e sugerir ações estratégicas.

🔐 Autenticação e API: Sistema de autenticação seguro via API (JWT) e uma interface web tradicional com login.

🧩 Arquitetura Modular: O projeto é dividido em apps Django independentes, facilitando a manutenção e a escalabilidade.

🛠️ Tecnologias Utilizadas
Este projeto foi construído com uma stack de tecnologias modernas e robustas:

Backend: Django, Django REST Framework

Banco de Dados: PostgreSQL

Inteligência Artificial: Google Gemini

Gestão de Configurações: Python Decouple

Frontend: Django Templates, HTML (com componentes modulares)

Qualidade de Código: Flake8

🚀 Como Usar o Projeto
Siga os passos abaixo para configurar e executar o SGE em seu ambiente local.

Pré-requisitos
Python 3.10+

Pip e Venv

Git

Um servidor PostgreSQL ativo

1. Clonar o Repositório
git clone https://github.com/alvarossantos/sge.git

2. Configurar o Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente
# No Linux ou macOS:
source venv/bin/activate
# No Windows:
.\venv\Scripts\activate

3. Instalar as Dependências
Instale todos os pacotes necessários listados nos arquivos de requisitos.

pip install -r requirements.txt
pip install -r requirements_dev.txt

4. Configurar as Variáveis de Ambiente
O projeto utiliza um arquivo .env para gerenciar chaves de API e configurações do banco de dados.

a. Crie um arquivo chamado .env na raiz do projeto (na mesma pasta que o manage.py).

b. Copie e cole o conteúdo abaixo no seu arquivo .env, substituindo os valores pelos seus.

# Chave secreta do Django (gere uma nova, não use esta)
SECRET_KEY=django-insecure-sua-chave-aqui-troque-por-uma-nova

# Configuração do modo Debug (True para desenvolvimento, False para produção)
DEBUG=True

# Hosts permitidos (em produção, coloque seu domínio)
ALLOWED_HOSTS=127.0.0.1,localhost

# Configurações do Banco de Dados PostgreSQL
DB_NAME=sge_db
DB_USER=seu_usuario_postgres
DB_PASSWORD=sua_senha_postgres
DB_HOST=localhost
DB_PORT=5432

# Chave de API do Google Gemini
GEMINI_API_KEY=sua_chave_de_api_do_gemini_aqui
GEMINI_MODEL=gemini-pro

Importante: Para gerar uma nova SECRET_KEY, você pode usar um gerador online ou executar um comando do Django.

5. Configurar o Banco de Dados
Com o servidor PostgreSQL rodando e as variáveis de ambiente configuradas:

# Aplica as migrações para criar as tabelas no banco de dados
python manage.py migrate

6. Criar um Superusuário
Você precisará de um usuário administrador para acessar o painel de controle do Django.

python manage.py createsuperuser

Siga as instruções para criar seu usuário.

7. Executar o Servidor
Tudo pronto! Inicie o servidor de desenvolvimento.

python manage.py runserver

Acesse [link suspeito removido] em seu navegador para ver a aplicação funcionando.

🤖 Usando o Agente de IA
O SGE possui um comando de gerenciamento para invocar o agente de IA e gerar um novo insight com base nos dados atuais do banco.

Para executá-lo, use o seguinte comando no terminal (com o ambiente virtual ativado):

python manage.py sge_agent_invoke

Este comando irá:

Coletar os dados de produtos, vendas e estoque.

Enviar os dados para a API do Gemini com um prompt específico.

Salvar o resultado gerado pela IA no banco de dados.

O novo insight aparecerá automaticamente no dashboard da página inicial.

🏛️ Estrutura do Projeto
O código é organizado em apps Django, cada um com sua responsabilidade:

/app: Configurações centrais, URLs principais e templates base.

/authentication: Gerencia a autenticação via API (JWT).

/products, /categories, /brands, /suppliers: Apps de CRUD para as entidades principais.

/inflows, /outflows: Gerenciam a lógica de entrada e saída de estoque.

/ai: Contém toda a lógica do agente Gemini, incluindo prompts e comandos.
