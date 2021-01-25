#Título da janela
TITLE = 'Fuga da Caverna'
#Largura da janela
WIDTH = 800
# Altura da janela
HEIGHT = 679

#Função para desenhar a tela
def draw():
    screen.blit('caverna', (0, 0))
    morcego.draw()

#Aqui a gente pega o clique do mouse
def on_mouse_down():
    morcego.y -= 50

#Função de atualização. Normalmente é chamada 60 vezes por segundo
def update():
    morcego.y += morcego.speed

#Adicionando o morcego
morcego = Actor('morcego1', (75, 350))

#Aumentando a velocidade do morcego
morcego.speed = 1