#Imports de libs
import turtle


#Funções

#Cria a screen do turtle - USO: nome_da_screen = init_screen(size x, size y, imagem de fundo, nome do jogo)
def init_screen(x, y, backgrund, name_game):
    screen = turtle.Screen(); screen.setup(x, y); screen.bgpic(backgrund); screen.title(name_game); return screen

#Cria shapes para usar no turtle - pode adicionar .gif de uma animacao em sequencia, basta terem o mesmo nome e estarem em sequencia de 1 em diante, ex.: nome1
def add_shapes(screen, diretorio):
    for i in range(diretorio[1]):
        screen.addshape(f'{diretorio[0]}{i+1}.gif')

#Cria uma nova turtle - adiciona um novo objeto para o turtle, tribuindo alguma informacoes iniciais
def add_objects(diretorio, speed, hide, x, y):
    objects = turtle.Turtle(); objects.hideturtle(); objects.penup(); objects.speed(0); objects.setpos(x, y)
    if (hide == False):
        objects.showturtle()
    objects.speed(speed); objects.shape(diretorio); return objects