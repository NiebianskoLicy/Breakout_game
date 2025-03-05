from turtle import Turtle

# TODO transport some functions from main to other classes

class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.is_hit = False

    def set_location(self, x, y):
        self.goto(x,y)

    def get_location(self):
        return self.xcor(), self.ycor()

    def remove(self):
        self.hideturtle()

    def hit(self):
        return True



class Wall:
    def __init__(self):
        self.bricks = []
        self.create_wall()
        self.reset()

    def reset(self):
        for brick in self.bricks:
            loc = brick.get_location()
            brick.goto(loc)


    def create_wall(self):
        x = -425
        y = 280
        for b in range(12):
            brick = Brick()
            brick.set_location(x=x,y=y)
            x += 65
            brick.goto(x, y)
            self.bricks.append(brick)

    def hit(self, ball):
        for brick in self.bricks:
            if ball.distance(x=brick.xcor(), y=brick.ycor()) < 20 and ball.ycor() < 280:
                brick.remove()
                return True