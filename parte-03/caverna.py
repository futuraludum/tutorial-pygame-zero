#Título do jogo
TITLE = 'Voando na Caverna'
#Largura da janela
WIDTH = 800
# Altura da janela
HEIGHT = 679

#Esta função executa em torno de 60 vezes por segundo
def update():
    morcego.y += morcego.speed
    estalactite1.x -= velocidade_tela
    estalagmite1.x -= velocidade_tela
    #Condição para verificar se a estalactite atingiu uma posição negativa no eixo x
    if (estalactite1.x) < 0:
        estalactite1.x = WIDTH
        estalagmite1.x = WIDTH

#Desenha os objetos na tela
def draw():
    screen.blit('caverna', (0, 0))
    morcego.draw()
    estalactite1.draw()
    estalagmite1.draw()

#Executa sempre que o botão do mouse é pressionado
def on_mouse_down():
    morcego.y -= 50

#Cria o personagem morcego do jogo
morcego = Actor('morcego1', (75, 350))

#Velocidade do morcego
morcego.speed = 1

#Adicionando os obstáculos
espaco = 180
estalactite1 = Actor('estalactite1', (450, 0))
estalagmite1 = Actor('estalagmite1', (450, estalactite1.height + espaco))

velocidade_tela = 1