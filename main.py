from manim import *

class Test(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=GREEN, fill_color=PINK,fill_opacity=.75)
        self.play(Create(sq), run_time = 3)
        self.wait()
