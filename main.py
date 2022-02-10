#Imports de libs
import turtle
#Imports de arquivos da propria pasta
from player import *; from functions_turtle import *; from collision import *; from enemy import *; from game_over import *; from menu import *


#Funções

#Movimentação
#Move o personagem para cima
def walk_up():
    global gif_walk_default_number
    
    if (mapas.mapa_atual == 1):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 90, 10, gif_walk_default_number[0], 4, './move/up/mapa1/up', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 2):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 90, 10, gif_walk_default_number[0], 4, './move/up/mapa2/up', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 3):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 90, 10, gif_walk_default_number[0], 4, './move/up/mapa3/up', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 4):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 90, 10, gif_walk_default_number[0], 4, './move/up/fim/up', teclas_on, teclas_off, mapas)
    gif_walk_default_number = reset_frame_walk(frame, 1, 1, 1)
#Move o personagem para baixo
def walk_down():
    global gif_walk_default_number

    if (mapas.mapa_atual == 1):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 270, 10, gif_walk_default_number[1], 4, './move/down/mapa1/down', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 2):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 270, 10, gif_walk_default_number[1], 4, './move/down/mapa2/down', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 3):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 270, 10, gif_walk_default_number[1], 4, './move/down/mapa3/down', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 4):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 270, 10, gif_walk_default_number[1], 4, './move/down/fim/down', teclas_on, teclas_off, mapas)
    gif_walk_default_number = reset_frame_walk(1, frame, 1, 1)
#Move o personagem para a direita
def walk_right():
    global gif_walk_default_number

    if (mapas.mapa_atual == 1):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 0, 10, gif_walk_default_number[2], 6, './move/right/mapa1/right', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 2):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 0, 10, gif_walk_default_number[2], 6, './move/right/mapa2/right', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 3):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 0, 10, gif_walk_default_number[2], 6, './move/right/mapa3/right', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 4):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 0, 10, gif_walk_default_number[2], 6, './move/right/fim/right', teclas_on, teclas_off, mapas)
    gif_walk_default_number = reset_frame_walk(1, 1, frame, 1)
#Move o personagem para esquerda
def walk_left():
    global gif_walk_default_number

    if (mapas.mapa_atual == 1):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 180, 10, gif_walk_default_number[3], 6, './move/left/mapa1/left', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 2):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 180, 10, gif_walk_default_number[3], 6, './move/left/mapa2/left', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 3):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 180, 10, gif_walk_default_number[3], 6, './move/left/mapa3/left', teclas_on, teclas_off, mapas)
    elif (mapas.mapa_atual == 4):
        frame = walk_main(janela, lista_objetos, lista_inimigos, 180, 10, gif_walk_default_number[3], 6, './move/left/fim/left', teclas_on, teclas_off, mapas)
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
    atack_bow(x, y, janela, lista_objetos, lista_inimigos, teclas_on, teclas_off, time_shot, mapas)
#Reativa a permissao para o arco pode atirar novamente
def time_shot():
    nessa.arrow.ataque = True

#Inimigos
#Chama os slimes para o mapa
def chamando_slime():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_slime = slime.pos(); pos_slime_dois = slime_dois.pos()
    
    #Se caso o atributo que permite os slimes continuarem a se mover for true o laco comeca
    if (slime.ontimer_continuar == True or slime_dois.ontimer_continuar == True):
        #Checa se o slime1 pode continuar
        if (slime.ontimer_continuar == True and mapas.inimigos_quantidade['slime'] >= 1):
            slime.showturtle()
            enemy_persegue(janela, pos_player, 'slime1', lista_inimigos, enemy_list, 5)
            #Se o slime colidir em algo do mapa
            if (collision_mapa(slime, mapas) == True):
                slime.setpos(pos_slime)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

        #Checa se o slime2 pode continuar
        if (slime_dois.ontimer_continuar == True and mapas.inimigos_quantidade['slime'] >= 2):
            slime_dois.showturtle()
            enemy_persegue(janela, pos_player, 'slime2', lista_inimigos, enemy_list, 5)
            #Se o slime colidir em algo do mapa
            if (collision_mapa(slime_dois, mapas) == True):
                slime_dois.setpos(pos_slime_dois)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Chama novamente a funcao
    janela.ontimer(chamando_slime, 100)
#Chama os morcegos para o mapa
def chamando_morcego():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_morcego = morcego.pos(); pos_morcego_dois = morcego_dois.pos()

    #Se caso o atributo que permite os morcegos continuarem a se mover for true o laco comeca
    if (morcego.ontimer_continuar == True or morcego_dois.ontimer_continuar == True):
        #Checa se o morcego1 pode continuar
        if (morcego.ontimer_continuar == True and mapas.inimigos_quantidade['morcego'] >= 1):
            morcego.showturtle()
            enemy_persegue(janela, pos_player, 'morcego1',lista_inimigos, enemy_list, 10)
            #Se o morcego colidir em algo do mapa
            if (collision_mapa(morcego, mapas) == True):
                morcego.setpos(pos_morcego)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

        #Checa se o morcego2 pode continuar
        if (morcego_dois.ontimer_continuar == True and mapas.inimigos_quantidade['morcego'] >= 2):
            morcego_dois.showturtle()
            enemy_persegue(janela, pos_player, 'morcego2', lista_inimigos, enemy_list, 10)
            #Se o morcego colidir em algo do mapa
            if (collision_mapa(morcego_dois, mapas) == True):
                morcego_dois.setpos(pos_morcego_dois)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Chama novamente a funcao
    janela.ontimer(chamando_morcego, 100)
