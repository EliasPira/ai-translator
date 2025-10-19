# 🧠 AI Translator com Azure OpenAI

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![LangChain](https://img.shields.io/badge/LangChain-Azure_OpenAI-blueviolet)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Este projeto realiza a extração e tradução de artigos da web utilizando Azure OpenAI e LangChain. O conteúdo é formatado em Markdown estruturado e salvo localmente para fácil reutilização.

## 🚀 Funcionalidades

- 🔍 Extração de texto limpo a partir de qualquer URL
- 🌐 Tradução automática para o idioma desejado
- 📝 Formatação do conteúdo em Markdown com títulos e parágrafos
- 💾 Salvamento em arquivos `.md` com timestamp exclusivo

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [LangChain](https://www.langchain.com/) com [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 📦 Como usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie um arquivo `.env` com suas credenciais da Azure OpenAI:**

   ```env
   AZURE_OPENAI_API_KEY=your-api-key
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
   ```

5. **Execute o script principal:**

   ```bash
   python main3.py
   ```

## 📁 Resultados

Os arquivos traduzidos são salvos automaticamente na pasta `resultados/`, com nomes únicos baseados na data e hora da execução.

## 📄 Licença

Distribuído sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e compartilhar.

## 👨‍💻 Expert

---

<table>
  <tr>
    <td align="center" width="100">
      <a href="https://github.com/EliasPira">
        <img src="https://avatars.githubusercontent.com/u/189679772?s=100" width="80" alt="Elias Acosta"/>
      </a>
    </td>
    <td>
      <strong>Elias Acosta</strong>  
      <br/>
      <a href="https://github.com/EliasPira">GitHub</a> • 
      <a href="https://www.linkedin.com/in/elias-acosta-a0ba8619a">LinkedIn</a>
    </td>
  </tr>
</table>

