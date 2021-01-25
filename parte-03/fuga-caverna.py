#Título da janela
TITLE = 'Fuga da Caverna'
#Largura da janela
WIDTH = 800
# Altura da janela
HEIGHT = 679

#Função para desenhar na tela
def draw():
    screen.blit('caverna', (0, 0))
    morcego.draw()
    estalactite_pequena.draw()
    estalagmite_pequena.draw()

#Aqui a gente pega o clique do mouse
def on_mouse_down():
    morcego.y -= 50

#Função de atualização. Normalmente é chamada 60 vezes por segundo
def update():
    morcego.y += morcego.speed
    estalactite_pequena.x -= velocidade_tela
    estalagmite_pequena.x -= velocidade_tela
    if estalactite_pequena.x < 0:
        estalactite_pequena.x = WIDTH
        estalagmite_pequena.x = WIDTH

#Adicionando o morcego
morcego = Actor('morcego1', (75, 350))

#Aumentando a velocidade do morcego
morcego.speed = 1

#Definindo a velocidade da tela
velocidade_tela = 1

#Definindo o espaço entre estalactites e estalagmites, para o morcego passar no meio
espaco = 200

#Adicionando os obstáculos
estalactite_pequena = Actor('estalactite1', (300, 0))
estalagmite_pequena = Actor('estalagmite1', (300, estalactite_pequena.height + espaco))