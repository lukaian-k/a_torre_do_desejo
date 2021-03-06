#Imports de libs
from time import sleep
#Imports de arquivos da propria pasta
from menu import inicio


#Funcao que limpa a tela e muda alguma informacoes sobre o estado do jogo
def game_over(screen, player, lista_inimigos, enemy_name, teclas_off, mapas):
    #Bloqueia todos os eventos de ontimer, move e oculta todos os objetos
    mapas.ontimer_continuar = False; player.arrow.hideturtle(); player.hideturtle(); player.setpos(-810, 277)
    teclas_off('wsda', screen) #Desativa todos os eventos de teclado e mouse
    
    #Ocultando todos os inimidos e movendo eles para um lugar onde nao iram afetar o jogo
    for i in enemy_name:
        lista_inimigos[i].ontimer_continuar = False; lista_inimigos[i].hideturtle()
        if (i == 'estatua'):
            lista_inimigos[i].bola_de_fogo.hideturtle(); lista_inimigos[i].bola_de_fogo.setheading(0)
        if (i == 'estatua' or i == 'boss_final'):
            lista_inimigos[i].tempo_animacao = 0
        lista_inimigos[i].setpos(0, 1000)
    for i in range(4):
        lista_inimigos[f'bola_final{i+1}'].ontimer_continuar = False; lista_inimigos[f'bola_final{i+1}'].hideturtle(); lista_inimigos[f'bola_final{i+1}'].setpos(0, 1000); lista_inimigos[f'bola_final{i+1}'].tempo_animacao = 0

    #Muda o estado de qual mapa o jogo esta e atualiza o frame atual da tela
    screen.update(); mapas.mapa_atual = 0

    #Informa quais mapas foram jogados ate o momento
    mapas.mapa1_reiniciado = True
    if (mapas.mapa_atual >= 2):
        mapas.mapa2_reiniciado = True
    if (mapas.mapa_atual >= 3):
        mapas.mapa3_reiniciado = True

    #Tela de game over
    if (mapas.final == False):
        for i in range(15):
            screen.bgpic(f'./screen/game_over/frame{i+1}.gif'); screen.update(); sleep(0.01)
        sleep(3)

    #Chama a funcao para reiniciar o jogo novamente
    inicio(screen, player, lista_inimigos, enemy_name, mapas) #Chama a tela inicial do jogo para que o jogador posso iniciar novamente