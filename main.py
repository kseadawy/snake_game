from turtle import  Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


#initialize screen
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)


is_game_started = True
snake = Snake()

screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.listen()

current_food = Food()
score_board = ScoreBoard()
while is_game_started:
    screen.update()
    snake.move()

    if snake.head.distance(current_food) < 15:
        current_food.refresh()
        score_board.increment_score()
        snake.extend()


    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.game_over()
        is_game_started = False

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 15:
            is_game_started = False
            score_board.game_over()

screen.exitonclick()