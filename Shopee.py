import requests
from bs4 import BeautifulSoup

# Função para obter o preço do produto
def obter_preco_shopee(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    # Fazer requisição à página do produto
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parsear o HTML da página usando o parser nativo
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontra o elemento do preço (ajuste isso com base no HTML da página)
        preco_elemento = soup.find("span", class_="pdp-price")
        
        if preco_elemento:
            preco = preco_elemento.text.strip()
            print(f"Preço atual do produto: {preco}")
        else:
            print("Não foi possível encontrar o preço do produto.")
    else:
        print(f"Erro ao acessar a página. Código de status: {response.status_code}")

# URL do produto na Shopee
url_produto = "https://br.shp.ee/oxq9oih"
obter_preco_shopee(url_produto)
