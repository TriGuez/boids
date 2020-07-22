from math import cos,sin

################################
# Classe correspondant aux boids
# Un boid possède :
#    - une position x
#    - une position y
#    - Une vitesse v (qu'on considère comme constante pour l'instant)
#    - Un angle a
#    - nouveau_x et nouveau_y pour gérer les trucs
#    - ...
# Un boid peut :
#    - boidMove() : Se déplacer
#    - boidMeet() : Rencontrer quelqu'un et adapter son comportement en conséquence
#    - boidAvoid() : Changer de trajectoire en approchant un obstacle 
#    - ...
###############################
class boid:

    def __init__(self,x,y,v,a):
        self.x = x
        self.y = y
        self.v = v
        self.a = a
        self.nouveau_x = 0
        self.nouveau_y = 0



    # Boid se déplace
    def boidMove(self):
        self.nouveau_x = self.x + self.v *cos(self.a)
        self.nouveau_y = self.x + self.v *sin(self.a)

    # Attention gérer les autres dudez
    def boidMeet(self):
        pass

    # Gestion des frontières : changer d'angle ?
    def boidAvoid(self):
        pass

    # Pour débug
    def boidPrint(self):
        print("x : " + str(self.x) + " & y : " + str(self.y))
        print(" New x : "+ str(self.nouveau_x) +"    New y :" + str(self.nouveau_y))
        print("------------------")