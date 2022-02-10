#Imports de libs
from time import sleep
#Imports de arquivos da propria pasta
from enemy import enemy_list


#Funcao que inicia e reinicia o jogo
def inicio(screen, player, lista_inimigos, enemy_name, mapas):
    global play; play = False

    #Se caso o jogo for iniciado pela primeira vez
    if (mapas.mapa1_reiniciado == False):
        #Exibe os nomes da equipe de desenvolvimento e conta a historia do jogo
        for i in range(70):
            screen.bgpic(f'./screen/equipe/dev{i+1}.gif'); screen.update(); sleep(0.01)
        for i in range(3):
            screen.bgpic(f'./history/inicio/frame{i+1}.gif'); screen.update(); sleep(6)
        #Ativa o evento da tecla 'Enter'
        screen.onkey(iniciar_gamer, 'Return')
        
        #Inicia o laco que so acabara apos o jogador prescionar a tecla 'Enter'
        while True:
            for i in range(10):
                #Caso seja verdade inicia o jogo
                if (play == True):
                    play = False; screen.onkey(None, 'Return'); return True
                #Caso o jogo ainda nao seja reiniciado
                screen.bgpic(f'./screen/tela_inicial/tela{i+1}.gif'); sleep(0.03); screen.update()
    #Reseta todos os elementos para recomecar o jogo apartir do mapa um
    else:
        #Se o jogo tiver sido finalizado ir exibir novamente os nomes dos criadores do jogo
        if (mapas.final == True):
            mapas.final = False
            for i in range(70):
                screen.bgpic(f'./screen/equipe/dev{i+1}.gif'); screen.update(); sleep(0.01)
        #Ativa o evento de tecla 'Enter'
        screen.onkey(iniciar_gamer, 'Return')

        while True:
            for i in range(10):
                #Caso seja verdade reinicia o jogo resetando todas as informacoes do jogo como se ele tive-se acabado de iniciar pela primeira vez
                if (play == True):
                    play = False; screen.onkey(None, 'Return')

                    #Altera alguns valores e muda alguns sprites
                    mapas.monstros_fase = 6;  mapas.mapa_atual = 1; mapas.ontimer_continuar = True
                    player.showturtle(); player.shape('./move/right/mapa1/right1.gif'); player.chave.pegou = 0; player.chave.shape('./objects/chave1.gif')
                    
                    #Altera algumas propriedades dos inimigos do jogo
                    for i in enemy_name:
                        lista_inimigos[i].ontimer_continuar = True; lista_inimigos[i].vida = enemy_list[i]['vida']; lista_inimigos[i].frame = 1
                    for i in range(4):
                        lista_inimigos[f'bola_final{i+1}'].ontimer_continuar = True
                    lista_inimigos['estatua'].bola_de_fogo.shape('./projectiles/bola_de_fogo/bola_de_fogo4.gif')
                    lista_inimigos['boss_final'].shape('./enemy/boss_final/boss_final_left1.gif')

                    #Chama a funcao responsavel por iniciar o mapa um
                    mapas.mapa_um()
                    return

                #Caso nao o jogo nao seja reiniciado ainda
                screen.bgpic(f'./screen/tela_inicial/tela{i+1}.gif'); sleep(0.03); screen.update()
#Chamada quando a tecla enter for pressionada dando assim a permissao para iniciar/reiniciar o jogo
def iniciar_gamer():
    global play; play = True