#Chama os slimes grande para o mapa
def chamando_slime_grande():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_slime_grande = slime_grande.pos(); pos_slime_grande_dois = slime_grande_dois.pos()
    
    #Se caso o atributo que permite os slimes grande continuarem a se mover for true o laco comeca
    if (slime_grande.ontimer_continuar == True or slime_grande_dois.ontimer_continuar == True):
        #Checa se o slime_grande1 pode continuar
        if (slime_grande.ontimer_continuar == True and mapas.inimigos_quantidade['slime_grande'] >= 1):
            slime_grande.showturtle()
            enemy_persegue(janela, pos_player, 'slime_grande1', lista_inimigos, enemy_list, 5)
            #Se o slime grande colidir em algo do mapa
            if (collision_mapa(slime_grande, mapas) == True):
                slime_grande.setpos(pos_slime_grande)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o slime_grande2 pode continuar
        if (slime_grande_dois.ontimer_continuar == True and mapas.inimigos_quantidade['slime_grande'] >= 2):
            slime_grande_dois.showturtle()
            enemy_persegue(janela, pos_player, 'slime_grande2', lista_inimigos, enemy_list, 5)
            #Se o slime grande colidir em algo do mapa
            if (collision_mapa(slime_grande_dois, mapas) == True):
                slime_grande_dois.setpos(pos_slime_grande_dois)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
                
    #Chama novamente a funcao
    janela.ontimer(chamando_slime_grande, 100)
#Chama a estatua para o mapa
def chamando_estatua():
    #Se caso o atributo que permite a estatua continuarem a se mover for true o laco comeca
    if (estatua.ontimer_continuar == True and mapas.inimigos_quantidade['estatua'] >= 1):
        estatua.showturtle()
        if (acao_estatua(janela, estatua, nessa, collision_enemy_projectiles, 4) == True):
            estatua.setpos(0, 1000)
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
    else:
        estatua.bola_de_fogo.hideturtle()
        janela.update()

    #Chama novamente a funcao
    janela.ontimer(chamando_estatua, 30)
#Chama os demonios para o mapa
def chamando_demonio():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_demonio_um = demonio_um.pos(); pos_demonio_dois = demonio_dois.pos(); pos_demonio_tres = demonio_tres.pos(); pos_demonio_quatro = demonio_quatro.pos()
    
    #Se caso o atributo que permite os demonios continuarem a se mover for true o laco comeca
    if (demonio_um.ontimer_continuar == True or demonio_dois.ontimer_continuar == True or demonio_tres.ontimer_continuar == True or demonio_quatro.ontimer_continuar == True):
        #Checa se o demonio1 pode continuar
        if (demonio_um.ontimer_continuar == True and mapas.inimigos_quantidade['demonio'] >= 1):
            demonio_um.showturtle()
            enemy_persegue(janela, pos_player, 'demonio1', lista_inimigos, enemy_list, 10)
            #Se o demonio1 colidir em algo do mapa
            if (collision_mapa(demonio_um, mapas) == True):
                demonio_um.setpos(pos_demonio_um)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o demonio2 pode continuar
        if (demonio_dois.ontimer_continuar == True and mapas.inimigos_quantidade['demonio'] >= 2):
            demonio_dois.showturtle()
            enemy_persegue(janela, pos_player, 'demonio2', lista_inimigos, enemy_list, 10)
            #Se o demonio2 colidir em algo do mapa
            if (collision_mapa(demonio_dois, mapas) == True):
                demonio_dois.setpos(pos_demonio_dois)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o demonio3 pode continuar
        if (demonio_tres.ontimer_continuar == True and mapas.inimigos_quantidade['demonio'] >= 3):
            demonio_tres.showturtle()
            enemy_persegue(janela, pos_player, 'demonio3', lista_inimigos, enemy_list, 10)
            #Se o demonio3 colidir em algo do mapa
            if (collision_mapa(demonio_tres, mapas) == True):
                demonio_tres.setpos(pos_demonio_tres)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o demonio4 pode continuar
        if (demonio_quatro.ontimer_continuar == True and mapas.inimigos_quantidade['demonio'] >= 4):
            demonio_quatro.showturtle()
            enemy_persegue(janela, pos_player, 'demonio4', lista_inimigos, enemy_list, 10)
            #Se o demonio4 colidir em algo do mapa
            if (collision_mapa(demonio_quatro, mapas) == True):
                demonio_quatro.setpos(pos_demonio_quatro)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
                
    #Chama novamente a funcao
    janela.ontimer(chamando_demonio, 100)
