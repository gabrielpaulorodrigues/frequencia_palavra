from collections import Counter
from turtle import color
import wget
import os
import matplotlib.pyplot as plt

# Verifica se o arquivo existe
if os.path.exists('livro.txt'):
    print("Arquivo já existe, e não será baixado.")
else:
    print("Arquivo não existe, baixando...")
    wget.download(
        'https://www.gutenberg.org/files/16429/16429-0.txt', 'livro.txt')

with open('livro.txt', encoding="utf-8") as arquivo:
    texto = arquivo.read().lower()

texto_filtrado = ''.join(
    [letra for letra in texto if letra.isalpha() or letra == ' '])

letras = [l for l in texto_filtrado if l.isalpha()]
frequencia_letras = Counter(letras)

rotulos, valores = zip(*frequencia_letras.most_common(10))
plt.title('Ranking das letras que mais aparece no livro')
plt.bar(rotulos, valores)
plt.xlabel('Letras')
plt.ylabel('Frequência')

for i, v in enumerate(valores):
    plt.text(i, v, str(v), fontweight='bold', horizontalalignment='center',
             verticalalignment='bottom', color='red')

plt.show()
