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
        for i in range(3):
            screen.bgpic(f'./history/inicio/frame{i+1}.gif')
            screen.update()
            sleep(6)
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
    #Reseta todos os elementos para recomecar o jogo apartir do mapa um
    else:
        if (mapas.final == True):
            mapas.final = False
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

                    mapas.monstros_fase = 6
                    mapas.mapa_atual = 1
                    mapas.ontimer_continuar = True
                    player.showturtle()
                    player.shape('./move/right/mapa1/right1.gif')
                    player.chave.pegou = 0
                    player.chave.shape('./objects/chave1.gif')
                    
                    for i in enemy_name:
                        lista_inimigos[i].ontimer_continuar = True
                        lista_inimigos[i].vida = enemy_list[i]['vida']
                        lista_inimigos[i].frame = 1
                    for i in range(4):
                        lista_inimigos[f'bola_final{i+1}'].ontimer_continuar = True
                    lista_inimigos['estatua'].bola_de_fogo.shape('./projectiles/bola_de_fogo/bola_de_fogo4.gif')
                    lista_inimigos['boss_final'].shape('./enemy/boss_final/boss_final_left1.gif')

                    mapas.mapa_um()
                    return

                screen.bgpic(f'./screen/tela_inicial/tela{i+1}.gif')
                sleep(0.03)
                screen.update()

def iniciar_gamer():
    global play
    play = True