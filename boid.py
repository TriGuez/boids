from math import cos,sin,pi, sqrt
import numpy as np
import random

'''
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
        self.v_save = v
        self.a = a
        self.nouveau_x = 0
        self.nouveau_y = 0

        self.chmgt_angle = 0

        self.wall_bas = 0
        self.wall_haut = 760
        self.wall_gauche = 0
        self.wall_droite = 1130
        self.bordure_safe = 3 * self.v
        self.avoided = False
        self.cpt_avoided = 0


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
            self.avoided = True
            #correction_random = random.uniform(pi/2 - pi/8 ,pi/2 + pi/8 )
            #self.a = self.a + correction_random
            self.a = self.a + pi / 2

            self.cpt_avoided = self.cpt_avoided + 1
            if(self.cpt_avoided >= 10):
                self.v = self.v + 0.1

        else:
            self.avoided = False
            self.cpt_avoided = 0
            self.v = self.v_save

    # Mise à jour des x et y, et rajout de hasard dans l'orientation
    def boidUpdate(self):
        self.x = self.nouveau_x
        self.y = self.nouveau_y
        

        if(self.avoided == False):
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

    def get_nv_x(self):
        return self.get_nv_x

    def get_nv_y(self):
        return self.get_nv_y'''

def UpdateBoidPos(x, y, angle, speed, distance, cohesion) :
    x=x+ speed*np.sqrt(2) * np.cos(angle)
    y=y+ speed*np.sqrt(2) * np.sin(angle)
    '''
    if x >= 1130 :
        angle = (pi-angle)
    if x <= 0 :
        angle = pi-angle
    if y >= 760 :
        angle = (-angle)
    if y <= 0 :
        angle = -angle
        '''
    bound_x_max = np.where(x>=1130)
    bound_x_min = np.where(x<=0)
    bound_y_max = np.where(y>=720)
    bound_y_min = np.where(y<=0)
    angle[bound_x_max] = np.pi-angle[bound_x_max]
    angle[bound_x_min] = np.pi-angle[bound_x_min]
    angle[bound_y_max] = -angle[bound_y_max]
    angle[bound_y_min] = -angle[bound_y_min]
    return x,y, angle+[((random.random()-0.5)*pi/180 *10) for _ in range(np.size(angle))]