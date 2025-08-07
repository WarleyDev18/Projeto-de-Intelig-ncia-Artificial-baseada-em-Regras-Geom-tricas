# main.py
import sys
import os
from svgpathtools import svg2paths2, Path
from ia.IA_base import calcular_area_path, calcular_largura_comprimento
from ia.sup import extrair_retangulos_svg, gerar_planta_iluminada
import xml.etree.ElementTree as ET
from svgpathtools import parse_path


def analisar_como_paths(svg_file):
    print("\n[🔍] Analisando com base em <path>...")
    paths, attributes, svg_attributes = svg2paths2(svg_file)
    area_total = 0
    for i, path in enumerate(paths):
        try:
            area = calcular_area_path(path)
            largura, comprimento = calcular_largura_comprimento(path)

            if area and area > 0.1:
                print(f" - Cômodo {i+1}:")
                print(f"     Área: {area:.2f} m²")
                print(f"     Largura: {largura:.2f} m")
                print(f"     Comprimento: {comprimento:.2f} m")

                gerar_planta_iluminada(
                    nome=f"Cômodo {i+1}",
                    largura=largura,
                    comprimento=comprimento,
                    x_offset=0,
                    y_offset=0
                )

                area_total += area
        except Exception as e:
            print(f"Erro ao processar cômodo {i+1}: {e}")
    print(f"\n[✅] Área total dos cômodos: {area_total:.2f} m²")


def analisar_como_retangulos(svg_file):
    print("\n[🔍] Analisando com base em <rect>...")
    comodos = extrair_retangulos_svg(svg_file)
    if not comodos:
        print("Nenhum retângulo encontrado.")
        return

    for i, comodo in enumerate(comodos):
        nome = f"Cômodo {i+1}"
        largura = comodo["largura"]
        comprimento = comodo["comprimento"]
        print(f" - {nome}:")
        print(f"     Largura: {largura:.2f} m")
        print(f"     Comprimento: {comprimento:.2f} m")
        print(f"     Área: {largura * comprimento:.2f} m²")

        gerar_planta_iluminada(
            nome=nome,
            largura=largura,
            comprimento=comprimento,
            x_offset=0,
            y_offset=0
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_svg>")
        sys.exit(1)

    svg_file = sys.argv[1]

    if not os.path.exists(svg_file):
        print(f"Arquivo '{svg_file}' não encontrado.")
        sys.exit(1)

    # Verifica se há <rect> ou <path> no SVG
    tree = ET.parse(svg_file)
    root = tree.getroot()
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}

    has_rects = root.findall('.//svg:rect', namespaces)
    has_paths = root.findall('.//svg:path', namespaces)

    if has_rects:
        analisar_como_retangulos(svg_file)
    elif has_paths:
        analisar_como_paths(svg_file)
    else:
        print("Nenhum <rect> ou <path> encontrado no SVG.")