#Chama os esqueletos para o mapa
def chamando_esqueleto():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos(); pos_esqueleto_um = esqueleto_um.pos(); pos_esqueleto_dois = esqueleto_dois.pos(); pos_esqueleto_tres = esqueleto_tres.pos(); pos_esqueleto_quatro = esqueleto_quatro.pos(); pos_esqueleto_cinco = esqueleto_cinco.pos(); pos_esqueleto_seis = esqueleto_seis.pos(); pos_esqueleto_sete = esqueleto_sete.pos(); pos_esqueleto_oito = esqueleto_oito.pos()
    
    #Se caso o atributo que permite os esqueletos continuarem a se mover for true o laco comeca
    if (esqueleto_um.ontimer_continuar == True or esqueleto_dois.ontimer_continuar == True or esqueleto_tres.ontimer_continuar == True or esqueleto_quatro.ontimer_continuar == True or esqueleto_cinco.ontimer_continuar == True or esqueleto_seis.ontimer_continuar == True or esqueleto_sete.ontimer_continuar == True or esqueleto_oito.ontimer_continuar == True):
        #Checa se o esqueleto1 pode continuar
        if (esqueleto_um.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 1):
            esqueleto_um.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto1', lista_inimigos, enemy_list, 8)
            #Se o esqueleto1 colidir em algo do mapa
            if (collision_mapa(esqueleto_um, mapas) == True):
                esqueleto_um.setpos(pos_esqueleto_um)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o esqueleto2 pode continuar
        if (esqueleto_dois.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 2):
            esqueleto_dois.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto2', lista_inimigos, enemy_list, 8)
            #Se o esqueleto colidir em algo do mapa
            if (collision_mapa(esqueleto_dois, mapas) == True):
                esqueleto_dois.setpos(pos_esqueleto_dois)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o esqueleto3 pode continuar
        if (esqueleto_tres.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 3):
            esqueleto_tres.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto3', lista_inimigos, enemy_list, 8)
            #Se o esqueleto3 colidir em algo do mapa
            if (collision_mapa(esqueleto_tres, mapas) == True):
                esqueleto_tres.setpos(pos_esqueleto_tres)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o esqueleto4 pode continuar
        if (esqueleto_quatro.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 4):
            esqueleto_quatro.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto4', lista_inimigos, enemy_list, 8)
            #Se o esqueleto4 colidir em algo do mapa
            if (collision_mapa(esqueleto_quatro, mapas) == True):
                esqueleto_quatro.setpos(pos_esqueleto_quatro)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
        
        #Checa se o esqueleto5 pode continuar
        if (esqueleto_cinco.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 5):
            esqueleto_cinco.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto5', lista_inimigos, enemy_list, 8)
            #Se o esqueleto5 colidir em algo do mapa
            if (collision_mapa(esqueleto_cinco, mapas) == True):
                esqueleto_cinco.setpos(pos_esqueleto_cinco)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

        #Checa se o esqueleto6 pode continuar
        if (esqueleto_seis.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 6):
            esqueleto_seis.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto6', lista_inimigos, enemy_list, 8)
            #Se o esqueleto6 colidir em algo do mapa
            if (collision_mapa(esqueleto_seis, mapas) == True):
                esqueleto_seis.setpos(pos_esqueleto_seis)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

        #Checa se o esqueleto7 pode continuar
        if (esqueleto_sete.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 7):
            esqueleto_sete.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto7', lista_inimigos, enemy_list, 8)
            #Se o esqueleto7 colidir em algo do mapa
            if (collision_mapa(esqueleto_sete, mapas) == True):
                esqueleto_sete.setpos(pos_esqueleto_sete)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

        #Checa se o esqueleto8 pode continuar
        if (esqueleto_oito.ontimer_continuar == True and mapas.inimigos_quantidade['esqueleto'] >= 8):
            esqueleto_oito.showturtle()
            enemy_persegue(janela, pos_player, 'esqueleto8', lista_inimigos, enemy_list, 8)
            #Se o esqueleto8 colidir em algo do mapa
            if (collision_mapa(esqueleto_oito, mapas) == True):
                esqueleto_oito.setpos(pos_esqueleto_oito)
            #Caso a personagem morrer
            if (collision_enemy(lista_inimigos, nessa)):
                game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)
                
    #Chama novamente a funcao
    janela.ontimer(chamando_esqueleto, 100)
#Chama o boss final para o mapa
def chamando_boss_final():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos()

    #Se caso o atributo que permite os boss_final continuarem a se mover for true o laco comeca
    if (boss_final.ontimer_continuar == True and mapas.inimigos_quantidade['boss_final'] >= 1):
        boss_final.showturtle()
        boss_final_acao(janela, pos_player, boss_final, 5)
        #Caso a personagem morrer
        if (collision_enemy(lista_inimigos, nessa)):
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Chama novamente a funcao
    janela.ontimer(chamando_boss_final, 100)
