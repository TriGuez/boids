# Idées et fonctionnement :

* Fonctionnement global :
    + Classe boids. Chaque possède ses caractéristiques et son comportement est géré par une fonction utilisant les caractéristiques du boid. Ils gèrent leur vie.
    + Penser aux variables x,y mais aussi nouveau_x et nouveau_y 
    + Le tableau n'est PAS une grille mais bien un plan cartésien en x et en y, chaque coordonnée doit être calculée en conséquence -> quick math
    + Le choix :
        - Soit tout est calculé avant et tout est mis à jour d'un coup pour l'affichage -> relativement fluide si pas trop d'oiseaux :
        ```
        while(1):
            for i in boid_list:
                i.behave()
            
            OpenGL.update()
        ```
        - Soit l'oiseau sont calculé à tour de role -> fluide :
        ```
        while(1):
            for i in boid_list:
                i.behave()
                OpenGL.print_boid(i)

            for i in boid_list:
                i.update_coord() # nouveau_x <- x ...
        ```

* OpenGL : Mystère et boule de Guezennec



# Modules 
```bash
python -m pip install pyqt5
python -m pip install pyqt5-tools
python -m pip install PyOpenGL
```