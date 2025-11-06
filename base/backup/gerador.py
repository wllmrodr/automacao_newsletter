# Nome do arquivo: gerador.py
import json
from jinja2 import Environment, FileSystemLoader
import os

print("Iniciando a geração da newsletter...")

# Configura o ambiente do Jinja2 para procurar arquivos na mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(script_dir))

# 1. Carrega o template HTML
try:
    template = env.get_template('template.html')
    print("[1/4] Template 'template.html' carregado.")
except Exception as e:
    print(f"ERRO ao carregar 'template.html': {e}")
    exit()

# 2. Carrega os dados do JSON
try:
    with open('dados.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("[2/4] Dados 'dados.json' carregados.")
except Exception as e:
    print(f"ERRO ao carregar 'dados.json': {e}")
    exit()

# 3. Renderiza o template com os dados
try:
    output_html = template.render(**data)
    print("[3/4] HTML renderizado com sucesso.")
except Exception as e:
    print(f"ERRO ao renderizar o template: {e}")
    exit()

# 4. Salva o arquivo final
output_filename = 'newsletter_final.html'
try:
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(output_html)
    
    full_path = os.path.join(script_dir, output_filename)
    print(f"[4/4] Arquivo '{output_filename}' criado com sucesso!")
    print(f"--------------------------------------------------")
    print(f"PROCESSO CONCLUÍDO.")
    print(f"Seu arquivo está aqui: {full_path}")

except Exception as e:
    print(f"ERRO ao salvar o arquivo final: {e}")
    exit()