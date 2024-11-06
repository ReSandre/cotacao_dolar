from bs4 import BeautifulSoup
import requests

link = 'https://www.google.com/search?q=cotacao+dolar'
headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, 'html.parser')


cotacao = site.find('span', class_="DFlfde SwHCTb")
print(cotacao.getText())
print(f'Cotação do dólar hoje:{cotacao['data-value']}')