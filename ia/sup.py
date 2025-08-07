import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import math

def extrair_retangulos_svg(arquivo_svg):
    tree = ET.parse(arquivo_svg)
    root = tree.getroot()

    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    comodos = []

    for rect in root.findall('.//svg:rect', namespaces):
        x = float(rect.get('x', 0))
        y = float(rect.get('y', 0))
        width = float(rect.get('width', 0))
        height = float(rect.get('height', 0))

        comodos.append({
            "nome": "Cômodo Detectado",
            "largura": width / 100,  # converter para metros
            "comprimento": height / 100,
            "lux": 150
        })

    return comodos

import matplotlib.pyplot as plt

def gerar_planta_iluminada(nome, largura, comprimento, x_offset, y_offset, margem=0.5, distancia_ideal=2.0):
    largura_util = largura - 2 * margem
    comprimento_util = comprimento - 2 * margem

    # Quantidade de lâmpadas na horizontal e vertical
    colunas = max(1, round(largura_util / distancia_ideal))
    linhas = max(1, round(comprimento_util / distancia_ideal))

    # Espaçamento real entre lâmpadas
    dx = largura_util / max(1, colunas - 1) if colunas > 1 else 0
    dy = comprimento_util / max(1, linhas - 1) if linhas > 1 else 0

    # Cálculo do início da malha centralizada
    inicio_x = x_offset + margem + (largura_util - (colunas - 1) * dx) / 2
    inicio_y = y_offset + margem + (comprimento_util - (linhas - 1) * dy) / 2

    # Coordenadas das lâmpadas
    lampadas = [
        (inicio_x + i * dx, inicio_y + j * dy)
        for j in range(linhas)
        for i in range(colunas)
    ]

    # Plotagem
    fig, ax = plt.subplots()
    ax.set_title(f"Cômodo: {nome}")
    ax.set_xlim(x_offset - 1, x_offset + largura + 1)
    ax.set_ylim(y_offset - 1, y_offset + comprimento + 1)
    ax.set_aspect('equal')
    ax.set_facecolor('white')

    # Desenha o cômodo
    rect = plt.Rectangle((x_offset, y_offset), largura, comprimento, facecolor='lightgray', edgecolor='black')
    ax.add_patch(rect)

    # Desenha as lâmpadas
    for x, y in lampadas:
        ax.plot(x, y, 'o', color='yellowgreen', markersize=8)

    plt.show()


# EXEMPLO PRÁTICO
gerar_planta_iluminada(
    nome="Sala",
    largura=6,         # Eixo X
    comprimento=4,     # Eixo Y
    x_offset=0,
    y_offset=0
)
