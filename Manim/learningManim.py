from manim import *
from colour import Color

# %%manim -qm -v WARNING LaggingGroup

# config.background_color = WHITE

config.frame_width = 16
config.frame_height = 9

config.pixel_width = 1920
config.pixel_height = 1080

class ValueTrackerPlot(Scene):
  def construct(self):
    a = ValueTracker(1)
    a.save_state()

    ax = Axes(x_range = [-2, 2, 1], y_range = [-8.5, 8.5, 1], x_length = 4, y_length = 6)
    parabola = ax.plot(lambda x: x**2, color = RED)
    parabola.add_updater(
        lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color = RED))
    )
    a_number = DecimalNumber(
        a.get_value(),
        color = WHITE,
        num_decimal_places = 1,
        show_ellipsis = False
    )
    a_number.add_updater(
        lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
    )
    self.add(ax, parabola, a_number)
    self.play(a.animate.set_value(2))
    self.play(a.animate.set_value(-2))
    self.play(Restore(a), run_time = 2)

class AllUpdaterTypes(Scene):
  def construct(self):
    red_dot = Dot(color = RED).shift(LEFT)
    pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
    pointer.add_updater( # place arrow left of dot
        lambda mob: mob.next_to(red_dot, LEFT)
    )

    def shifter(mob, dt): # make dot move 2 units RIGHT/sec
      mob.shift(2+dt*RIGHT)
    red_dot.add_updater(shifter)

    def scene_scaler(dt): # scale objects depensing on distance to ORIGIN
      for mob in self.mobjects:
        mob.set(width = 2/(1 + np.linalg.norm(mob.get_center)))
    self.add_updater(scene_scaler)

    self.add(red_dot, pointer)
    self.update_self(0)
    self.wait(5)

class Disperse(Animation): # We inherit from the animation instead of the scene
  def __init__(self, mobject, dot_radius = 0.05, dot_number = 100, **kwargs):
    super().__init__(mobject, **kwargs) # calls the initialisation of the parent 
    # what is super()?
    self.dot_radius = dot_radius
    self.dot_number = dot_number

  def begin(self):
    dots = VGroup(
        *[Dot(radius = self.dot_radius).move_to(self.mobject.point_from_proportion(p)) 
        for p in np.linspace(0, 1, self.dot_number)]
    ) # Adding dots

    for dot in dots: 
      # assigning a custom attribute to every dot to tell it where to move
      dot.initial_position = dot.get_center()
      dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())

    dots.set_opacity(0)
    self.mobject.add(dots) 
    # setting the dots group as a child of the original mobject
    self.dots = dots 
    # saving this dots group as an attribute of the animation

    super().begin()

  def clean_up_from_scene(self, scene: "Scene") -> None:
    # overwriting the clean_up_from_scene method (?)
    super().clean_up_from_scene(scene)
    scene.remove(self.dots)

  def interpolate_mobject(self, alpha): 
    # overwriting the interpolate_mobject method
    # fade out the original mobject but at the same time fade in the dots

    # when you overwrite the interpolate_mobject method, you have to write the
    # rate function yourself

    alpha = self.rate_func(alpha) # getting the rate_func from the parent class

    if alpha <= 0.5: # first half of the animation
      self.mobject.set_opacity(1 - 2*alpha, family = False) 
      # when alpha = 0.5, opacity = 0
      # family = False sets the opacity only for the mobject itself and not the child
      self.dots.set_opacity(2*alpha) # dots increase in opacity

    else:
      self.mobject.set_opacity(0) 
      # the object is faded out in the second half of the animation so opacity = 0
      self.dots.set_opacity(2*(1 - alpha))
      # the dots decrease in opacity

      for dot in self.dots:
        dot.move_to(dot.initial_position + 2*(alpha - 0.5)*dot.shift_vector)
        # dots move from their initial position to direction of shift vector
        # the size of shift vector increases with alpha and is 1 at alpha = 1

class CustomAnimationExample(Scene):
  def construct(self):
    st = Star(color = YELLOW, fill_opacity = 1).scale(3)
    self.add(st)
    self.wait()
    self.play(Disperse(st, dot_number = 100, run_time = 4))

class SimpleCustomAnimation(Scene):
  def construct(self):
    def spiral_out(mobject, t): # defining the animation
      radius = 4*t    
      angle = 2*t * 2*PI
      mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
      mobject.set_color(Color(hue = t, saturation = 1, luminance = 0.5))
      mobject.set_opacity(1-t)

    d = Dot(color = WHITE)
    self.add(d)
    self.play(UpdateFromAlphaFunc(d, spiral_out, run_time = 3))

class AnimationMechanisms(Scene):
  def construct(self):
    c = Circle()

    c.generate_target()
    c.target.set_fill(color = GREEN, opacity = 0.5)
    c.target.shift(2*RIGHT + UP).scale(0.5) # setting properties of target

    self.add(c)
    self.wait()
    self.play(MoveToTarget(c)) 
    # setting everything first and then executing it as opposed to animate which
    # does everything after c.animate.[transformation]

    s = Square()
    s.save_state() # will return to this state
    self.play(FadeIn(s))
    self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
    self.play(s.animate.shift(5*DOWN).rotate(PI/4))
    self.wait()
    self.play(Restore(s), run_time = 2)

class AnimateSyntax(Scene):
  def construct(self):
    s = Square(color = GREEN, fill_opacity = 0.5)
    c = Circle(color = RED, fill_opacity = 0.5)
    self.add(s, c)

    self.play(s.animate.shift(UP), c.animate.shift(DOWN))
    self.play(VGroup(s,c).animate.arrange(RIGHT, buff = 1))
    self.play(c.animate(rate_func = lambda x: (np.sin(x*PI/2))**3).shift(RIGHT).scale(2))
    # animate is kinda like a general version of Rotate, it is bad at rotation but it 
    # is good at general animations. Its syntax is c.animate.[transformation at the end
    # state] as opposed to Rotate(c)
     
    self.wait()

class LaggingGroup(Scene):
  def construct(self):
    squares = VGroup(*[Square(color=Color(hue=j/20, saturation = 1, 
    luminance = 0.5), fill_opacity = 0.5) 
    for j in range(20)]).arrange_in_grid(4, 5).scale(0.75)
    t = Tex(r"\text{This is how you do animations}").shift(UP)
    tex = Tex(r"$\frac{-\hbar}{2m}\frac{\partial \psi}{\partial x} \
    +V \psi = i \hbar \frac{\partial \psi}{\partial t}$").next_to(t, DOWN)

    self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio = 0.2, run_time = 2))
    # Animating an enitre VGroup
    self.wait(2)
    self.play(FadeOut(squares))
    self.wait()
    self.play(Write(t), Write(tex), lag_ratio = 0.9, run_time = 2)
    self.wait(3)

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
