#Imports de libs
import turtle
from time import sleep
#Imports de arquivos da propria pasta
from collision import *; from game_over import game_over; from enemy import enemy_name


#Funções

#Movimentação do player - funcao principal do movimento do player, muda a direcao e sprite de acordo com a direcao que foi aperta
def walk_main(screen, lista_objetos, lista_inimigos, direcao, distancia, frame, all_frames, diretorio, eventos_on, eventos_off, mapas):
    screen.update(); eventos_off('wsda', screen)
    posicao = lista_objetos['player'].pos()
    lista_objetos['player'].setheading(direcao); lista_objetos['player'].forward(distancia)

    if (frame < all_frames+1):
        lista_objetos['player'].shape(f'{diretorio}{frame}.gif')
        frame += 1
    else:
        frame = 1

    if (collision_mapa(lista_objetos['player'], mapas) == True):
        lista_objetos['player'].setpos(posicao)
    if (collision_mapa(lista_objetos['player'], mapas) == 'kill'):
        game_over(screen, lista_objetos['player'], lista_inimigos, enemy_name, eventos_off, mapas)

    if (lista_objetos['chave'].pegou == 1):
        mapas.key()
    screen.update()
    eventos_on(screen)
    return frame
#Reseta os frames da animacao da direcao do player - é uma dependencia da funcao da funcao da movimentacao. ela armazena qual tecla foi apertada por ultimo para que continue a animacao em sequencia na ordem certa de cada direcao
def reset_frame_walk(frame_up, frame_down, frame_right, frame_left):
    return [frame_up, frame_down, frame_right, frame_left]

#Tiro do arco - faz com que a flecha mude de sprite e direcao, cria a movimentacao do tiro e checa se colidio com alguma coisa
def atack_bow(x, y, screen, lista_objetos, lista_inimigos, eventos_on, eventos_off, time_shot, mapas):
    print(x, y)
    if (lista_objetos['flecha'].ataque == True and mapas.monstros_fase > 0):
        eventos_off('wsda', screen)
        lista_objetos['flecha'].setpos(lista_objetos['player'].pos())
        angulo_arrow = lista_objetos['flecha'].towards(x, y)
        lista_objetos['flecha'].setheading(angulo_arrow)

        #Troca o icone da flecha de acordo com a direcao da dela
        if (0 <= angulo_arrow <= 29 or 330 <= angulo_arrow <= 360): #Direita
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow1.gif')
        elif (30 <= angulo_arrow <= 59): #Vertical - superior direito
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow5.gif')
        elif (60 <= angulo_arrow <= 119): #Cima
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow3.gif')
        elif (120 <= angulo_arrow <= 149): #Vertical - superior esquerdo
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow6.gif')
        elif (150 <= angulo_arrow <= 209): #Esquerda
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow2.gif')
        elif (210 <= angulo_arrow <= 239): #Vertical - inferior esquerdo
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow8.gif')
        elif (240 <= angulo_arrow <= 299): #Baixo
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow4.gif')
        elif (300 <= angulo_arrow <= 329): #Vertical - inferior direito
            lista_objetos['flecha'].shape('./projectiles/arrow/arrow7.gif')
        
        lista_objetos['flecha'].showturtle()
        tiro(x, y, screen, lista_objetos, lista_inimigos, eventos_on, eventos_off, time_shot, mapas)

def tiro(x, y, screen, lista_objetos, lista_inimigos, eventos_on, eventos_off, time_shot, mapas):
    ocorreu_colisao = False
    screen.update()
    lista_objetos['flecha'].forward(10); screen.update()
    if (collision_mapa(lista_objetos['flecha'], mapas) == True):
        ocorreu_colisao = True
    inimigo_colisao = collision_enemy(lista_inimigos, lista_objetos['flecha'])
    if (inimigo_colisao != None):
        if (inimigo_colisao[1] == 'estatua' and mapas.monstros_fase > 1):
            pass
        else:
            inimigo_colisao[0].vida -= 1

        if (inimigo_colisao[0].vida > 0):
            if (inimigo_colisao[1] == 'slime_grande1' or inimigo_colisao[1] == 'slime_grande2'):
                lista_objetos['player'].numeros_dano.setpos(inimigo_colisao[0].xcor(), inimigo_colisao[0].ycor()+inimigo_colisao[0].tamanho[2]*1.3)
            elif (inimigo_colisao[1] == 'estatua'):
                lista_objetos['player'].numeros_dano.setpos(inimigo_colisao[0].xcor(), inimigo_colisao[0].ycor()+inimigo_colisao[0].tamanho[2]*1.7)
            else:
                lista_objetos['player'].numeros_dano.setpos(inimigo_colisao[0].xcor(), inimigo_colisao[0].ycor()+inimigo_colisao[0].tamanho[2]*2.5)
            lista_objetos['player'].numeros_dano.showturtle()
            lista_objetos['player'].numeros_dano.shape(f'./objects/numeros/numero{inimigo_colisao[0].vida}.gif')
            screen.update()
            sleep(0.2)
            lista_objetos['player'].numeros_dano.hideturtle()
            ocorreu_colisao = True
        else:
            inimigo_colisao[0].shape('./enemy/sprite_transparente/sprite1.gif')
            inimigo_colisao[0].ontimer_continuar = False
            mapas.monstros_fase -= 1
            if (mapas.monstros_fase <= 0 and mapas.mapa_atual != 3):
                lista_objetos['player'].chave.showturtle()
            elif (mapas.monstros_fase <= 0 and mapas.mapa_atual == 3):
                mapas.key()
            ocorreu_colisao = True
    if (ocorreu_colisao == True or lista_objetos['flecha'].distancia >= 33):
        lista_objetos['flecha'].hideturtle(); screen.update(); eventos_on(screen)
        lista_objetos['flecha'].ataque = False; screen.ontimer(time_shot, 1000)
        lista_objetos['flecha'].distancia = 0
    else:
        lista_objetos['flecha'].distancia += 1
        screen.update()
        tiro(x, y, screen, lista_objetos, lista_inimigos, eventos_on, eventos_off, time_shot, mapas)