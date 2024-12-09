from turtle import Screen, Turtle
from generate_string import generate_string, read_archive

def create_screen():
    screen = Screen()
    screen.title("Fractais")
    screen.bgcolor("black")
    return screen

def create_turtle():
    brad = Turtle()
    brad.color("white")
    brad.pensize(1)
    brad.left(90)
    
    string = generate_string(6, read_archive("rules.json"))
    
    stack = []
    for char in string:
        if char == "F":
            brad.forward(2)
        elif char == "+":
            brad.right(25)
        elif char == "-":
            brad.left(25)
        elif char == "/":
            brad.right(45)
        elif char == "\\":
            brad.left(45)
        elif char == "r":
            brad.color("red")
        elif char == "g":
            brad.color("green")
        elif char == "b":
            brad.color("blue")
        elif char == "n":
            brad.color("white")
        elif char == "[":
            stack.append((brad.heading(), brad.position()))
        elif char == "]":
            heading, position = stack.pop()
            brad.setheading(heading)
            brad.setpos(position)
    
    return brad

if __name__ == "__main__":
    screen = create_screen()
    brad = create_turtle()
    screen.mainloop()
