from turtle import *
speed(0)        

def dessine_congruences(x0, y0, n, modulo):
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
#    flag = 1
#    color = "red"
    for x in range(1,modulo):
        multiplication = n * x
        mod = multiplication % modulo
        modx, mody = positions[mod]
        up()
        goto(positions[x])
        down()
        goto(positions[mod])
    return positions

##dessine_congruences(-300, 60, 18, 47)
##dessine_congruences(150, 60, 18, 48)
##dessine_congruences(-300, -320, 18, 49)
#dessine_congruences(150, -320, 18, 50)

class Congruences:
    def __init__(self, nombre, modulo):
        self.nombre = nombre
        self.modulo = modulo
        self.positions = []

    def dessine_cercle(self, xorigine=-100, yorigine=-200):
        self.xorigine = xorigine
        self.yorigine = yorigine
        up(); goto(self.xorigine-25, self.yorigine-30); down();
        write(f'Congruences de {self.nombre} modulo {self.modulo}',
              font=("calibri", 14, "normal"))
        up();goto(self.xorigine, self.yorigine); down()
        flag = 0
        for x in range(0,self.modulo):
            forward(1500*1/self.modulo)
            left(360/self.modulo)
            dot()
            self.positions.append(pos())
            if self.modulo < 51:
                write(flag, align="left", font=("calibri", 18, "normal"))
            flag += 1
        
        for x in range(1,self.modulo):
            multiplication = self.nombre * x
            mod = multiplication % self.modulo
            modx, mody = self.positions[mod]
            up()
            goto(self.positions[x])
            down()
            goto(self.positions[mod])
    
    def histogramme(self):
        mods = [(self.nombre*x)% self.modulo for x in range(1, self.modulo)]
        self.sommes_congruences= []
        xaxis = [x for x in range(self.modulo)]
        for m in xaxis:
            self.sommes_congruences.append(mods.count(m))
        self.fig = plt.plot(xaxis, self.sommes_congruences)
        plt.show()
        
C = Congruences(4, 10)
C.dessine_cercle()

