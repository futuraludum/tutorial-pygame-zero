#Título do jogo
TITLE = 'Voando na Caverna'
#Largura da janela
WIDTH = 800
# Altura da janela
HEIGHT = 679

#Esta função executa em torno de 60 vezes por segundo
def update():
    morcego.y += morcego.speed

#Desenha os objetos na tela
def draw():
    screen.blit('caverna', (0, 0))
    morcego.draw()

#Executa sempre que o botão do mouse é pressionado
def on_mouse_down():
    morcego.y -= 50

#Cria o personagem morcego do jogo
morcego = Actor('morcego1', (75, 350))

#Velocidade do morcego
morcego.speed = 1