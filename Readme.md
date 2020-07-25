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

* Fonctionnement de l'animation' :
	+ On utilise un QGraphicsView et un QGraphicsScene. Le QGraphicsScene contient tout les objets qu'on veut animer (boids, borat etc...)
	+ On lance l'animation dans un QThread. Il va calculer les coordonées des boids a intervalles réguliers (définis par nous) et les envoyer aux objets créés dans le QGraphicsScene
	+ Le QThread permet de ne pas bloquer toute l'application, et d'avoir un affichage fluide de l'animation.



# Modules

### Prerequisites

+ Python 3
+ pip

### For Windows environments : 
```bash
python -m pip install pyqt5
python -m pip install pyqt5-tools
python -m pip install numpy
python -m pip install matplotlib
```

### For Linux environments :
```bash
python3 -m pip install pyqt5==5.14
sudo apt-get install python3-pyqt5 -y
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools -y
pip3 install numpy
pip3 install matplotlib
```

# Run

```
python3 main.py
```