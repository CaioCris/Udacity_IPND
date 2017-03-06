import turtle

def draw_square(square_turtle):
    for i in range(1,5):
        square_turtle.forward(100)
        square_turtle.right(90)

def draw_triangle(triangle_turtle):
    for i in range(1,4):
        triangle_turtle.forward(100)
        triangle_turtle.left(120) 

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #Brad - draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Angie - draw circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    #Carl - draw triangle
    carl = turtle.Turtle()
    carl.shape("triangle")
    carl.color("yellow")
    draw_triangle(carl)

    window.exitonclick()

draw_art()