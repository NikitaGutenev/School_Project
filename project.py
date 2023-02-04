import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.animation import FuncAnimation


#класс частицы
class system():
    def __init__(self, x, y, z):
        r = math.sqrt(x**2 + y**2 + z**2)
        # силы тяжести частицы
        self.Fx = x/math.fabs(r)**13 - x/math.fabs(r)**7
        self.Fy = y/math.fabs(r)**13 - y/math.fabs(r)**7
        self.Fz = z/math.fabs(r)**13 - z/math.fabs(r)**7
        #её координаты
        self.coord = (x, y, z)


# создание куба с частицами
cube = []
for x in range(3,13):
    for y in range(3,13):
        for z in range(3,13):
            p = system(x,y,z)
            cube.append(p.coord)



#функция для вывода частиц
def plot_verticles(vertices, isosurf = False, filename = None, borders = None):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]    
    if isosurf:
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    else:
        ax.scatter(x, y, z, c='r', marker='.')    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    #  ----- creating a limited space for particles -----
    edge_vertices = [    
        [0,0,0],
        [16,0,0],
        [16,16,0],
        [0,16,0],
        [0,0,16],
        [16,0,16],
        [16,16,16],
        [0,16,16]
    ]
    # Plot the vertices
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


    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)

    

#вызов функций
plot_verticles(vertices = cube, isosurf = False)