#Chama o bola final para o mapa
def chamando_bola_final():
    #Criando algumas variaveis para guarda as posicoes dos objetos
    pos_player = nessa.pos()

    #Se caso o atributo que permite os bola_final1 continuarem a se mover for true o laco comeca
    if (bola_final_um.ontimer_continuar == True and mapas.inimigos_quantidade['bola_final'] >= 1):
        bola_final_um.showturtle()
        bola_final_acao(janela, pos_player, bola_final_um, (-821, -333))
        #Caso a personagem morrer
        if (collision_enemy_projectiles(bola_final_um, nessa) == True):
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Se caso o atributo que permite os bola_final2 continuarem a se mover for true o laco comeca
    if (bola_final_dois.ontimer_continuar == True and mapas.inimigos_quantidade['bola_final'] >= 2):
        bola_final_dois.showturtle()
        bola_final_acao(janela, pos_player, bola_final_dois, (-817, 222))
        #Caso a personagem morrer
        if (collision_enemy_projectiles(bola_final_dois, nessa) == True):
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Se caso o atributo que permite os bola_final3 continuarem a se mover for true o laco comeca
    if (bola_final_tres.ontimer_continuar == True and mapas.inimigos_quantidade['bola_final'] >= 3):
        bola_final_tres.showturtle()
        bola_final_acao(janela, pos_player, bola_final_tres, (821, 221))
        #Caso a personagem morrer
        if (collision_enemy_projectiles(bola_final_tres, nessa) == True):
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Se caso o atributo que permite os bola_final4 continuarem a se mover for true o laco comeca
    if (bola_final_quatro.ontimer_continuar == True and mapas.inimigos_quantidade['bola_final'] >= 4):
        bola_final_quatro.showturtle()
        bola_final_acao(janela, pos_player, bola_final_quatro, (823, -329))
        #Caso a personagem morrer
        if (collision_enemy_projectiles(bola_final_quatro, nessa) == True):
            game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    #Chama novamente a funcao
    janela.ontimer(chamando_bola_final, 100)

#Animacao do background - na lista adicione as informacoes: 1, quantidade de frames, diretorio, milissegundos
def animation_background():
    if (mapas.ontimer_continuar == True):
        if (mapas.animacao_fundo[0] < mapas.animacao_fundo[1]+1):
            janela.bgpic(f'{mapas.animacao_fundo[2]}{mapas.animacao_fundo[0]}.gif')
            mapas.animacao_fundo[0] += 1
        else:
            mapas.animacao_fundo[0] = 1
        janela.ontimer(animation_background, mapas.animacao_fundo[3])


