# ping-pong-game
Game Objective:
The objective of Pong is to score points by successfully hitting the ball past your opponent's paddle.

Features:
Two-Player Gameplay: The game is designed for two players, with each controlling a paddle on opposite sides of the screen.

Player Controls:

Player 1 (left side) controls their paddle using the W (up) and S (down) keys.
Player 2 (right side) controls their paddle using the UP (up) and DOWN (down) arrow keys.
Ball Movement:

The ball moves horizontally across the screen at a constant velocity.
It bounces off the top and bottom walls as well as the paddles when they collide.
Scoring:

When the ball passes beyond one player's paddle and reaches the edge of the screen, the opposing player earns a point.
The score is displayed at the top center of the screen.
Game Over:

The game continues until one player reaches a predetermined score (not implemented in this basic version).
Players can quit the game by closing the window.
Implementation Details:
Graphics: Basic shapes (rectangles for paddles and an ellipse for the ball) are drawn using Pygame's drawing functions.

Collision Detection: Collisions between the ball and the paddles, as well as the ball and the walls, are detected using simple bounding box collision detection.

Scorekeeping: Scores for each player are displayed using Pygame's font rendering functionality.

