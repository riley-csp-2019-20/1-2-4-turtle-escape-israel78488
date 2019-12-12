
import turtle as trtl
import random

israel = trtl.Turtle()
israel.ht()
israel.speed(0)

Judah = trtl.Turtle()
Judah.speed(0)
trtl.pencolor = "red"




wall_width = 15
door_width = 20
distance = 40

def drawDoor():
    israel.penup()
    israel.forward(door_width)
    israel.pendown()
    

def drawBarrier():
    israel.right(90)
    israel.forward(2*wall_width)
    israel.backward(2*wall_width)
    israel.left(90)


for i in range(25):

    if i > 4:
        #door
        door = random.randint(door_width, distance - 2* door_width)
        #barrier
        barrier = random.randint(2*wall_width, distance - 2* door_width)

        
        if door < barrier:
            israel.forward(door)
            drawDoor()

            israel.forward(barrier - door - door_width)
            drawBarrier()
            israel.forward(distance - barrier)

        else: 
            israel.forward(barrier)
            drawBarrier()


            israel.forward(door - barrier)
            drawDoor()
            israel.forward(distance - door - door_width)

    israel.right(90)
    distance +=wall_width


#movement functions

def up():
    Judah.setheading(90)
    Judah.forward(10)

def right():
    Judah.setheading(0)
    Judah.forward(10)

def down():
    Judah.setheading(270)
    Judah.forward(10)

def left():
    Judah.setheading(180)
    Judah.forward(10)        


#onkeypress

wn = trtl.Screen()

wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(up,"Up")
wn.listen()

wn.mainloop()
