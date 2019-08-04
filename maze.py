import turtle

#Initialize lists
pos_list = []
stamp_list = []


SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

snake = turtle.clone()

turtle.hideturtle()


def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos) 
    snake_stamp = snake.stamp()
    stamp_list.append(snake_stamp)

