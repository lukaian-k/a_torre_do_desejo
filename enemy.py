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
'demonio4': {'diretorio': './enemy/demonio/demonio', 'frames': 6, 'vida': 1}}

#Lista inimigos - uma lista que contem apenas as chaves do dicionario enemy_list
enemy_name = list(enemy_list.keys())


#Funcoes

#Acao de cada inimigo - o que cada inimigo ira fazer
#Slime - Morcego - Slime grande
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

def acao_estatua(screen, enemy, player, collision_enemy_projectiles):
    if (enemy.frame == 5):
        enemy.frame = 1

    enemy.bola_de_fogo.showturtle()
    if (enemy.tempo_animacao >= 50):
        enemy.tempo_animacao = 0
        enemy.bola_de_fogo.hideturtle()
        enemy.bola_de_fogo.setpos(12, -14)
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