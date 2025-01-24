import json

with open('resultados\mulher2.jpg-atual.jpg.json') as f:
    d = json.load(f)
    print(d)