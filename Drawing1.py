import turtle

#Drawing Mount Fuji

Fuji=turtle.Turtle()

#Moving to the tip of the mountain

Fuji.penup()
Fuji.left(90)
Fuji.forward(100)
Fuji.right(90)
Fuji.pendown()

#Drawing Mount Fuji (triangle)

Fuji.color("gray")
Fuji.begin_fill()
Fuji.right(60)
Fuji.forward(200)
Fuji.right(120)
Fuji.forward(200)
Fuji.right(120)
Fuji.forward(200)
Fuji.end_fill()

#Drawing the snowcap
Fuji.color("white")
Fuji.penup()
Fuji.left(180)
Fuji.forward(60)
Fuji.left(180)
Fuji.pendown()
Fuji.begin_fill()
Fuji.right(20)
Fuji.forward(20)
Fuji.right(80)
Fuji.forward(20)
Fuji.left(80)
Fuji.forward(20)
Fuji.right(80)
Fuji.forward(20)
Fuji.left(160)
Fuji.forward(60)
Fuji.left(120)
Fuji.forward(60)
Fuji.end_fill()