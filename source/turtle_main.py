from turtle import Screen, Turtle
from generate_string import generate_string, read_archive

def create_screen():
    screen = Screen()
    screen.title("Fractais")
    screen.bgcolor("black")
    return screen

def create_turtle(lineWidthBase, angle, string):
    brad = Turtle()
    brad.color("white")
    brad.pensize(1)
    brad.left(90)
    
    lineWidth = lineWidthBase
    stack = []
    for char in string:
        if char in "FGAB":
            brad.forward(lineWidth)
        elif char == "+":
            brad.right(angle)  
        elif char == "-":
            brad.left(angle)
        elif char == "/":
            brad.right(angle/2)
        elif char == "\\":
            brad.left(angle/2)
        elif char == "r":
            brad.color("red")
        elif char == "g":
            brad.color("green")
        elif char == "b":
            brad.color("blue")
        elif char == "n":
            brad.color("white")
        elif char == "1":
            lineWidth = lineWidthBase
        elif char == "2":
            lineWidth = lineWidthBase*2
        elif char == "[":
            stack.append((brad.heading(), brad.position(), lineWidth))
        elif char == "]":
            heading, position, lineWidth = stack.pop()
            brad.setheading(heading)
            brad.setpos(position)
    
    return brad

if __name__ == "__main__":
    screen = create_screen()
    brad = create_turtle()
    screen.mainloop()
