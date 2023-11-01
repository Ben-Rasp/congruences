from turtle import *
speed(0)        

def dessine_congruences(x0, y0, n, modulo):      ##création de la fonction
    """Déplace le curseur de turtle vers le début deu schéma, trace un cercle 
    sur lequel sont répartis les nombres entre 0 et le modulo (c'est à dire tous
    les 'restes' possibles) puis trace le liens entre les nombres de la table de 
    multiplication et leur congruence."""
    up(); goto(x0-25, y0-30); down();            ##le crayon se déplace
    write(f'Congruences de {n} modulo {modulo}', ##Création du titre de l'image
         font=('calibri', 14, 'normal'))         
    up();goto(x0,y0); down()                     ##le crayon se déplace: x0,y0
    speed(0)                                     ##et il s'abaisse pour écrire
    positions = []                               ##liste des positions (vide)

    for x in range(0,modulo):                    ##pour chaque nbr du modulo...
        forward(1500*1/modulo)                   ##je m'avance d'une distance
                                                 ##proportionnelle (pour rester
                                                 ##dans le cadre)
        left(360/modulo)                         ##je tourne ensuite d'un angle
                                                 ##particulier (360 / modulo)
        dot()                                    ##je trace un point
        positions.append(pos())                  ##les coordonnées de ce point
                                                 ##sont stockées dans positions
        if modulo < 51:      ##si le modulo est <51, je peux noter les nombres.
            write(x, align="left", font=("calibri", 12, "normal"))

    for x in range(1,modulo):          ##pour chaque nombre de modulo...
        multiplication = n * x         ##je calcule sa multiplication par n
        mod = multiplication % modulo  ##je calcule le résultat de cette 
                                       ##multiplication modulo (le reste)
        modx, mody = positions[mod]    ##les coord x,y sont celles du point
                                       ##stocké dans positions à son emplacement
        up()                           ##je soulève le crayon
        goto(positions[x])             ##je me déplace vers le point x
        down()                         ##je baisse le crayon pour tracer
        goto(positions[mod])           ##je trace le trait vers le modulo de x

#MAIN_________________________________________________________________________

if __name__=="__main__":
    dessine_congruences(-150, -200, 12, 10) #polygone de la table de 12, modulo 4
