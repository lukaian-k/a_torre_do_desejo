#Lista de todos os os inimigos do jogo - aqui encontra-se duas informacoes, o diretorio dos .gif e quantos .gif tem cada um dos inimigos
enemy_list = {'slime1': {'diretorio': './enemy/slime/slime', 'frames': 5, 'vida': 1},
'slime2': {'diretorio': './enemy/slime/slime', 'frames': 5, 'vida': 1},
'morcego1': {'diretorio': './enemy/morcego/morcego', 'frames': 8, 'vida': 1},
'morcego2': {'diretorio': './enemy/morcego/morcego', 'frames': 8, 'vida': 1},
'slime_grande1': {'diretorio': './enemy/slime_grande/slime_grande', 'frames': 4, 'vida': 1},
'slime_grande2': {'diretorio': './enemy/slime_grande/slime_grande', 'frames': 4, 'vida': 1},
'estatua': {'diretorio': './enemy/estatua/estatua', 'frames': 1, 'vida': 1},
'demonio1': {'diretorio': './enemy/demonio/demonio', 'frames': 6, 'vida': 1},
'demonio2': {'diretorio': './enemy/demonio/demonio', 'frames': 6, 'vida': 1},
'demonio3': {'diretorio': './enemy/demonio/demonio', 'frames': 6, 'vida': 1},
'demonio4': {'diretorio': './enemy/demonio/demonio', 'frames': 6, 'vida': 1},
'esqueleto1': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto2': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto3': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto4': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto5': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto6': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto7': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'esqueleto8': {'diretorio': './enemy/esqueleto/esqueleto', 'frames': 6, 'vida': 1},
'boss_final': {'diretorio': './enemy/boss_final/boss_final', 'frames': 5, 'vida': 1}}

#Lista inimigos - uma lista que contem apenas as chaves do dicionario enemy_list
enemy_name = list(enemy_list.keys())


#Funcoes

#Acao de cada inimigo - o que cada inimigo ira fazer
#Slime - Morcego - Slime grande - Demonio - Esqueleto
def enemy_persegue(screen, pos_player, name, enemy, all_frames, forward):
    if (enemy[name].frame < all_frames[name]['frames']+1):
        angulo = enemy[name].towards(pos_player); enemy[name].setheading(angulo); enemy[name].forward(forward)
        if (0 <= angulo <= 90 or 270 <= angulo <= 360):
            enemy[name].shape(f'{enemy_list[name]["diretorio"]}_right{enemy[name].frame}.gif')
        else:
            enemy[name].shape(f'{enemy_list[name]["diretorio"]}_left{enemy[name].frame}.gif')
        screen.update(); enemy[name].frame += 1
    else:
        enemy[name].frame = 1

def acao_estatua(screen, enemy, player, collision_enemy_projectiles, all_frames):
    if (enemy.tempo_animacao == 0):
        enemy.bola_de_fogo.setpos(12, -14)

    if (enemy.frame == all_frames+1):
        enemy.frame = 1

    enemy.bola_de_fogo.showturtle()
    if (enemy.tempo_animacao >= 50):
        enemy.tempo_animacao = 0
        enemy.bola_de_fogo.hideturtle()
        enemy.bola_de_fogo.shape(f'./projectiles/bola_de_fogo/bola_de_fogo{enemy.frame}.gif')
        enemy.bola_de_fogo.right(90)
        enemy.frame += 1
    else:
        enemy.bola_de_fogo.forward(15)
        enemy.tempo_animacao += 1

    if (enemy.frame == 1 or enemy.frame == 3):
        enemy.bola_de_fogo.tamanho = [25, 25, 94, 94]
    else:
        enemy.bola_de_fogo.tamanho = [94, 94, 25, 25]
    
    #Caso a personagem morrer
    if (collision_enemy_projectiles(enemy.bola_de_fogo, player) == True):
        enemy.bola_de_fogo.hideturtle()
        return True
    screen.update()

#Boss final - acao
def boss_final_acao(screen, pos_player, enemy, all_frames):
    if (enemy.tempo_animacao == 0):
        enemy.setheading(enemy.towards(pos_player))

    if (enemy.frame == all_frames+1):
        enemy.frame = 1

    if (enemy.tempo_animacao >= 50):
        enemy.tempo_animacao = 0
        enemy.shape(f'./enemy/boss_final/boss_final_left{enemy.frame}.gif')
        enemy.frame += 1
    else:
        enemy.forward(10)
        enemy.tempo_animacao += 1
    
    screen.update()

#Bola final - acao
def bola_final_acao(screen, pos_player, enemy, coor):
    if (enemy.tempo_animacao == 0):
        enemy.setpos(coor)
        enemy.setheading(enemy.towards(pos_player))
    enemy.tempo_animacao += 1

    if (enemy.tempo_animacao >= 130):
        enemy.tempo_animacao = 0
    elif (enemy.tempo_animacao >= 70):
        enemy.backward(15)
    else:
        enemy.forward(15)
    
    screen.update()