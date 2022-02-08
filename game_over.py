#Imports de libs
from time import sleep
from menu import inicio


def game_over(screen, player, lista_inimigos, enemy_name, teclas_off, mapas):
    #Bloqueia todos os eventos de ontimer, move e oculta todos os objetos
    mapas.ontimer_continuar = False
    player.arrow.hideturtle()
    player.hideturtle()
    player.setpos(-810, 277)
    teclas_off('wsda', screen) #Desativa todos os eventos de teclado e mouse
    for i in enemy_name:
        lista_inimigos[i].ontimer_continuar = False
        lista_inimigos[i].hideturtle()
        if (i == 'estatua'):
            lista_inimigos[i].bola_de_fogo.hideturtle()
        lista_inimigos[i].setpos(0, 1000)

    screen.update()
    mapas.mapa_atual = 0
    #Tela de game over
    for i in range(15):
        screen.bgpic(f'./screen/game_over/frame{i+1}.gif')
        screen.update()
        sleep(0.01)
    sleep(3)

    inicio(screen, player, lista_inimigos, enemy_name, mapas) #Chama a tela inicial do jogo para que o jogador posso iniciar novamente