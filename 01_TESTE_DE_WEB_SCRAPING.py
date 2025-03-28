import requests
from bs4 import BeautifulSoup
import wget
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

elementos = soup.find_all('li')
c = 1

for elemento in elementos:
    tag_a = elemento.find('a', class_='internal-link')

    if tag_a:
        wget.download(tag_a.get('href'),  f'Anexo{c}.pdf')
        c+=1

with zipfile.ZipFile('anexos.zip', 'w') as zip:
    zip.write('Anexo1.pdf')
    zip.write('Anexo2.pdf')

os.remove('Anexo1.pdf')
os.remove('Anexo2.pdf')