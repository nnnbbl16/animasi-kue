import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Happy Birthday!")
screen.bgcolor("black")

# Create a turtle object for the cake
cake = turtle.Turtle()
cake.speed(3)

# Draw the cake base
cake.penup()
cake.goto(-100, -50)
cake.pendown()
cake.color("chocolate")
cake.begin_fill()
for _ in range(2):
    cake.forward(200)
    cake.left(90)
    cake.forward(100)
    cake.left(90)
cake.end_fill()

# Draw the frosting
cake.penup()
cake.goto(-110, 50)
cake.pendown()
cake.color("white")
cake.begin_fill()
for _ in range(2):
    cake.forward(220)
    cake.left(90)
    cake.forward(20)
    cake.left(90)
cake.end_fill()

# Draw candles
cake.penup()
cake.goto(-60, 70)
cake.pendown()
cake.color("yellow")
for _ in range(3):
    cake.begin_fill()
    cake.forward(10)
    cake.left(90)
    cake.forward(30)
    cake.left(90)
    cake.forward(10)
    cake.left(90)
    cake.forward(30)
    cake.left(90)
    cake.end_fill()
    cake.penup()
    cake.forward(50)
    cake.pendown()

# Write the message
cake.penup()
cake.goto(0, 150)  # Set position to the center
cake.color("white")
cake.write("Happy Birthday!", align="center", font=("Arial", 24, "bold"))
cake.hideturtle()

# Create a new turtle object for the lines and text
lines = turtle.Turtle()
lines.speed(3)
lines.color("white")

# Draw three lines
line_y_positions = [-150, -170, -190]
for y in line_y_positions:
    lines.penup()
    lines.goto(-200, y)
    lines.pendown()
    lines.forward(400)

# Add name above the lines
name = "for???????"
lines.penup()
lines.goto(0, -130)
lines.pendown()
lines.write(name, align="center", font=("Arial", 16, "normal"))

lines.hideturtle()

# Create a new turtle object for the balloons
balloons = turtle.Turtle()
balloons.speed(3)

# Function to draw a balloon
def draw_balloon(x, y, color):
    balloons.penup()
    balloons.goto(x, y)
    balloons.pendown()
    balloons.color(color)
    balloons.begin_fill()
    balloons.circle(20)  # Draw balloon
    balloons.end_fill()
    balloons.right(90)
    balloons.forward(50)  # Draw string
    balloons.left(90)

# Draw balloons
balloon_positions = [(-200, 200), (-150, 220), (150, 200), (200, 220)]
balloon_colors = ["red", "green", "blue", "purple"]

for position, color in zip(balloon_positions, balloon_colors):
    draw_balloon(position[0], position[1], color)

balloons.hideturtle()

# Keep the window open
turtle.done()