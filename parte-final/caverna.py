# Importação da blbioteca
import random

# Título do jogo
TITLE = 'Voando na Caverna'
# Largura da janela
WIDTH = 800
# Altura da janela
HEIGHT = 679

# Esta função executa em torno de 60 vezes por segundo
def update():
    morcego.speed += gravidade
    morcego.y += morcego.speed
    estalactite1.x -= velocidade_tela
    estalagmite1.x -= velocidade_tela
    # Condição para verificar se a estalactite atingiu uma posição negativa no eixo x
    if (estalactite1.right) < 0:
        offset = random.randint(-80, 80)
        print('offset: ' + str(offset))
        estalactite1.midleft = (WIDTH, offset)
        estalagmite1.midleft = (WIDTH, offset + estalactite1.height + espaco)
        estalactite1.number += 1
    # Condição para verificar se o morcego atingiu o topo ou o chão da caverna
    if (morcego.y > HEIGHT):
        reset()
    # Condição que verifica a colisão nos obstáculos
    if (morcego.colliderect(estalactite1)) or (morcego.colliderect(estalagmite1)) or (morcego.y <= 0):
        colisao()
    # Condição que verifica se o morcego está vivo, caso positivo o sistema verifica uma
    # segunda condição, se a velocidade for maior que zero muda para a imagem 1, senão usa a imagem 2
    if (morcego.alive):
        if (morcego.speed > 0):
            morcego.image = 'morcego1'
        else:
            morcego.image = 'morcego2'
    # Condição para atualizar os pontos
    if (estalactite1.right < morcego.left):
        morcego.score = estalactite1.number

# Desenha os objetos na tela
def draw():
    screen.blit('caverna', (0, 0))
    morcego.draw()
    estalactite1.draw()
    estalagmite1.draw()
    # Desenha o quadro de pontos do jogador atual
    screen.draw.text(
        str(morcego.score),
        color = 'yellow',
        midtop = (WIDTH/2, 15),
        fontsize = 55
        )

# Executa sempre que o botão do mouse é pressionado
def on_mouse_down():
    if (morcego.alive):
        morcego.speed = -6.5

# Função para reiniciar o jogo
def reset():
    morcego.speed = 1
    morcego.center = (75, 350)
    estalactite1.center = (450, 0)
    estalagmite1.center = (450, estalactite1.height + espaco)
    morcego.alive = True
    morcego.image = 'morcego1'
    morcego.score = 0
    estalactite1.number = 1

# Função para executar os comandos depois da colisão
def colisao():
    morcego.image = "morcego-fantasma"
    morcego.alive = False

# Cria o personagem morcego do jogo
morcego = Actor('morcego1')

# Adicionando os obstáculos
espaco = 180
estalactite1 = Actor('estalactite1')
estalagmite1 = Actor('estalagmite1')

velocidade_tela = 1
gravidade = 0.3

reset()