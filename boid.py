################################
# Classe correspondant aux boids
# Un boid possède :
#    - une position x
#    - une position y
#    - Une vitesse v (qu'on considère comme constante pour l'instant)
#    - ...
# Un boid peut :
#    - boidMove() : Se déplacer
#    - boidMeet() : Rencontrer quelqu'un et adapter son comportement en conséquence
#    - boidAvoid() : Changer de trajectoire en approchant un obstacle 
#    - ...
###############################
class boid:

    def __init__(self,x,y,v):
        self.x = x
        self.y = y
        self.v = v

    # Boid se déplace
    def boidMove(self):
        pass

    #
    def boidMeet(self):
        pass

    def boidAvoid(self):
        pass