#Objetos
#Criando um objeto com elementos relacionados ao mapa do jogo
class mapas():
    #Variaveis
    animacao_fundo = []
    ontimer_continuar = True
    mapa_atual = 1
    mapa1_reiniciado = False
    mapa2_reiniciado = False
    mapa3_reiniciado = False
    monstros_fase = 6
    inimigos_quantidade = {}
    final = False

    #Funcoes
    #Chamada quando pega a chave/entra no portal/elimina todos os inimigos do mapa 3
    def key():
        if (mapas.mapa_atual == 1):
            nessa.chave.pegou = 2
            nessa.chave.hideturtle()
            mapas.animacao_fundo = [1, 4, './maps/map1/aberto/mapa', 100]

        elif (mapas.mapa_atual == 2):
            nessa.chave.pegou = 2
            nessa.chave.hideturtle()
            mapas.mapa_tres()

        elif (mapas.mapa_atual == 3):
            mapas.fim()

    def mapa_um():
        #Lista para selecionar quantos inimigos serao utilizados
        mapas.inimigos_quantidade = {'slime': 2, 'morcego': 2, 'slime_grande': 2}

        #Chamando os inimigos do mapa
        #Slimes
        lista_inimigos['slime1'].setpos(-150, 115); lista_inimigos['slime2'].setpos(202, -285)
        #Morcegos
        lista_inimigos['morcego1'].setpos(422, -290); lista_inimigos['morcego2'].setpos(-50, 200)
        #Slimes grande
        lista_inimigos['slime_grande1'].setpos(-594, -257); lista_inimigos['slime_grande2'].setpos(643, -271)

        #Posicao da chave no mapa um
        nessa.chave.setpos(665, 156)

        #Funcoes dos inimigos
        if (mapas.mapa1_reiniciado == False):
            chamando_slime(); chamando_morcego(); chamando_slime_grande()

        teclas_on(janela)
        #Animacao background
        #Posicao dos elementos na lista: 0 = 1, 1 = quantidade de frames, 2 = diretorio, 3 = milissegundos
        mapas.animacao_fundo = [1, 4, './maps/map1/fechado/mapa', 100]; animation_background()

    def mapa_dois():
        mapas.animacao_fundo = [1, 1, './maps/map2/mapa', 100]
        nessa.shape('./move/right/mapa2/right1.gif')
        nessa.chave.pegou = 0
        nessa.chave.setpos(12, -14)
        nessa.chave.shape('./objects/portal1.gif')
        mapas.mapa_atual = 2
        mapas.monstros_fase = 5
        nessa.setpos(283, -347)
        for i in enemy_name:
            lista_inimigos[i].hideturtle()

        mapas.inimigos_quantidade = {'estatua': 1, 'demonio': 4}
        lista_inimigos['estatua'].setpos(11, 66); lista_inimigos['estatua'].shape('./enemy/estatua/estatua_left1.gif')
        lista_inimigos['demonio1'].setpos(-479, -264); lista_inimigos['demonio2'].setpos(-651, -50); lista_inimigos['demonio3'].setpos(611, 136); lista_inimigos['demonio4'].setpos(240, 313)
        if (mapas.mapa2_reiniciado == False):
            chamando_estatua(); chamando_demonio()

    def mapa_tres():
        mapas.animacao_fundo = [1, 1, './maps/map3/mapa', 100]
        nessa.shape('./move/right/mapa3/right1.gif')
        nessa.setpos(12, -14)
        nessa.chave.pegou = 0
        mapas.mapa_atual = 3
        mapas.monstros_fase = 9
        for i in enemy_name:
            lista_inimigos[i].hideturtle()

        mapas.inimigos_quantidade = {'esqueleto': 8, 'boss_final': 1, 'bola_final': 4}
        lista_inimigos['boss_final'].setpos(0, 301); lista_inimigos['boss_final'].shape('./enemy/boss_final/boss_final_left1.gif')
        lista_inimigos['esqueleto1'].setpos(-601, 307); lista_inimigos['esqueleto2'].setpos(-622, -303); lista_inimigos['esqueleto3'].setpos(612, 315); lista_inimigos['esqueleto4'].setpos(599, -314); lista_inimigos['esqueleto5'].setpos(-536, 109); lista_inimigos['esqueleto6'].setpos(-527, -118); lista_inimigos['esqueleto7'].setpos(350, 121); lista_inimigos['esqueleto8'].setpos(359, -82)
        if (mapas.mapa3_reiniciado == False):
            chamando_esqueleto(); chamando_boss_final(); chamando_bola_final()

    def fim():
        for i in enemy_name:
            lista_inimigos[i].hideturtle()
        for i in range(4):
            lista_inimigos[f'bola_final{i+1}'].ontimer_continuar = False
            lista_inimigos[f'bola_final{i+1}'].hideturtle()

        nessa.setpos(1, -37)
        nessa.shape('./move/right/fim/right1.gif')
        mapas.animacao_fundo = [1, 1, './maps/fim/fim', 100]
        mapas.mapa_atual = 4

        janela.update()

    #Escolhas
    def poder():
        mapas.ontimer_continuar = False
        nessa.hideturtle()
        janela.bgpic('./history/finais/ruim/ruim1.gif')
        janela.update()

        sleep(10)
        mapas.final = True
        game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    def riquezas():
        mapas.ontimer_continuar = False
        nessa.hideturtle()
        janela.bgpic('./history/finais/neutro/neutro1.gif')
        janela.update()

        sleep(10)
        mapas.final = True
        game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

    def liberdade():
        mapas.ontimer_continuar = False
        nessa.hideturtle()
        janela.bgpic('./history/finais/bom/bom1.gif')
        janela.update()

        sleep(10)
        mapas.final = True
        game_over(janela, nessa, lista_inimigos, enemy_name, teclas_off, mapas)

#Main

#Cria uma lista para ser possivel resetar a animacao da direção do player
gif_walk_default_number = [1, 1, 1, 1] #Elemento 0 = up, 1 = down, 2 = right, 3 = left

#Cria a screen definindo algumas configuracoes como background, dimenssoes da tela e nome do programa
janela = init_screen(1920, 1080, './maps/map1/fechado/mapa1.gif', 'A torre do desejo')
#Tirando a atualizacao dos frames
janela.tracer(0)

#Habilita eventos na janela
janela.listen()


#Tela inicial do jogo
if (inicio(janela, None, None, None, mapas) == True):
    janela.update()


#Adiciona os shapes para usar no turtle

#Adiciona os frames da movimentacao do player + objeto (flecha) + chave
frames_nessa = [['./move/up/mapa1/up', 4], ['./move/down/mapa1/down', 4], ['./move/right/mapa1/right', 6], ['./move/left/mapa1/left', 6],
['./move/up/mapa2/up', 4], ['./move/down/mapa2/down', 4], ['./move/right/mapa2/right', 6], ['./move/left/mapa2/left', 6],
['./move/up/mapa3/up', 4], ['./move/down/mapa3/down', 4], ['./move/right/mapa3/right', 6], ['./move/left/mapa3/left', 6],
['./move/up/fim/up', 4], ['./move/down/fim/down', 4], ['./move/right/fim/right', 6], ['./move/left/fim/left', 6],
['./projectiles/arrow/arrow', 8], ['./objects/chave', 1]]
for i in range(len(frames_nessa)):
    add_shapes(janela, frames_nessa[i])

