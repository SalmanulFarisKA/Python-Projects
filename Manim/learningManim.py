from manim import *
from colour import Color

# %%manim -qm -v WARNING LaggingGroup

config.background_color = BLACK

config.frame_width = 16
config.frame_height = 9

config.pixel_width = 1920
config.pixel_height = 1080

class LaggingGroup(Scene):
  def construct(self):
    squares = VGroup(*[Square(color=Color(hue=j/20, saturation = 1, 
    luminance = 0.5), fill_opacity = 0.5) 
    for j in range(20)]).arrange_in_grid(4, 5).scale(0.75)
    t = Text("This is how you do animations").shift(UP)
    tex = Tex(r"$\frac{-\hbar}{2m}\frac{\partial \psi}{\partial x} \
    +V \psi = i \hbar \frac{\partial \psi}{\partial t}$").next_to(t, DOWN)

    self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio = 0.2, run_time = 2))
    # Animating an enitre VGroup
    self.wait(0.5)
    self.play(FadeOut(squares))
    self.wait()
    self.play(Write(t), FadeIn(tex), lag_ratio = 0.8, run_time = 2)
    self.wait()

class BasicAnimations(Scene):
  def construct(self):
      polys = VGroup(
          *[RegularPolygon(5, radius = 1, fill_opacity = 0.5,
          color = Color(hue = j/5, saturation = 1, luminance = 0.5)) 
          for j in range(5)]
      ).arrange(RIGHT)
      self.play(DrawBorderThenFill(polys), run_time = 2)
      self.play(
          Rotate(polys[0], PI, rate_func = lambda t: t), # or you can put rate_func = linear
          Rotate(polys[1], PI, rate_func = smooth),
          Rotate(polys[2], PI, rate_func = lambda t: np.sin(t*PI)),
          Rotate(polys[3], PI, rate_func = there_and_back),
          Rotate(polys[4], PI, rate_func = lambda t: 1 - abs(1 - 2*t)),
          run_time = 2
      )
      self.wait()

class SimpleScene(Scene):
  def construct(self):
    plane = NumberPlane(
        x_range=(-8, 8), 
        y_range=(-4.5, 4.5),
        background_line_style = {
            "stroke_color": PINK # How do I change the axis colors to black?
        }
        )
    t = Triangle(color = PURPLE, fill_opacity = 0.5)
    self.add(plane, t)

    Text.set_default(color=BLACK, font_size=100)
    t = Text("Hello World")
    t.move_to([0, 3, 0])
    self.add(t)

    Text.set_default(color=BLACK, font_size = DEFAULT_FONT_SIZE)
    t2 = Text("Goodbye!").next_to(t, DOWN)
    self.add(t2)
    

class Tutorial(Scene):
  def construct(self):
    plane = NumberPlane()
    self.add(plane)

    # next_to method
    red_dot = Dot(color=RED) 
    # since no specific position is mentioned for it, it is centred
    green_dot = Dot(color=GREEN)
    green_dot.next_to(red_dot, RIGHT*3+UP*3) # RIGHT == [1, 0, 0]
    self.add(red_dot, green_dot)

    # shift
    s = Square(color=ORANGE)
    s.shift(2*UP + 4*RIGHT)
    self.add(s)

    # move_to
    c = Circle(color=PURPLE)
    c.move_to([-3, -3, 0])
    self.add(c)

    #align_to
    c2 = Circle(radius = 0.5, color = RED, fill_opacity = 0.5)
    c3 = c2.copy().set_color(YELLOW)
    c4 = c2.copy().set_color(ORANGE)
    c2.align_to(s, UP) # upper border of c2 matches with the upper border of s
    c3.align_to(s, RIGHT)
    c4.align_to(s, UP + RIGHT)
    self.add(c2, c3, c4)

class CriticalPoints(Scene):
  def construct(self):
    c = Circle(color = GREEN, fill_opacity = 0.5)
    self.add(c)

    for d in [(0, 0, 0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
      self.add(Cross(scale_factor = 0.2).move_to(c.get_critical_point(d)))

    s = Square(color=RED, fill_opacity=0.5)
    s.move_to([1, 0, 0], aligned_edge=LEFT)
    self.add(s)

from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
  def construct(self):
    for perc in range(5, 51, 5):
      self.add(Circle(radius=perc*(Percent(X_AXIS))))
      self.add(Square(side_length=2*perc*Percent(Y_AXIS), color=YELLOW))

    d = Dot()
    d.shift(100 * Pixels * RIGHT)
    self.add(d)

class Grouping(Scene):
  def construct (self):
    red_dot = Dot(color=RED)
    green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
    blue_dot = Dot(color=BLUE,).next_to(red_dot, UP)
    dot_group = VGroup(red_dot, green_dot, blue_dot)
    # A group of three MObjects that we can manipulate like a single MObject
    dot_group.to_edge(RIGHT)
    self.add(dot_group)

    # additional methods for grouped MObjects

    circles = VGroup(*[Circle(radius = 0.2) for _ in range(10)])
    # The star unpacks the list as VGroup doesn't accept iterators

    circles.arrange(UP, buff = 0.5) # buffer of 0.5 MUnits
    # Arranges the circles one by one from top to bottom

    self.add(circles)

    stars = VGroup(*[Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
    stars.arrange_in_grid(4, 5, buff = 0.2)

    self.add(stars)
