# Angela Yu - Python Day 23
## Turtle Crossing Game

- Turtle Crossing Code Structure
  - Create the screen
    - black screen
    - width 600 pixels and height 600 pixels
    - exit on click
  - Create and move turtle
    - starting x_pos 0 and y_pos -200
    - turtle moves up only (not down, left nor right)
  - Detect when turtle reaches end of screen at top
    - when turtles hits top edge moves back to original position
    - player levels up
    - car speed increases
  - Create and move random cars
    - will move from right to left along y-axis
  - Detect turtle collision with car
    - game over when turtle collides with car
  - Detect when turtle successfully crosses to the other side
  - Create scoreboard
    - Keep score (levels)