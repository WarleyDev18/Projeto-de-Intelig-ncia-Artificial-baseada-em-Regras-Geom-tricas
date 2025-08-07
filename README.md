[README (1).md](https://github.com/user-attachments/files/21673257/README.1.md)
# 🧠 Projeto de Inteligência Artificial baseada em Regras Geométricas

Este projeto aplica regras matemáticas para **analisar plantas arquitetônicas em SVG** e gerar **sugestões de iluminação automatizadas** com base na geometria dos cômodos.

---

## 💡 Objetivo

Criar um sistema que:
- Analise arquivos SVG contendo plantas de ambientes;
- Calcule área, largura e comprimento de cada cômodo;
- Sugira a quantidade e disposição ideal de lâmpadas;
- Gere visualizações automáticas da planta com as sugestões.

---

## 📁 Estrutura do Projeto

```
/
├── main.py                 # Script principal: executa análise completa
├── ia/
│   ├── IA_base.py          # Cálculos com paths SVG
│   ├── IA_suges.py         # Sugestões com paths e retângulos
│   └── sup.py              # Visualização e lógica de iluminação
├── assets/
│   ├── base.svg            # Planta com paths
│   └── planta3.svg         # Planta com retângulos
├── output/                 # Saída com imagens geradas (opcional)
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd NOME_DO_REPO
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o script principal
```bash
python main.py assets/planta3.svg
```

---

## 📊 Exemplo de Saída

- Cômodos detectados com suas medidas (m², largura, comprimento)
- Imagem com lâmpadas dispostas automaticamente:

```
 - Cômodo 1:
     Área: 8.00 m²
     Largura: 4.00 m
     Comprimento: 2.00 m
```

> 💡 A sugestão de iluminação é baseada em uma distância ideal de 2 metros entre lâmpadas.

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- [svgpathtools](https://pypi.org/project/svgpathtools/)
- [matplotlib](https://matplotlib.org/)
- SVG padrão (com elementos `<path>` ou `<rect>`)

---

## 📎 Licença

Este projeto é de uso livre para fins educacionais ou acadêmicos.  
Sinta-se à vontade para adaptar e expandir.

---

## 🤝 Contribuições

Sugestões, melhorias ou colaborações são muito bem-vindas!  
Abra uma *issue* ou envie um *pull request*.

---

## 📷 Pré-visualização (opcional)

Você pode incluir aqui uma imagem como exemplo da saída:

```
output/
├── Comodo1.png
├── Comodo2.png
```
