from tkinter import*
import time
import random

root = Tk()

root.title("bounce!")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width = 500, height = 500, bd = 0, bg = 'black', highlightthickness = 0)
canvas.pack()

root.update()

global counter
counter = 0

global count
count = 0

class Ball:
    def __init__(self,  canvas,  paddle,  color,  obs):
        self.canvas = canvas
        self.paddle = paddle
        self.obs = obs
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id,  250,  200)

        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = -1
        self.y = start[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hitPaddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False


    def hitobs(self, pos, speed):
        global counter
        
        if(len(obs) == 0):
            canvas.create_text(250, 250, text = "YOU WON", fill = 'red')
            counter = counter + 1
            
        for i in range(len(obs)):
            obs_pos = self.canvas.coords(self.obs[i].id)

            if pos[2] >= obs_pos[0] and pos[0] <= obs_pos[2]:
                if pos[3] >= obs_pos[1] and pos[1] <= obs_pos[3]:

                    self.canvas.delete(self.obs[i].id)
                    self.obs.remove(self.obs[i])

                    self.y = speed[0]

                    return True
        return False

    def draw(self):
        global counter
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        speed = [3, 4]
        random.shuffle(speed)

        if pos[0] <= 0:
            self.x = speed[0]
        if pos[2] >= self.canvas_width:
            self.x = -speed[0]

        if pos[1] <= 0:
            self.y = speed[0]
        if pos[3] >= self.canvas_height:
            canvas.create_text(250, 50, text = "GAME OVER", fill = 'red')
            counter = counter+1

        if self.hitPaddle(pos)  ==  True:
            self.y = -speed[0]

        self.hitobs(pos, speed)
            

class Obs:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 37, 37, fill = color)
        self.canvas.move(self.id, x, y)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 250, 490)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.focus_set()
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)

    def turnLeft(self, event):
        paddle_pos = self.canvas.coords(self.id)
        if paddle_pos[0] <= 0:
            self.x = 0
        else:
            self.x = -6
        self.canvas.move(self.id, self.x, 0)
    def turnRight(self, event):
        paddle_pos = self.canvas.coords(self.id)
        if paddle_pos[2] >= self.canvas_width:
            self.x = 0
        else:
            self.x = 6
        self.canvas.move(self.id, self.x, 0)

paddle = Paddle(canvas, "white")

COLOR = ["PeachPuff3", "dark slate gray", "rosy brown", "light goldenrod yellow", "turquoise3", "salmon",
                       "light steel blue", "dark khaki", "pale violet red", "orchid", "tan", "MistyRose2",
                       "DodgerBlue4", "wheat2", "RosyBrown2", "bisque3", "DarkSeaGreen1"]
b = []
for i in range(0, 3):

    for j in range(0, 12):
        random.shuffle(COLOR)
        tmp = Obs(canvas, COLOR[0], (50 * j) + 10, (50 * i))
        b.append(tmp)


obs = b
ball = Ball(canvas, paddle, "red", obs)
while(1):
        ball.draw()
        root.update()
        root.update_idletasks()
        time.sleep(0.01)
        if(counter>0):
            break

root.mainloop()
