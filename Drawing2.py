import turtle

def olianahaddad_entry(x,y,scale):

    # Draws yellow circle as background using a loop(represents warmth and positivity).
    turtle.penup()
    turtle.goto(x,y-60*scale)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("gold","yellow")
    turtle.begin_fill()
    for i in range(36):
        turtle.forward((2*3.14*60*scale)/36)
        turtle.left(10)
    turtle.end_fill()

    # Draws orange star inside the circle using a loop(symbolizes creativity and uniqueness).
    turtle.penup()
    turtle.goto(x,y-35*scale)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("orange","orange")
    turtle.begin_fill()
    for i in range(5):   # Draws 5 points of the star.
        turtle.forward(70*scale)
        turtle.right(144)
    turtle.end_fill()

def main():
    turtle.speed(0)
    # Draws two stamps, not overlapping.
    olianahaddad_entry(-70,0,1)
    olianahaddad_entry(70,30,0.8)

main()