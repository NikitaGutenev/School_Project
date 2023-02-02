import numpy as np
import matplotlib.pyplot as plt


#класс частицы
class system():
    def __init__(self, x, y, z):
        self.coord = (x, y, z)


# создание куба с частицами
cube = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            p = system(x,y,z)
            cube.append(p.coord)

#функция для вывода частиц
def plot_verticles(vertices, isosurf = False, filename = None):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]    
    if isosurf:
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    else:
        ax.scatter(x, y, z, c='r', marker='*')    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)



plot_verticles(vertices = cube, isosurf = False)



