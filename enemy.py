#Lista de todos os os inimigos do jogo - aqui encontra-se duas informacoes, o diretorio dos .gif e quantos .gif tem cada um dos inimigos
enemy_list = {'slime1': {'diretorio': './enemy/slime/slime', 'frames': 5},
'slime2': {'diretorio': './enemy/slime/slime', 'frames': 5},
'slime3': {'diretorio': './enemy/slime/slime', 'frames': 5},
'morcego1': {'diretorio': './enemy/morcego/morcego', 'frames': 8},
'morcego2': {'diretorio': './enemy/morcego/morcego', 'frames': 8}}

#Lista inimigos - uma lista que contem apenas as chaves do dicionario enemy_list
enemy_name = list(enemy_list.keys())


#Funcoes

#Acao de cada inimigo - o que cada inimigo ira fazer
#Slime
def enemy_slime(screen, pos_player, enemy, all_frames, numero):
    for i in range(all_frames):
        if (enemy.frame < all_frames+1):
            angulo = enemy.towards(pos_player); enemy.setheading(angulo); enemy.forward(5)
            enemy.shape(f'{enemy_list[f"slime{numero}"]["diretorio"]}{enemy.frame}.gif')
            screen.update(); enemy.frame += 1
            return
        else:
            enemy.frame = 1
            screen.update()
#Morcego
def enemy_morcego(screen, pos_player, enemy, all_frames, numero):
    for i in range(all_frames):
        if (enemy.frame < all_frames+1):
            angulo = enemy.towards(pos_player); enemy.setheading(angulo); enemy.forward(10)
            enemy.shape(f'{enemy_list[f"morcego{numero}"]["diretorio"]}{enemy.frame}.gif')
            screen.update(); enemy.frame += 1
            return
        else:
            enemy.frame = 1
            screen.update()