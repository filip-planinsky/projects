import turtle
import math


def draw_square(turtle_instance, square_side):
    """
    draw square
    """
    turtle_instance.color("green")

    for i in range(4):
        turtle_instance.fd(square_side)
        turtle_instance.lt(90)


def draw_triangle(turtle_instance, side_a, side_b, side_c, alpha, beta, gamma):
    """
    draw triangle with calculate length and angle
    """
    turtle_instance.color("blue")

    turtle_instance.lt(alpha)
    turtle_instance.fd(side_b)
    turtle_instance.rt(180 - gamma)
    turtle_instance.fd(side_c)
    turtle_instance.rt(180 - beta)
    turtle_instance.fd(side_a)


def set_position_for_new_level(turtle_side_b, side_b, alpha, gamma):
    """
    set drawing turtle to gamma angel and
    create two new turtle to restart iteration
    """
    turtle_side_b.rt(-alpha)
    turtle_side_b.bk(side_b)

    turtle_side_c = turtle_side_b.clone()
    turtle_side_c.color("blue")
    turtle_side_c.rt(180)
    turtle_side_c.bk(side_b)

    turtle_side_b.lt(gamma)

    return turtle_side_c, turtle_side_b


def draw_square_triangle(turtle_instance, square_side, alpha, beta):
    """
    draw square and triangel with given numbers
    returning new sides, gamma and two new squares
    """
    draw_square(turtle_instance, square_side)

    side_b, side_c, gamma = calculate_triangle(square_side, alpha, beta)

    # move turtle to alpha
    turtle_instance.lt(90)
    turtle_instance.fd(square_side)
    turtle_instance.rt(90)

    draw_triangle(turtle_instance, square_side, side_b, side_c, alpha, beta, gamma)

    turtle_side_c, turtle_side_b = set_position_for_new_level(turtle_instance, side_b, alpha, gamma)

    return side_b, side_c, gamma, turtle_side_c, turtle_side_b


def calculate_triangle(side_a, alpha, beta):
    """
    calculating the unknown angel and two sides
    for new triangle
    """
    gamma = 180 - alpha - beta

    # turning gamma and alpha into radian and calculating sine to calculate side_c afterwards
    gamma_sin = math.sin(math.radians(gamma))
    alpha_sin = math.sin(math.radians(alpha))

    # calculating length of side_c of triangle
    side_c = round((side_a / gamma_sin) * alpha_sin, 2)

    # turning beta into sin
    beta_sin = math.sin(math.radians(beta))

    # calculating length of side_b
    side_b = round((side_a / gamma_sin) * beta_sin, 2)

    return side_b, side_c, gamma


def draw_iteration(turtle1, side_a, alpha, beta, level):
    """
    draw figure for each iteration until reaching the
    given recursion level
    """

    if level > 0:
        side_b, side_c, gamma, turtle_side_c, turtle_side_b = draw_square_triangle(turtle1, side_a, alpha, beta)

        # draw iteration with two turtles
        draw_iteration(turtle_side_c, side_b, alpha, beta, level-1)
        draw_iteration(turtle_side_b, side_c, alpha, beta, level-1)

        turtle_side_c.hideturtle()
        turtle_side_b.hideturtle()


if __name__ == '__main__':
    """
    program prompt user for vaid input
    to draw squares and triangles recursively until
    recursion level is reached
    
    """

    while True:
        try:
            # prompt user for input and check if it's valid
            square_size = float(input("square size: "))
            alpha = int(input("angel Alpha: "))
            beta = int(input("angel Beta: "))
            recursion_level = int(input('recursion level: '))

        except ValueError:
            continue

        if square_size < 0 or alpha < 0 or beta < 0 or recursion_level < 0:
            print("Please enter valid integers. ALL number must be bigger than 0.")

        else:
            break

    if square_size > 1 and alpha > 1 and beta > 1 and recursion_level > 0:
        # initialising turtle and window
        window = turtle.Screen()
        window.setup(width=800, height=800)
        window.screensize(2000, 2000)

        turtle_drawer = turtle.Turtle()
        turtle_drawer.speed(3)

        # draw_figure recursively
        draw_iteration(turtle_drawer, square_size, alpha, beta, recursion_level)

        # close window on click
        window.exitonclick()

