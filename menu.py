from time import sleep
from enemy import enemy_list


def inicio(screen, player, lista_inimigos, enemy_name, mapas):
    global play
    play = False

    if (mapas.mapa1_reiniciado == False):
        for i in range(70):
            screen.bgpic(f'./screen/equipe/dev{i+1}.gif')
            screen.update()
            sleep(0.01)
        screen.onkey(iniciar_gamer, 'Return')

        while True:
            for i in range(10):
                if (play == True):
                    play = False
                    screen.onkey(None, 'Return')
                    return True
                screen.bgpic(f'./screen/tela_inicial/tela{i+1}.gif')
                sleep(0.03)
                screen.update()
    else:
        if (mapas.final == True):
            mapas.ontimer_continuar = False
            for i in range(70):
                screen.bgpic(f'./screen/equipe/dev{i+1}.gif')
                screen.update()
                sleep(0.01)
        screen.onkey(iniciar_gamer, 'Return')

        while True:
            for i in range(10):
                if (play == True):
                    play = False
                    screen.onkey(None, 'Return')
                    
                    mapas.mapa1_reiniciado = True
                    if (mapas.mapa_atual >= 2):
                        mapas.mapa2_reiniciado = True
                    if (mapas.mapa_atual >= 3):
                        mapas.mapa3_reiniciado = True

                    mapas.monstros_fase = 6
                    mapas.mapa_atual = 1
                    mapas.ontimer_continuar = True
                    mapas.final = False
                    player.showturtle()
                    player.shape('./move/right/mapa1/right1.gif')
                    player.chave.pegou = 0
                    player.chave.shape('./objects/chave1.gif')
                    
                    for i in enemy_name:
                        lista_inimigos[i].ontimer_continuar = True
                        lista_inimigos[i].vida = enemy_list[i]['vida']
                        lista_inimigos[i].frame = 1
                    lista_inimigos['estatua'].bola_de_fogo.setheading(0)
                    lista_inimigos['estatua'].bola_de_fogo.shape('./projectiles/bola_de_fogo/bola_de_fogo4.gif')
                    lista_inimigos['estatua'].tempo_animacao = 0
                    lista_inimigos['boss_final'].tempo_animacao = 0

                    mapas.mapa_um()
                    return

                screen.bgpic(f'./screen/tela_inicial/tela{i+1}.gif')
                sleep(0.03)
                screen.update()

def iniciar_gamer():
    global play
    play = True