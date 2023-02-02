import numpy as np
import matplotlib.pyplot as plt
#класс частицы
class system():
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

cube = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            p = system(x,y,z)
            cube.append(p.coord)

vertices = np.array(
    [
        i for i in cube
    ]
)

plt.plot_verticles(vertices = vertices, isosurf = False)
exit()
#Это окно
tk = Tk()
tk.protocol("WM_DELETE_WINDOW")
tk.title("куб")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=900, height=600)
canvas.pack()
tk.mainloop()



