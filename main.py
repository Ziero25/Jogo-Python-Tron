from turtle import *
from freegames import square, vector
from time import sleep

p1xy = vector(-200, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(200, 0)
p2aim = vector(-4, 0)
p2body = set()

p3xy = vector(0, 200)
p3aim = vector(0, -4)
p3body = set()




#------------Define a area do jogo(Quadrado que abre o jogo)------------#
def inside(head):
    """Return True if head inside screen."""
    return -300 < head.x < 300 and -300 < head.y < 300


#------------Menssagem de saudação------------#
print()
print('=================================================')
print('         Bem-vindo a Grade de Tron!         ')
print('=================================================')
print()

#------------Script para fazer o usuario escolhe a cor do personagem------------#
colors = ['red', 'green', 'blue', 'black', 'orange', 'pink', 'gray', 'purple']
count = 0
lenght = len(colors) - 1
colorPlayer1 = input(f"Escolha a cor do Player 1: {colors} ")
colorPlayer2 = input(f"Escolha a cor do Player 2: {colors} ")
colorPlayer3 = input(f"Escolha a cor do Player 3: {colors} ")
    
while(count <= lenght):
    if(colors[count] == colorPlayer1):
        square(p1xy.x, p1xy.y, 3, colors[count])
        break
    count += 1

#------------Temporizador para inicio do jogo------------#
sleep(1)
print('STARTING GAME...')
sleep(1)
print("3")
sleep(1)  
print("2")
sleep(1)
print("1")
sleep(1)
print("GO!")

#-----------Define os movimentos dos players-------------#
def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    p3xy.move(p3aim)
    p3head = p3xy.copy()


    

#------------Colisão dos players entre eles------------#
    if not inside(p1head) or p1head in p2body:
        print(f"Player {colorPlayer2} and {colorPlayer3} wins!")
        return

    if not inside(p1head) or p1head in p3body:
        print(f"Player {colorPlayer2} and {colorPlayer3} wins!")
        return

    if not inside(p2head) or p2head in p1body:
        print(f"Player {colorPlayer1} and {colorPlayer3} wins!")
        return

    if not inside(p2head) or p2head in p3body:
        print(f"Player {colorPlayer1} and {colorPlayer3} wins!")
        return

    if not inside(p3head) or p3head in p1body:
        print(f"Player {colorPlayer1} and {colorPlayer2} wins!")
        return

    if not inside(p3head) or p3head in p2body:
        print(f"Player {colorPlayer1} and {colorPlayer2} wins!")
        return

    
#------------Colisão do player em si mesmo------------#
    if not inside(p1head) or p1head in p1body:
        print(f"Player {colorPlayer2} and {colorPlayer3} wins!")
        return

    if not inside(p2head) or p2head in p2body:
        print(f"Player {colorPlayer1} and {colorPlayer3} wins!")
        return

    if not inside(p3head) or p3head in p3body:
        print(f"Player {colorPlayer1} and {colorPlayer2} wins!")
        return

#-----------Adiciona o 'corpo' a 'cabeça'-------------#
    p1body.add(p1head)
    p2body.add(p2head)
    p3body.add(p3head)


#------------Adiciona a direção para que os quadrados devem seguir------------#
    square(p1xy.x, p1xy.y, 3, colorPlayer1)
    square(p2xy.x, p2xy.y, 3, colorPlayer2)
    square(p3xy.x, p3xy.y, 3, colorPlayer3)
    update()
    ontimer(draw, 20)

#------------Adiciona as teclas de comando------------#
setup(600, 600, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 's')
onkey(lambda: p2aim.rotate(90), 'g')
onkey(lambda: p2aim.rotate(-90), 'h')
onkey(lambda: p3aim.rotate(90), '9')
onkey(lambda: p3aim.rotate(-90), '5')
draw()
done()

#------------Alterações Realizadas------------#
#Criação do Player 3
#Escolha de cor do player
#Colisão entre os players e entre eles mesmos
#Adicionado um Temporizador para começar o jogo.
#Boost de velocidade - Não feito
#Imagem de fundo - Não feito