#Adiciona os frames dos inimigos
#Animacao da esquerda
for i in enemy_name:
    info = [f'{enemy_list[i]["diretorio"]}_left', enemy_list[i]['frames']]
    add_shapes(janela, info)
#Animacao da direita
for i in enemy_name:
    info = [f'{enemy_list[i]["diretorio"]}_right', enemy_list[i]['frames']]
    add_shapes(janela, info)

#Adiciona um sprite tranparente
add_shapes(janela, ['./enemy/sprite_transparente/sprite', 1])

#Adiciona os numeros para o dano do jogo
add_shapes(janela, ['./objects/numeros/numero', 9])

#Adiciona a bola de fogo
add_shapes(janela, ['./projectiles/bola_de_fogo/bola_de_fogo', 4])

#Adiciona o portal
add_shapes(janela, ['./objects/portal', 1])

#Adiciona a bola final
add_shapes(janela, ['./projectiles/bola_final/bola_final', 1])


#Criacao do player + objeto (flecha)

#Player
nessa = add_objects('./move/right/mapa1/right1.gif', 0, False, -810, 277) #Cria a nessa (personagem principal do jogo)
nessa.player = True; nessa.voador = False #Cria alguns atributos

#Flecha
nessa.arrow = add_objects('./projectiles/arrow/arrow1.gif', 1, True, -810, 277) #Cria a flecha
nessa.arrow.player = False; nessa.arrow.ataque = True; nessa.arrow.voador = False; nessa.arrow.distancia = 0 #Cria alguns atributos

#Chave
nessa.chave = add_objects('./objects/chave1.gif', 0, True, 665, 156) #Cria a chave
nessa.chave.pegou = 0 #Cria alguns atributos

#Numeros para o dano
nessa.numeros_dano = add_objects('./objects/numeros/numero1.gif', 0, True, 0, 0) #Cria numeros para usar no dano

#Lista de todos os objetos criados
lista_objetos = {'player': nessa, 'flecha': nessa.arrow, 'chave': nessa.chave, 'numeros': nessa.numeros_dano}


#Criacao de todos os inimigos

#Slimes
#Criando o slime1
slime = add_objects(f'{enemy_list["slime1"]["diretorio"]}_left1.gif', 0, True, -150, 115) #Adiciona um objeto no turtle
slime.frame = 1; slime.vida = enemy_list['slime1']['vida']; slime.tamanho = [26, 26, 21, 21]; slime.ontimer_continuar = True; slime.voador = False #Cria alguns atributos
#Criando o slime2
slime_dois = slime.clone(); slime_dois.setpos(202, -285) #Clona um objeto
slime_dois.frame = 1; slime_dois.vida = enemy_list['slime2']['vida']; slime_dois.tamanho = [26, 26, 21, 21]; slime_dois.ontimer_continuar = True; slime_dois.voador = False #Cria alguns atributos

#Morcegos
#Criando o morcego1
morcego = add_objects(f'{enemy_list["morcego1"]["diretorio"]}_left1.gif', 0, True, 422, -290) #Adiciona um objeto no turtle
morcego.frame = 1; morcego.vida = enemy_list['morcego1']['vida']; morcego.tamanho = [29, 29, 18, 18]; morcego.ontimer_continuar = True; morcego.voador = True #Cria alguns atributos
#Criando o morcego2
morcego_dois = morcego.clone(); morcego_dois.setpos(-50, 200) #Clona um objeto
morcego_dois.frame = 1; morcego_dois.vida = enemy_list['morcego2']['vida']; morcego_dois.tamanho = [29, 29, 18, 18]; morcego_dois.ontimer_continuar = True; morcego_dois.voador = True #Cria alguns atributos

#Slimes grande
#Criando o slime_grande1
slime_grande = add_objects(f'{enemy_list["slime_grande1"]["diretorio"]}_left1.gif', 0, True, -594, -257) #Adiciona um objeto no turtle
slime_grande.frame = 1; slime_grande.vida = enemy_list['slime_grande1']['vida']; slime_grande.tamanho = [86, 86, 68, 68]; slime_grande.ontimer_continuar = True; slime_grande.voador = False #Cria alguns atributos
#Criando o slime_grande2
slime_grande_dois = slime_grande.clone(); slime_grande_dois.setpos(643, -271) #Clona um objeto
slime_grande_dois.frame = 1; slime_grande_dois.vida = enemy_list['slime_grande2']['vida']; slime_grande_dois.tamanho = [86, 86, 68, 68]; slime_grande_dois.ontimer_continuar = True; slime_grande_dois.voador = False #Cria alguns atributos

