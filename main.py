#Imports
import turtle; from player import *; from functions_turtle import *; from collision import *; from enemy import *


#Funções

#Movimentação
#Move o personagem para cima
def walk_up():
    global gif_walk_default_number
    
    frame = walk_main(janela, lista_objetos, 90, 10, gif_walk_default_number[0], 4, './move/up/up', teclas_on, teclas_off)
    gif_walk_default_number = reset_frame_walk(frame, 1, 1, 1)
#Move o personagem para baixo
def walk_down():
    global gif_walk_default_number

    frame = walk_main(janela, lista_objetos, 270, 10, gif_walk_default_number[1], 4, './move/down/down', teclas_on, teclas_off)
    gif_walk_default_number = reset_frame_walk(1, frame, 1, 1)
#Move o personagem para a direita
def walk_right():
    global gif_walk_default_number

    frame = walk_main(janela, lista_objetos, 0, 10, gif_walk_default_number[2], 6, './move/right/right', teclas_on, teclas_off)
    gif_walk_default_number = reset_frame_walk(1, 1, frame, 1)
#Move o personagem para esquerda
def walk_left():
    global gif_walk_default_number

    frame = walk_main(janela, lista_objetos, 180, 10, gif_walk_default_number[3], 6, './move/left/left', teclas_on, teclas_off)
    gif_walk_default_number = reset_frame_walk(1, 1, 1, frame)

#Eventos on/off
#Cria todos os eventos de teclado e mouse
def teclas_on(screen):
    #Chama as funcoes para movimentar o personagem ao clicar a tecla referente a cada evento
    funcoes = [walk_up, walk_down, walk_right, walk_left]
    teclas = 'wsda'
    for i in range(len(funcoes)):
        screen.onkeypress(funcoes[i], teclas[i])
    #Ao clicar com o botao esquerdo do mouse o player atira uma flecha no local onde ocorreu o clique
    screen.onclick(shot_bow)
#Desativa todos os eventos de teclado e mouse
def teclas_off(teclas, screen):
    for i in teclas:
        screen.onkeypress(None, i)
    screen.onclick(None)

#Ataque do player com o arco - chama a funcao de tiro do arco se caso o botao esquerdo o mouse for apertado
def shot_bow(x, y):
    atack_bow(x, y, janela, lista_objetos, lista_inimigos, teclas_on, teclas_off, time_shot)
#Reativa a permissao para o arco pode atirar novamente
def time_shot():
    arrow.ataque = True

#Inimigos
#Chama os slimes para o mapa
def chamando_slime():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_slime = slime.pos(); pos_slime_dois = slime_dois.pos()
    
    #Se caso o atributo que permite os slimes continuarem a se mover for true o laco comeca
    if (slime.ontimer_continuar == True or slime_dois.ontimer_continuar == True):
        #Checa se o slime1 pode continuar
        if (slime.ontimer_continuar == True):
            enemy_slime(janela, pos_player, lista_inimigos['slime1'], enemy_list['slime1']['frames'], 1)
            #Se o slime colidir em algo do mapa
            if (collision_map1(slime) == True):
                slime.setpos(pos_slime)
        #Checa se o slime2 pode continuar
        if (slime_dois.ontimer_continuar == True):
            enemy_slime(janela, pos_player, lista_inimigos['slime2'], enemy_list['slime2']['frames'], 2)
            #Se o slime colidir em algo do mapa
            if (collision_map1(slime_dois) == True):
                slime_dois.setpos(pos_slime_dois)
        #Chama novamente a funcao
        janela.ontimer(chamando_slime, 100)

def chamando_morcego():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos()

    if (morcego.ontimer_continuar == True):
        enemy_morcego(janela, pos_player, morcego, enemy_list['morcego1']['frames'])
        janela.ontimer(chamando_morcego, 100)


#Main

#Cria uma lista para ser possivel resetar a animacao da direção do player
gif_walk_default_number = [1, 1, 1, 1] #Elemento 0 = up, 1 = down, 2 = right, 3 = left

#Cria a screen definindo algumas configuracoes como background, dimenssoes da tela e nome do programa
janela = init_screen(1366, 720, './maps/map1/mapa_inicio.gif', 'A torre do desejo')
#Tirando a atualizacao dos frames
janela.tracer(0)

#Adiciona os shapes para usar no turtle
#Adiciona os frames da movimentacao do player + objeto (flecha)
frames_nessa = [['./move/up/up', 4], ['./move/down/down', 4], ['./move/right/right', 6], ['./move/left/left', 6], ['./projectiles/arrow/arrow', 8]]
for i in range(len(frames_nessa)):
    add_shapes(janela, frames_nessa[i])
#Adiciona os frames dos inimigos
for i in enemy_name:
    info = [enemy_list[i]['diretorio'], enemy_list[i]['frames']]
    add_shapes(janela, info)

#Criacao do player + objeto (flecha)
#Player
nessa = add_objects('./move/right/right1.gif', 0, False, -810, 277) #Cria a nessa (personagem principal do jogo)
#Flecha
arrow = add_objects('./projectiles/arrow/arrow1.gif', 1, True, 0, 0) #Cria a flecha
arrow.ataque = True #Cria alguns atributos
#Lista de todos os objetos criados
lista_objetos = {'player': nessa, 'flecha': arrow}

#Criacao de todos os inimigos
#Slimes
#Criando o slime1
slime = add_objects(f'{enemy_list["slime1"]["diretorio"]}1.gif', 1, False, -376, 130) #Adiciona um objeto no turtle
slime.frame = 1; slime.vida = 3; slime.tamanho = [26, 26, 21, 21]; slime.ontimer_continuar = True #Cria alguns atributos
#Criando o slime2
slime_dois = slime.clone(); slime_dois.setpos(150, -235) #Clona um objeto
slime_dois.frame = 1; slime_dois.vida = 3; slime_dois.tamanho = [26, 26, 21, 21]; slime_dois.ontimer_continuar = True #Cria alguns atributos
#Morcegos
morcego = add_objects(f'{enemy_list["morcego1"]["diretorio"]}1.gif', 1, False, 600, -170) #Adiciona um objeto no turtle
morcego.frame = 1; morcego.vida = 2; morcego.tamanho = [29, 29, 18, 18]; morcego.ontimer_continuar = True #Cria alguns atributos
#Lista de todos os inimigos criados
lista_inimigos = {'slime1': slime, 'slime2': slime_dois, 'morcego1': morcego}


#Chama os monstros para o mapa
#Chamando os slimes
chamando_slime()
#Chamando os morcegos
chamando_morcego()

#Eventos da janela
janela.listen()
#Ativa todos os eventos de clique e teclado
teclas_on(janela)


#Loop - para manter a tela aberta
janela.mainloop()