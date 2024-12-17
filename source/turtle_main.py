import turtle

def create_turtle():
    brad = turtle.Turtle()
    #brad.color("white")
    brad.speed(0)
    brad.pensize(1)
    brad.left(90)
    return brad


def draw_l_system(lineWidthBase, angle, string):
    lineWidth = lineWidthBase
    stack = []
    
    screen = turtle.Screen()
    print(len(string))

    screen.tracer(1,2)
    n_moves = 0
    pow10 = 100
    pow4 = 64
    
    brad = create_turtle()
    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = float("-inf"), float("-inf")
    llx, lly, urx, ury = 0, 0, 0, 0
    first_call = True
    
    margin = 20
    
    def update_bounds():
        nonlocal first_call
        nonlocal min_x, min_y, max_x, max_y
        nonlocal llx, lly, urx, ury
        
        x, y = brad.xcor(), brad.ycor()
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)
        if first_call or min_x - llx <= margin or min_y - lly <= margin or urx - margin <= 0 or ury - max_y <= margin:
            first_call = False
            # Adjust the screen view dynamically
            screen.setworldcoordinates(
                min_x - margin, min_y - margin,
                max_x + margin, max_y + margin
            )
            llx = min_x - margin
            lly = min_y - margin
            urx = max_x + margin
            ury = max_y + margin
    
    for char in string:
        if char in "FGAB":
            brad.forward(lineWidth)
            n_moves += 1
            update_bounds()
            if n_moves == pow10:
                pow10 *= 10
                pow4 *= 4
                screen.tracer(pow4,0)
        elif char == "+":
            brad.right(angle)  
        elif char == "-":
            brad.left(angle)
        elif char == "/":
            brad.right(angle / 2)
        elif char == "\\":
            brad.left(angle / 2)
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
            lineWidth = lineWidthBase * 2
        elif char == "[":
            stack.append((brad.heading(), brad.position(), lineWidth))
        elif char == "]":
            heading, position, lineWidth = stack.pop()
            brad.setheading(heading)
            brad.setpos(position)
    return brad, screen