#Estatua
#Criando a estatua
estatua = add_objects(f'{enemy_list["estatua"]["diretorio"]}_left1.gif', 0, True, 0, 1000) #Adiciona um objeto no turtle
estatua.frame = 1; estatua.vida = enemy_list['estatua']['vida']; estatua.tamanho = [143, 143, 103, 0]; estatua.ontimer_continuar = True; estatua.tempo_animacao = 0; estatua.voador = False #Cria alguns atributos
#Criando a bola de fogo da estatua
estatua.bola_de_fogo = add_objects('./projectiles/bola_de_fogo/bola_de_fogo4.gif', 1, True, 0, 0) #Cria a flecha
estatua.bola_de_fogo; estatua.bola_de_fogo.tamanho = [25, 25, 94, 94]; estatua.bola_de_fogo.voador = False #Cria alguns atributos

#Demonios
#Criando o demonio1
demonio_um = add_objects(f'{enemy_list["demonio1"]["diretorio"]}_left1.gif', 0, True, 0, 1000) #Adiciona um objeto no turtle
demonio_um.frame = 1; demonio_um.vida = enemy_list['demonio1']['vida']; demonio_um.tamanho = [86, 86, 68, 68]; demonio_um.ontimer_continuar = True; demonio_um.voador = False #Cria alguns atributos
#Criando o demonio2
demonio_dois = demonio_um.clone(); demonio_dois.setpos(0, 1000) #Clona um objeto
demonio_dois.frame = 1; demonio_dois.vida = enemy_list['demonio2']['vida']; demonio_dois.tamanho = [86, 86, 68, 68]; demonio_dois.ontimer_continuar = True; demonio_dois.voador = False #Cria alguns atributos
#Criando o demonio3
demonio_tres = demonio_um.clone(); demonio_tres.setpos(0, 1000) #Clona um objeto
demonio_tres.frame = 1; demonio_tres.vida = enemy_list['demonio3']['vida']; demonio_tres.tamanho = [86, 86, 68, 68]; demonio_tres.ontimer_continuar = True; demonio_tres.voador = False #Cria alguns atributos
#Criando o demonio4
demonio_quatro = demonio_um.clone(); demonio_quatro.setpos(0, 1000) #Clona um objeto
demonio_quatro.frame = 1; demonio_quatro.vida = enemy_list['demonio4']['vida']; demonio_quatro.tamanho = [86, 86, 68, 68]; demonio_quatro.ontimer_continuar = True; demonio_quatro.voador = False #Cria alguns atributos

#Esqueletos
#Criando o esqueleto1
esqueleto_um = add_objects(f'{enemy_list["esqueleto1"]["diretorio"]}_left1.gif', 0, True, 0, 1000) #Adiciona um objeto no turtle
esqueleto_um.player = False; esqueleto_um.frame = 1; esqueleto_um.vida = enemy_list['demonio1']['vida']; esqueleto_um.tamanho = [20, 20, 29, 29]; esqueleto_um.ontimer_continuar = True; esqueleto_um.voador = False #Cria alguns atributos
#Criando o esqueleto2
esqueleto_dois = esqueleto_um.clone(); esqueleto_dois.setpos(0, 1000) #Clona um objeto
esqueleto_dois.player = False; esqueleto_dois.frame = 1; esqueleto_dois.vida = enemy_list['esqueleto2']['vida']; esqueleto_dois.tamanho = [20, 20, 29, 29]; esqueleto_dois.ontimer_continuar = True; esqueleto_dois.voador = False #Cria alguns atributos
#Criando o esqueleto3
esqueleto_tres = esqueleto_um.clone(); esqueleto_tres.setpos(0, 1000) #Clona um objeto
esqueleto_tres.player = False; esqueleto_tres.frame = 1; esqueleto_tres.vida = enemy_list['esqueleto3']['vida']; esqueleto_tres.tamanho = [20, 20, 29, 29]; esqueleto_tres.ontimer_continuar = True; esqueleto_tres.voador = False #Cria alguns atributos
#Criando o esqueleto4
esqueleto_quatro = esqueleto_um.clone(); esqueleto_quatro.setpos(0, 1000) #Clona um objeto
esqueleto_quatro.player = False; esqueleto_quatro.frame = 1; esqueleto_quatro.vida = enemy_list['esqueleto4']['vida']; esqueleto_quatro.tamanho = [20, 20, 29, 29]; esqueleto_quatro.ontimer_continuar = True; esqueleto_quatro.voador = False #Cria alguns atributos
#Criando o esqueleto5
esqueleto_cinco = esqueleto_um.clone(); esqueleto_cinco.setpos(0, 1000) #Clona um objeto
esqueleto_cinco.player = False; esqueleto_cinco.frame = 1; esqueleto_cinco.vida = enemy_list['esqueleto5']['vida']; esqueleto_cinco.tamanho = [20, 20, 29, 29]; esqueleto_cinco.ontimer_continuar = True; esqueleto_cinco.voador = False #Cria alguns atributos
#Criando o esqueleto6
esqueleto_seis = esqueleto_um.clone(); esqueleto_seis.setpos(0, 1000) #Clona um objeto
esqueleto_seis.player = False; esqueleto_seis.frame = 1; esqueleto_seis.vida = enemy_list['esqueleto6']['vida']; esqueleto_seis.tamanho = [20, 20, 29, 29]; esqueleto_seis.ontimer_continuar = True; esqueleto_seis.voador = False #Cria alguns atributos
#Criando o esqueleto7
esqueleto_sete = esqueleto_um.clone(); esqueleto_sete.setpos(0, 1000) #Clona um objeto
esqueleto_sete.player = False; esqueleto_sete.frame = 1; esqueleto_sete.vida = enemy_list['esqueleto7']['vida']; esqueleto_sete.tamanho = [20, 20, 29, 29]; esqueleto_sete.ontimer_continuar = True; esqueleto_sete.voador = False #Cria alguns atributos
#Criando o esqueleto8
esqueleto_oito = esqueleto_um.clone(); esqueleto_oito.setpos(0, 1000) #Clona um objeto
esqueleto_oito.player = False; esqueleto_oito.frame = 1; esqueleto_oito.vida = enemy_list['esqueleto8']['vida']; esqueleto_oito.tamanho = [20, 20, 29, 29]; esqueleto_oito.ontimer_continuar = True; esqueleto_oito.voador = False #Cria alguns atributos

