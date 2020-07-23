from math import cos,sin,pi
import random

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

        self.chmgt_angle = 0

        self.wall_bas = 0
        self.wall_haut = 100
        self.wall_gauche = 0
        self.wall_droite = 100
        self.bordure_safe = 5 * self.v


    def boidBehave(self):

        self.boidAvoid()
        self.boidMove()
        self.boidUpdate()

    # Boid se déplace
    def boidMove(self):
        self.nouveau_x = self.x + self.v * cos(self.a)
        self.nouveau_y = self.y + self.v * sin(self.a)

    # Attention gérer les autres dudez
    def boidMeet(self):
        pass

    # Gestion des frontières : changer d'angle ?
    def boidAvoid(self):
        if(self.x <= (self.wall_bas+self.bordure_safe) or self.x >= (self.wall_haut-self.bordure_safe) or self.y <= (self.wall_gauche+self.bordure_safe) or self.y >= (self.wall_droite-self.bordure_safe)):
            
            self.a = self.a + pi / 2



    # Mise à jour des x et y, et rajout de hasard dans l'orientation
    def boidUpdate(self):
        self.x = self.nouveau_x
        self.y = self.nouveau_y
        
        
        if(self.chmgt_angle == 20):
            nouveau_a = (random.uniform(-pi/4,pi/4))
            self.a = self.a + nouveau_a
            self.chmgt_angle = 0
        else:
           self.chmgt_angle = self.chmgt_angle + 1
           nouveau_a = (random.uniform(-pi/32,pi/32))
           self.a = self.a + nouveau_a
        

    # Pour débug
    def boidPrint(self):
        print("x : " + str(self.x) + " & y : " + str(self.y))
        print(" New x : "+ str(self.nouveau_x) +"    New y :" + str(self.nouveau_y))
        print("------------------")

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y