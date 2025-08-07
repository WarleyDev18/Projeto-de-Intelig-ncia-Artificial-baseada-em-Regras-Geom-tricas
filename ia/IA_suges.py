import xml.etree.ElementTree as ET
from svgpathtools import parse_path
from sup import extrair_retangulos_svg
from sup import gerar_planta_iluminada

def calcular_area_svg(path_d):
    path = parse_path(path_d)
    area = 0.0
    for subpath in path.continuous_subpaths():
        area += abs(subpath.area())  # Área absoluta (sem sinal negativo)
    return area

def analisar_svg(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}

    # Encontra todos os elementos <path>
    paths = root.findall('.//svg:path', namespaces)

    comodos = extrair_retangulos_svg("planta3.svg")
    gerar_planta_iluminada(comodos)


    for element in paths:
        d = element.attrib.get('d')
        if not d:
            continue  # Ignora se não há definição de path

        eid = element.attrib.get('id', '')
        cls = element.attrib.get('class', '')

        # Se quiser logar os que têm dados mas sem id/class
        if not eid and not cls:
            print("Path sem id/class, mas com dados:", d[:40], "...")

        try:
            area = calcular_area_svg(d)
            comodos.append((eid or "sem_id", area))
        except Exception as e:
            print(f"Erro ao calcular área do path {eid}: {e}")

    # Ordena por área decrescente
    comodos.sort(key=lambda x: x[1], reverse=True)

    print("\nResumo dos cômodos válidos:")
    for nome, area in comodos:
        print(f" - {nome}: {area:.2f} unidades²")

# Exemplo de uso:
analisar_svg("planta3.svg")
