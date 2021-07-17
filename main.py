import turtle
def principal():
    cor = 'red'
    ax = int(input('Digite a coordenada x do primeiro ponto do triângulo: '))
    ay = int(input('Digite a coordenada y do primeiro ponto do triângulo: '))
    bx = int(input('Digite a coordenada x do segundo ponto do triângulo: '))
    by = int(input('Digite a coordenada y do segundo ponto do triângulo: '))
    cx = int(input('Digite a coordenada x do terceiro ponto do triângulo: '))
    cy = int(input('Digite a coordenada y do terceiro ponto do triângulo: '))
    opcao = int(input('Digite (1) para Translação ou (2) para Escala'))
    if opcao == 2:
        alfa = int(input('Digite o valor de alfa: '))
        trianguloGenerico(ax, ay, bx, by, cx, cy, cor)
        escala(ax, ay, bx, by, cx, cy, alfa)
    elif opcao ==1:
        xt = int(input('Digite os valor de xt'))
        yt = int(input('Digite os valor de yt'))
        trianguloGenerico(ax, ay, bx, by, cx, cy, cor)
        translacao(ax, ay, bx, by, cx, cy, xt, yt)

def trianguloGenerico(x1, y1, x2, y2, x3, y3, z):
    t = turtle.Turtle()
    t.color(z)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.penup()


def escala(x1, y1, x2, y2, x3, y3, alfa):
    ex1 = x1 * alfa
    ey1 = y1 * alfa
    ex2 = x2 * alfa
    ey2 = y2 * alfa
    ex3 = x3 * alfa
    ey3 = y3 * alfa
    z_ = 'green'
    trianguloGenerico(ex1, ey1, ex2, ey2, ex3, ey3, z_)

def translacao(x1, y1, x2, y2, x3, y3, a, b):
    ex1 = x1 + a
    ey1 = y1 + b
    ex2 = x2 + a
    ey2 = y2 + b
    ex3 = x3 + a
    ey3 = y3 + b
    z1 = 'blue'
    trianguloGenerico(ex1, ey1, ex2, ey2, ex3, ey3, z1)

principal()
