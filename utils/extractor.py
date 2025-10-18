import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\n", strip=True)

if __name__ == "__main__":
    url = "https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial"
    texto = extract_text_from_url(url)
    print("\n🔍 Texto extraído da página:")
    print(texto[:1000] + "...\n")  # Mostra os primeiros 1000 caracteres