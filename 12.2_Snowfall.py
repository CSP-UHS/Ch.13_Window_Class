'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
import arcade
import random


SW = 600
SH = 600
FN = 300

class Flake:
    def __init__(self, x, y, r, dy, c):
        self.x = x      # X spawn coord
        self.y = y      # Y spawn coord
        self.r = r      # Radius
        self.dy = dy    # velocity of y
        self.c = c      # color
        self.noise = arcade.load_sound("laser.mp3")

    def draw_flake(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)    # Draws a "flake"

    def update_flake(self):      # updates # of pixels 60 times per second
        self.y += self.dy       # moves y position * 60 per second

        # Respawn Flakes above window
        if self.y <= -self.r:
            self.x = random.randint(0, SW)
            self.y = random.randint(SH, SH + 100)
            arcade.play_sound(self.noise)


class OogaBooga(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.flake_list = []     # Create list to hold all snowflakes

        # create flakes
        for i in range(FN):
            r = random.randint(1, 3)
            dy = random.randint(-4, -1)
            x = random.randint(0, SW)
            y = random.randint(0, SH)
            c = arcade.color.SNOW

            if i == 1:
                c = arcade.color.RED

            flake = Flake(x, y, r, dy, c)
            self.flake_list.append(flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()

        # Make window
        arcade.draw_rectangle_filled(SW/2, SH/2, 10, SH, arcade.color.RED)
        arcade.draw_rectangle_filled(SW/2, SH/2, SW, 10, arcade.color.RED)

    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()


def main():
    window = OogaBooga(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    main()
