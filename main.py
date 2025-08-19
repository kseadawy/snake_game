from turtle import  Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

#initialize screen
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)

def reset():
    snake_game.reset()
    score_board.adjust_score()

is_game_started = True
snake_game = Snake()

screen.onkey(snake_game.right, "Right")
screen.onkey(snake_game.up, "Up")
screen.onkey(snake_game.left, "Left")
screen.onkey(snake_game.down, "Down")

screen.listen()

current_food = Food()
score_board = ScoreBoard()
while is_game_started:
    screen.update()
    snake_game.move()

    if snake_game.head.distance(current_food) < 15:
        current_food.refresh()
        score_board.update_score()
        snake_game.extend()


    if snake_game.head.xcor() > 270 or snake_game.head.xcor() < -280 or snake_game.head.ycor() > 300 or snake_game.head.ycor() < -300:
        score_board.game_over()
        reset()

    for segment in snake_game.segments[1::]:
        if snake_game.head.distance(segment) < 15:
            reset()

screen.exitonclick()