import matplotlib.pyplot as plt
import math
from celluloid import Camera
import random

#класс частицы
class system():
          
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.m = 10
        # силы тяжести частицы
        # self.Fx = (16-x)/math.fabs(r)**13 - (16-x)/math.fabs(r)**7
        # self.Fy = (16-y)/math.fabs(r)**13 - (16-y)/math.fabs(r)**7
        # self.Fz = (16-z)/math.fabs(r)**13 - (16-z)/math.fabs(r)**7
        self.Fx = 1/self.module_comparisonx(self.x)
        self.Fy = 1/self.module_comparisony(self.y)
        self.Fz = 1/self.module_comparisonz(self.z)
        #её координаты
        self.coord = [self.x, self.y, self.z]
        #ускорения частиц
        self.Ax= self.Fx/self.m
        self.Ay= self.Fy/self.m
        self.Az= self.Fz/self.m
        #скорость частиц
        self.vx= random.random() - 0.5
        self.vy= random.random() - 0.5
        self.vz= random.random() - 0.5
        #для удобства - массивы с силами,ускорениями и скоростями
        self.F = [self.Fx,self.Fy,self.Fz]
        self.A = [self.Ax,self.Ay,self.Az]
        self.V = [self.vx,self.vy,self.vz]
#обновляет данные массива
    def update(self):
        self.coord = [self.x, self.y, self.z]
        self.F = [self.Fx,self.Fy,self.Fz]
        self.A = [self.Ax,self.Ay,self.Az]
        self.V = [self.vx,self.vy,self.vz]
# вычисляет расстояние до близжайшей границы и осуществляет неупругое отталкивание по оси X
    def module_comparisonx(self,a):
        if abs(a) < abs(a - 16):
            if a<0:
                self.vx = abs(self.vx) / 2
                self.update()
            return abs(a)
        else:
            if a>16:
                self.vx = - abs(self.vx) / 2
                self.update()
            return -abs(a - 16)       
# вычисляет расстояние до близжайшей границы и осуществляет неупругое отталкивание по оси Y
    def module_comparisony(self,a):
        if abs(a) < abs(a - 16):
            if a<0:
                self.vy = abs(self.vy) / 2
                self.update()
            return abs(a)
        else:
            if a>16:
                self.vy = - abs(self.vy) / 2
                self.update()
            return -abs(a - 16)
# вычисляет расстояние до близжайшей границы и осуществляет неупругое отталкивание по оси Z
    def module_comparisonz(self,a):
        if abs(a) < abs(a - 16):
            if a<0:
                self.vz = abs(self.vz) / 2
                self.update()
            return abs(a)
        else:
            if a>16:
                self.vz = - abs(self.vz) / 2
                self.update()
            return -abs(a - 16)             
    
cube = []
for x in range(6,10):
    for y in range(6,10):
        for z in range(6,10):
            p = system(x,y,z)
            cube.append(p)

# 1 шаг частицы с учетом всех координат
chast = []
inter = []
radius = 3
helper = 0
def step(vertices,ax):
    global chast,inter,helper
    def raast(a,b):
        '''функция нахождения расстояния между частицами'''
        return math.sqrt((a.coord[0]-b.coord[0])**2 + (a.coord[1]-b.coord[1])**2 + (a.coord[2]-b.coord[2])**2)

    for item in range(64):
        for j in range(3):
            vertices[item].coord[j] += vertices[item].V[j]
            vertices[item].V[j] += vertices[item].A[j]

            #изменение силы взаимодействия со стенкой и вычисление ускорения
            vertices[item].F[j] = 1/(vertices[item].module_comparisonx(vertices[item].coord[j]))

            vertices[item].A[j]= vertices[item].F[j]**3/vertices[item].m


        #взаимодействие между часицами
        if ( ((distantion := raast(vertices[0], vertices[item])) < radius) and item!=0):
            chast.append(distantion)
            inter.append(item)
            helper = 1

        #ограничение ускорения (предельное ускорение)
        for j in range(3):
            if vertices[item].A[j] > 0.2:
                vertices[item].A[j] = 0.2
            if vertices[item].A[j] < -0.2:
                vertices[item].A[j] = -0.2
    

        #обновление цвета частиц
        if item==0:
            ax.scatter(vertices[item].coord[0], vertices[item].coord[1], vertices[item].coord[2], c='black', marker='*')
        elif helper==0:
            ax.scatter(vertices[item].coord[0], vertices[item].coord[1], vertices[item].coord[2], c='r', marker='.')
        else:
            ax.scatter(vertices[item].coord[0], vertices[item].coord[1], vertices[item].coord[2], c='g', marker='.')
        
        helper = 0
        
    for index,item in enumerate(inter): #эта   функция энумерате возвращается кортежи (индекс элемента массива, сам элемент массива)
        print(index, item)              #сделано это для того,чтобы было проще связывать этот массив с массивом chast
        for j in range(3):
            print(f'--|{vertices[item].coord[j]}|--')
            vertices[item].A[j] += (vertices[item].coord[j]/math.fabs(chast[index])**13 - 
                                    vertices[item].coord[j]/math.fabs(chast[index])**7)/vertices[item].m
    chast = []
    inter = []

#границы куба
def lines(ax):
    edge_vertices = [[0,0,0],[16,0,0],[16,16,0],
                    [0,16,0],[0,0,16],[16,0,16],
                    [16,16,16],[0,16,16]]
    x = [v[0] for v in edge_vertices]
    y = [v[1] for v in edge_vertices]
    z = [v[2] for v in edge_vertices]
    ax.scatter(x, y, z,c='blue',marker ='o')
    # Создание ребер куба путем соединения точек вершин
    edges = [    [0,1],[1,2],[2,3],[3,0],
                [4,5],[5,6],[6,7],[7,4],
                [0,4],[1,5],[2,6],[3,7]]
    for edge in edges:
        ax.plot3D(*zip(edge_vertices[edge[0]], edge_vertices[edge[1]]), color='blue')

#функция для вывода частиц
def plot_verticles(vertices):
    # Создание модели
    fig = plt.figure()
    camera = Camera(fig)
    ax = fig.add_subplot(111, projection='3d') 
    x = [v.coord[0] for v in vertices]
    y = [v.coord[1] for v in vertices]
    z = [v.coord[2] for v in vertices]    
    ax.scatter(x, y, z, c='r', marker='.')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Создание гиф
    lines(ax)
    camera.snap()
    for i in range(70): # кол-во кадров
        step(vertices,ax)
        lines(ax)
        camera.snap()
    animation = camera.animate()
    animation.save('dots.gif', writer = 'imagemagick')
    
#вызов функций
plot_verticles(cube)
print('ГОТОВО ЧЕКАЙ ГИФКУ')
