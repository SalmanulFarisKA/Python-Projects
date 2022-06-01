from manim import *
from colour import Color

# %%manim -qm -v WARNING Trig

config.frame_width = 16
config.frame_height = 9

config.pixel_width = 1920
config.pixel_height = 1080

class Trig(Scene):
  def construct(self):

    adj = 0.3

    # triangle

    t = Polygon(RIGHT + DOWN, RIGHT + UP, LEFT*2 + DOWN)

    # labels

    A = Tex(r"A").next_to(t, (RIGHT + DOWN) * (adj)).scale(0.9)
    
    A.add_updater(
        lambda mob: mob.next_to(t, (RIGHT + DOWN) * (adj))
    )

    B = Tex(r"B").next_to(t, (RIGHT + UP) * (adj)).scale(0.9)
    
    B.add_updater(
        lambda mob: mob.next_to(t, (RIGHT + UP) * (adj))
    )

    C = Tex(r"C").next_to(t, (LEFT*2 + DOWN) * (adj)).scale(0.9)
    
    C.add_updater(
        lambda mob: mob.next_to(t, (LEFT*2 + DOWN) * (adj))
    )

    # right angle

    l1 = Line(RIGHT + DOWN, 2 * LEFT + DOWN)
    l2 = Line(RIGHT + DOWN, RIGHT + UP)

    righta = RightAngle(l1, l2, color=RED, length=0.2)
    

    self.play(DrawBorderThenFill(t), Write(righta))
    self.play(Write(A), Write(B), Write(C))
