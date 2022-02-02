#Imports
import turtle; from enemy import enemy_name


#Funções

#Cria uma colisao em um eixo x, e eixo y - se chamada duas vezes pode-se criar uma colisao no formato de um quadrado
def collision_screen(objeto, x, y):
    xcor_objeto = objeto.xcor(); ycor_objeto = objeto.ycor()

    if (x >= 0): #X possitivo
        if (y >= 0): #X e Y positivos
            if (xcor_objeto > x or ycor_objeto > y):
                return True
        else: #X possitivo e Y negativo
            if (xcor_objeto > x or ycor_objeto < y):
                return True
    else: #X negativo
        if (y >= 0): #X negativo e Y positivo
            if (xcor_objeto < x or ycor_objeto > y):
                return True
        else: #X e Y negativo
            if (xcor_objeto < x or ycor_objeto < y):
                return True
    return False

#Cria uma colisao aparti de uma coordenada x e y, informando mais duas informacoes para cada eixo é possivel criar um area de colisao no formato de um quadrado ou retangulo
def collision_square(objeto, x, x_menos, x_mais, y, y_menos, y_mais):
    xcor_objeto = objeto.xcor(); ycor_objeto = objeto.ycor()
        
    if (y-y_menos < ycor_objeto < y+y_mais and x-x_menos < xcor_objeto < x+x_mais):
        return True
    return False

#Colisao com inimigos - informando uma lista dos inimigos que é necessario verificar se a colisao e informa o objeto que colidio com ele, a funcao ira retornar qual inimigo colidio caso haja a colisao
def collision_enemy(lista_inimigos, objeto):
    for i in range(len(enemy_name)):
        x = lista_inimigos[enemy_name[i]].xcor(); y = lista_inimigos[enemy_name[i]].ycor()

        if (collision_square(objeto, x, lista_inimigos[enemy_name[i]].tamanho[0], lista_inimigos[enemy_name[i]].tamanho[1], y, lista_inimigos[enemy_name[i]].tamanho[2], lista_inimigos[enemy_name[i]].tamanho[3]) == True):
            return lista_inimigos[enemy_name[i]]

#Colisoes de cada mapa - aqui esta cada colisao com o cenario de cada mapa
#Mapa1 - Checa se aconteceu alguma colisao em alguma regiao do cenario
def collision_map1(objeto):
    #Colisao com as paredes no mapa
    coordenadas_paredes = [[770, 340], [-820, -325]]
    for i in range(len(coordenadas_paredes)):
        if (collision_screen(objeto, coordenadas_paredes[i][0], coordenadas_paredes[i][1]) == True):
            return True
    
    if (collision_square(objeto, 280, 340, 340, 190, 230, 250) == True):
        return True

    #Colisao das caixas no mapa
    #Posicao dos elementos na lista: 0 = x, 1 = y, 2 = x_menos, 3 = x_mais, 4 = y_menos, 5 = y_mais
    if (objeto.voador == False):
        coordenadas_caixas = [[-823, -97, 20, 30, 10, 50], [-435, -32, 30, 30, 10, 50], [-375, 287, 30, 30, 10, 60], [-180, 30, 30, 30, 10, 50], [-52, 289, 30, 30, 10, 60], [75, -295, 30, 30, 10, 60], [397, -103, 30, 30, 9, 60], [779, -168, 30, 30, 10, 60], [743, 92, 30, 25, 10, 60], [616, 289, 30, 30, 10, 50], [745, 288, 30, 30, 10, 60]]
        for i in range(len(coordenadas_caixas)):
            if (collision_square(objeto, coordenadas_caixas[i][0], coordenadas_caixas[i][2], coordenadas_caixas[i][3], coordenadas_caixas[i][1], coordenadas_caixas[i][4], coordenadas_caixas[i][5]) == True):
                return True
    return False