#Boss final
boss_final = add_objects(f'{enemy_list["boss_final"]["diretorio"]}_left1.gif', 0, True, 0, 1000) #Adiciona um objeto no turtle
boss_final.tempo_animacao = 0; boss_final.player = False; boss_final.frame = 1; boss_final.vida = enemy_list['boss_final']['vida']; boss_final.tamanho = [103, 103, 158, 158]; boss_final.ontimer_continuar = True; boss_final.voador = True #Cria alguns atributos

#Bola final
#Criando a bola_final1
bola_final_um = add_objects('./projectiles/bola_final/bola_final1.gif', 0, True, 0, 1000) #Adiciona um objeto no turtle
bola_final_um.tempo_animacao = 0; bola_final_um.player = False; bola_final_um.frame = 1; bola_final_um.tamanho = [20, 20, 20, 20]; bola_final_um.ontimer_continuar = True; bola_final_um.voador = True #Cria alguns atributos
#Criando a bola_final2
bola_final_dois = bola_final_um.clone(); bola_final_dois.setpos(0, 1000) #Clona um objeto
bola_final_dois.tempo_animacao = 0; bola_final_dois.player = False; bola_final_dois.frame = 1; bola_final_dois.tamanho = [20, 20, 20, 20]; bola_final_dois.ontimer_continuar = True; bola_final_dois.voador = True #Cria alguns atributos
#Criando a bola_final3
bola_final_tres = bola_final_um.clone(); bola_final_tres.setpos(0, 1000) #Clona um objeto
bola_final_tres.tempo_animacao = 0; bola_final_tres.player = False; bola_final_tres.frame = 1; bola_final_tres.tamanho = [20, 20, 20, 20]; bola_final_tres.ontimer_continuar = True; bola_final_tres.voador = True #Cria alguns atributos
#Criando a bola_final4
bola_final_quatro = bola_final_um.clone(); bola_final_quatro.setpos(0, 1000) #Clona um objeto
bola_final_quatro.tempo_animacao = 0; bola_final_quatro.player = False; bola_final_quatro.tamanho = [20, 20, 20, 20]; bola_final_quatro.ontimer_continuar = True; bola_final_quatro.voador = True #Cria alguns atributos

#Lista de todos os inimigos criados
lista_inimigos = {'slime1': slime, 'slime2': slime_dois,
'morcego1': morcego, 'morcego2': morcego_dois,
'slime_grande1': slime_grande, 'slime_grande2': slime_grande_dois,
'estatua': estatua,
'demonio1': demonio_um, 'demonio2': demonio_dois, 'demonio3': demonio_tres, 'demonio4': demonio_quatro,
'esqueleto1': esqueleto_um, 'esqueleto2': esqueleto_dois, 'esqueleto3': esqueleto_tres, 'esqueleto4': esqueleto_quatro, 'esqueleto5': esqueleto_cinco, 'esqueleto6': esqueleto_seis, 'esqueleto7': esqueleto_sete, 'esqueleto8': esqueleto_oito,
'boss_final': boss_final,
'bola_final1': bola_final_um, 'bola_final2': bola_final_dois, 'bola_final3': bola_final_tres, 'bola_final4': bola_final_quatro}


#Iniciando o mapa um
mapas.mapa_um()

#Ativa todos os eventos de clique e teclado
teclas_on(janela)
#Loop - para manter a tela aberta
janela.mainloop()