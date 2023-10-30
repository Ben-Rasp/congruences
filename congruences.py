from turtle import *
import math
fenetre= Screen()
speed(0)




def point_decagone(longueur, diametre = 5, couleur = 'black'):
    """Fonction pour faire les points des sommets d'un octogone"""
    speed(0)
    color('red')
    for nb_cote in range(11):
        left(360/11)
        dot(diametre, couleur)
        up(); forward(longueur); down()
        
def repere(xmin, xmax, xgrad, ymin, ymax, ygrad):
    ##----- Fenêtre d'affichage et options -----##
    ##fenetre = Screen()
    ##fenetre.setworldcoordinates(xmin, ymin, xmax, ymax)
    speed(0)										# Vitesse la plus rapide
    color("black")
    ##----- Axe des abscisses -----##
    up()
    goto(xmin, 0)
    down()
    goto(xmax, 0)
    nbxgrad = int((xmax - xmin)/xgrad  + 1)
    long_xgrad = (ymax - ymin)/400.0 * 5
    for i in range(nbxgrad):
        x = xmin + i * xgrad
        up()
        goto(x, -long_xgrad)
        down()
        goto(x, long_xgrad)
    ##----- Axe des ordonnées -----##
    up()
    goto(0, ymin)
    down()
    goto(0, ymax)
    nbygrad = int((ymax - ymin)/ygrad  + 1)
    long_ygrad = (xmax - xmin)/400.0 * 5
    for i in range(nbygrad):
        y = ymin + i * ygrad
        up()
        goto(-long_ygrad, y)
        down()
        goto(long_ygrad, y)

def carre(xmin,xmax):
    color('red')
    up()
    for x in range(xmin,xmax):
        y = x**2 / 300
        goto(x,y)
        down()
    

#repere(-400, 400, 50, -400, 400, 50)
#carre(-300, 300)
def cercle(x0, y0, n, modulo):
    up(); goto(x0-15, y0-20); down();
    write(f'Congruences de {n} modulo {modulo}')
    up();goto(x0,y0); down()
    positions = []
    flag=0
    for x in range(0,modulo):
        forward(1000*1/modulo)
        left(360/modulo)
        dot()
        positions.append(pos())
        if modulo < 51:
            write(flag, align="left", font=("calibri", 12, "normal"))
        flag += 1
    flag = 1
    color = "red"
    for x in range(1,modulo):
        multiplication = n * x
        mod = multiplication % modulo
        modx, mody = positions[mod]
        up()
        goto(positions[x])
        down()
        goto(positions[mod])

cercle(-300, 60, 18, 104)
cercle(150, 60, 18, 105)
cercle(-300, -320, 18, 106)
cercle(150, -320, 18, 107)





    
    


    
