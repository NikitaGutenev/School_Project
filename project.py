import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time

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


#animation
def anima(vertices,ax):
    xs = []
    ys = []
    zs = []
    for i in range(5):
        for item in range(len(vertices)):
            vertices[item].vx += vertices[item].Ax
            vertices[item].vy += vertices[item].Ay
            vertices[item].vz += vertices[item].Az
            vertices[item].coord[0] += vertices[item].vx
            vertices[item].coord[1] += vertices[item].vy
            vertices[item].coord[2] += vertices[item].vz
            x = vertices[item].coord[0]
            y = vertices[item].coord[1]
            z = vertices[item].coord[2]
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    mass = zip(xs,ys,zs)
    for (i,j,k) in mass:
        ax.clear()
        ax.plot(i,j,k)
        ax.scatter(i, j, k, c='r', marker='.') 
        time.sleep(1/1000)

#функция для вывода частиц
def plot_verticles(vertices, isosurf = False, filename = None, borders = None):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v.coord[0] for v in vertices]
    y = [v.coord[1] for v in vertices]
    z = [v.coord[2] for v in vertices]    
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
        ani = animation.FuncAnimation(fig,anima(vertices,ax),interval=1000)
        plt.show()
    else:
        plt.savefig(filename)



    

#вызов функций
plot_verticles(vertices = cube, isosurf = False)


