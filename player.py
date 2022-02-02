#Imports
import turtle; from collision import *


#Funções

#Movimentação do player - funcao principal do movimento do player, muda a direcao e sprite de acordo com a direcao que foi aperta
def walk_main(screen, lista_objetos, direcao, distancia, frame, all_frames, diretorio, eventos_on, eventos_off):
    screen.update(); eventos_off('wsda', screen)
    posicao = lista_objetos['player'].pos()
    lista_objetos['player'].setheading(direcao); lista_objetos['player'].forward(distancia)

    if (frame < all_frames+1):
        lista_objetos['player'].shape(f'{diretorio}{frame}.gif')
        frame += 1
    else:
        frame = 1

    if (collision_map1(lista_objetos['player']) == True):
        lista_objetos['player'].setpos(posicao)
    eventos_on(screen)
    return frame
#Reseta os frames da animacao da direcao do player - é uma dependencia da funcao da funcao da movimentacao. ela armazena qual tecla foi apertada por ultimo para que continue a animacao em sequencia na ordem certa de cada direcao
def reset_frame_walk(frame_up, frame_down, frame_right, frame_left):
    return [frame_up, frame_down, frame_right, frame_left]

#Tiro do arco - faz com que a flecha mude de sprite e direcao, cria a movimentacao do tiro e checa se colidio com alguma coisa
def atack_bow(x, y, screen, lista_objetos, lista_inimigos, eventos_on, eventos_off, time_shot):
    #print(x, y)
    if (lista_objetos['flecha'].ataque == True):
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
        for i in range(33):
            screen.update()
            for z in range(10):
                lista_objetos['flecha'].forward(1)
                screen.update()
            if (collision_map1(lista_objetos['flecha']) == True):
                break
            inimigo_colisao = collision_enemy(lista_inimigos, lista_objetos['flecha'])
            if (inimigo_colisao != None):
                inimigo_colisao.vida -= 1
                if (inimigo_colisao.vida > 0):
                    break
                else:
                    inimigo_colisao.hideturtle()
                    inimigo_colisao.setpos(-2000, -2000)
                    inimigo_colisao.ontimer_continuar = False
                    break
        lista_objetos['flecha'].hideturtle(); screen.update(); eventos_on(screen)
        lista_objetos['flecha'].ataque = False; screen.ontimer(time_shot, 700)