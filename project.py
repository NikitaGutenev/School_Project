import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import numpy as np
from celluloid import Camera

#класс частицы
class system():
    def __init__(self, x, y, z):
        r = math.sqrt(x**2 + y**2 + z**2)
        m = 10
        # силы тяжести частицы
        self.Fx = x/math.fabs(r)**13 - x/math.fabs(r)**7
        self.Fy = y/math.fabs(r)**13 - y/math.fabs(r)**7
        self.Fz = z/math.fabs(r)**13 - z/math.fabs(r)**7
        #её координаты
        self.coord = [x, y, z]
        #ускорения частиц
        self.Ax= self.Fx/m
        self.Ay= self.Fy/m
        self.Az= self.Fz/m
        #скорость частиц
        self.vx= 1
        self.vy= 1
        self.vz= 1
        

# создание куба с частицами
cube = []
for x in range(3,13):
    for y in range(3,13):
        for z in range(3,13):
            p = system(x,y,z)
            cube.append(p)

def step(vertices,ax):
    for item in range(1000):
        vertices[item].vx += vertices[item].Ax
        vertices[item].vy += vertices[item].Ay
        vertices[item].vz += vertices[item].Az
        vertices[item].coord[0] += vertices[item].vx
        vertices[item].coord[1] += vertices[item].vy
        vertices[item].coord[2] += vertices[item].vz
        ax.scatter(vertices[item].coord[0], vertices[item].coord[1], vertices[item].coord[2], c='r', marker='.')

def lines(ax):
    edge_vertices = [
    [0,0,0],
    [16,0,0],
    [16,16,0],
    [0,16,0],
    [0,0,16],
    [16,0,16],
    [16,16,16],
    [0,16,16]]
    x = [v[0] for v in edge_vertices]
    y = [v[1] for v in edge_vertices]
    z = [v[2] for v in edge_vertices]
    ax.scatter(x, y, z,marker ='o')
    # Connect the vertices to form the edges of the cube
    edges = [    [0,1],
        [1,2],
        [2,3],
        [3,0],
        [4,5],
        [5,6],
        [6,7],
        [7,4],
        [0,4],
        [1,5],
        [2,6],
        [3,7]
    ]
    for edge in edges:
        ax.plot3D(*zip(edge_vertices[edge[0]], edge_vertices[edge[1]]), color='blue')

#функция для вывода частиц
def plot_verticles(vertices, isosurf = False, filename = None, borders = None):
    # Create a new plot
    fig = plt.figure()
    camera = Camera(fig)
    ax = fig.add_subplot(111, projection='3d') 
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    # Show or save the plot
    if filename is None:
        for i in range(10):
            step(vertices,ax)
            lines(ax)
            plt.show()
            camera.snap()
        animation = camera.animate()
        animation.save('dots.gif', writer = 'imagemagick')
    else:
        plt.savefig(filename)    

#вызов функций
plot_verticles(cube, isosurf = False, filename = None, borders = None)


