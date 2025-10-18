import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Carrega variáveis do .env
load_dotenv()

# Função para extrair texto limpo de uma URL
def extract_text_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove scripts e estilos
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        texto = soup.get_text(separator=' ')

        # Limpa espaços extras
        linhas = (line.strip() for line in texto.splitlines())
        partes = (frase.strip() for line in linhas for frase in line.split(" "))
        texto_limpo = '\n'.join(parte for parte in partes if parte)
        return texto_limpo
    else:
        raise Exception(f"Erro ao acessar a URL. Código: {response.status_code}")

# Instancia o cliente Azure OpenAI

# Instancia o cliente Azure OpenAI
client = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    max_retries=0
)

# Função para traduzir texto para o idioma desejado
def translate_article(text, lang):
    messages = [
        ("system", "Você atua como tradutor de textos"),
        ("user", f"Traduza o seguinte texto para o idioma {lang} e responda em Markdown:\n\n{text}")
    ]
    response = client.invoke(messages)
    return response.content

# Exemplo de uso
if __name__ == "__main__":
    url = "https://dev.to/johnnyreilly/azure-open-ai-handling-capacity-and-quota-limits-with-bicep-4n3k"
    texto_extraido = extract_text_from_url(url)
    traducao = translate_article(texto_extraido, "pt-br")

    print("\n🔍 Tradução em Markdown:\n")
    print(traducao)

    from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")