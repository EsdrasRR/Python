'''
MatPlot Commands List:

------------------------------------------------------------

    Markers(marker)
    '.'	point marker
    ','	pixel marker
    'o'	circle marker
    'v'	triangle_down marker
    '^'	triangle_up marker
    '<'	triangle_left marker
    '>'	triangle_right marker
    '1'	tri_down marker
    '2'	tri_up marker
    '3'	tri_left marker
    '4'	tri_right marker
    's'	square marker
    'p'	pentagon marker
    '*'	star marker
    'h'	hexagon1 marker
    'H'	hexagon2 marker
    '+'	plus marker
    'x'	x marker
    'D'	diamond marker
    'd'	thin_diamond marker
    '|'	vline marker
    '_'	hline marker

------------------------------------------------------------

    Line Styles(linestyle)
    '-'	solid line style
    '--'	dashed line style
    '-.'	dash-dot line style
    ':'	dotted line style

------------------------------------------------------------

    Colors(color)
    'b'	blue
    'g'	green
    'r'	red
    'c'	cyan
    'm'	magenta
    'y'	yellow
    'k'	black
    'w'	white

------------------------------------------------------------

'''


# Visualização de dados em Python

import matplotlib.pyplot as plt 

def graficoDeLinhas():
    x = [1,2,3,4]
    y = [2,3,6,9]

    titulo = "Gráfico de Linhas"
    eixox = "Eixo X"
    eixoy = "Eixo Y"

    # Legendas
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)

    # Construindo gráfico de linhas
    plt.plot(x,y)

    # Exibindo gráfico
    plt.show()

def graficoDeBarras():
    x = [1,2,3,4]
    y = [2,3,6,9]

    titulo = "Gráfico de Barras"
    eixox = "Eixo X"
    eixoy = "Eixo Y"

    # Legendas
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)

    # Construindo gráfico de barras
    plt.bar(x,y)

    # Exibindo gráfico
    plt.show()

def comparandoGraficoDeBarras():
    x1 = [1,3,5,7,9]
    y1 = [2,3,6,9,3]

    x2 = [2,4,6,8,10]
    y2 = [1,4,2,7,4]

    titulo="Comparação de Gráficos de Barras"
    eixox="Eixo X"
    eixoy="Eixo Y"

    # Legendas
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)

    # Construindo gráfico de barras
    plt.bar(x1,y1, label="Grupo 1")
    plt.bar(x2,y2, label="Grupo 2")
    plt.legend()

    # Exibindo gráfico
    plt.show()

def scatterplot():
    x = [1,3,5,7,9]
    y = [2,3,6,9,3]

    titulo = "Scatterplot: Gráfico de Dispersão"
    eixox = "Eixo X"
    eixoy = "Eixo Y"

    # Legendas
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)

    # Construindo gráfico de dispersão juntamento com o de linhas
    plt.scatter(x,y, label="Pontos", color="r", marker="h", s=100)
    plt.plot(x,y, color="k", linestyle=":")
    plt.legend()

    # Exibindo gráfico
    plt.show()

    # Salvando gráfico
    plt.savefig("grafico1.png", dpi=300)

scatterplot()