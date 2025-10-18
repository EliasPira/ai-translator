# 🧠 AI Translator com Azure OpenAI

Este projeto realiza a extração e tradução de artigos da web utilizando Azure OpenAI e LangChain. O conteúdo é formatado em Markdown e salvo localmente.

## 🚀 Funcionalidades

- Extração de texto limpo de qualquer URL
- Tradução automática para o idioma desejado
- Formatação em Markdown estruturado
- Salvamento em arquivos `.md` com timestamp

## 🛠️ Tecnologias

- Python
- LangChain + Azure OpenAI
- BeautifulSoup
- dotenv

## 📦 Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` com suas credenciais:

   ```env
   AZURE_OPENAI_API_KEY=...
   AZURE_OPENAI_ENDPOINT=...
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
   ```

5. Execute o script:

   ```bash
   python main3.py
   ```

## 📁 Resultados

Os arquivos traduzidos são salvos na pasta `resultados/` com nomes únicos baseados na data e hora.

## 📄 Licença

Este projeto está sob a licença MIT.

