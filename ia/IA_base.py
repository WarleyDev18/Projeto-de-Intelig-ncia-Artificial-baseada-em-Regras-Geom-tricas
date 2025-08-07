from svgpathtools import svg2paths2, Path

# Escala: 1 unidade SVG = 1 cm
ESCALA_CM = 1
ESCALA_M = ESCALA_CM / 100

def calcular_area_path(path: Path):
    try:
        area_svg_units = abs(path.area())
        area_cm2 = area_svg_units * ESCALA_CM ** 2
        area_m2 = area_cm2 / 10000
        return area_m2
    except:
        return None

def calcular_largura_comprimento(path: Path):
    pontos = []
    for segmento in path:
        if hasattr(segmento, 'start'):
            pontos.append(segmento.start)
        if hasattr(segmento, 'end'):
            pontos.append(segmento.end)

    xs = [p.real for p in pontos]
    ys = [p.imag for p in pontos]

    if not xs or not ys:
        return None, None

    largura_svg = max(xs) - min(xs)
    comprimento_svg = max(ys) - min(ys)

    largura_m = abs(largura_svg * ESCALA_M)
    comprimento_m = abs(comprimento_svg * ESCALA_M)

    return largura_m, comprimento_m

def exibir_resultados(paths):
    area_total = 0
    print("Cômodos detectados:")
    for i, path in enumerate(paths):
     try:
        area = calcular_area_path(path)
        largura, comprimento = calcular_largura_comprimento(path)

        if area and area > 0.1:
            print(f" - Cômodo {i+1}:")
            print(f"     Área: {area:.2f} m²")
            print(f"     Largura: {largura:.2f} m")
            print(f"     Comprimento: {comprimento:.2f} m")
            area_total += area
     except Exception as e:
        print(f"Erro ao processar cômodo {i+1}: {e}")

    print(f"\n Área total da planta: {area_total:.2f} m²")

# Carrega o SVG e executa
paths, attributes, svg_attributes = svg2paths2('base.svg')
exibir_resultados(paths)
