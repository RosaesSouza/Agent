# Criar diretório do projeto
mkdir meu_agente
cd meu_agente

# Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Instalar dependências com pip
pip install langchain>=1.0.0 langchain-openai>=0.3.0 langgraph>=1.0.0 python-dotenv