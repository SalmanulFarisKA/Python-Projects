from manim import *
from colour import Color

# %%manim -qm -v WARNING Trig

%%manim -qm -v WARNING Trig

config.frame_width = 16
config.frame_height = 9

config.pixel_width = 1920
config.pixel_height = 1080

class Trig(Scene):
  def construct(self):

    d = 2 # default waiting time
    adj = 0.3 # adjustment
    adj2 = 0.7
    adj3 = 0.3
    sc = 0.9 # scale
    sc2 = 0.7

    # triangle

    t = Polygon(2*RIGHT+1.5*DOWN, 2*LEFT + 1.5*DOWN, 2*RIGHT + 1.5*UP)

    # labels

    ## corners

    A = Tex(r"A").next_to(t, (RIGHT + DOWN) * (adj)).scale(sc)
    
    A.add_updater(
        lambda mob: mob.next_to(t, (RIGHT + DOWN) * (adj))
    )

    B = Tex(r"B").next_to(t, (RIGHT + UP) * (adj)).scale(sc)
    
    B.add_updater(
        lambda mob: mob.next_to(t, (RIGHT + UP) * (adj))
    )

    C = Tex(r"C").next_to(t, (LEFT*2 + DOWN) * (adj)).scale(sc)
    
    C.add_updater(
        lambda mob: mob.next_to(t, (LEFT*2 + DOWN) * (adj))
    )

    ## sides

    sideA = Tex(r"5").shift(0.5*LEFT+0.3*UP).scale(sc2)

    sideB = Tex(r"4").next_to(t, DOWN * (adj2)).scale(sc2)

    sideB.add_updater(
        lambda mob: mob.next_to(t, (DOWN) * (adj2)) 
    )

    sideC = Tex(r"3").next_to(t, RIGHT * (adj2)).scale(sc2)

    sideC.add_updater(
        lambda mob: mob.next_to(t, RIGHT * (adj2))
    )

    ## right angle

    l1 = Line(RIGHT + DOWN, 2 * LEFT + DOWN)
    l2 = Line(RIGHT + DOWN, RIGHT + UP)

    righta = RightAngle(l1, l2, color=RED, length=0.2)

    # value tracker

    a = ValueTracker(1)

    ## side A

    XA =  Tex(r"$\times$").scale(sc2)
    XA.add_updater(
        lambda mob: mob.next_to(sideA).next_to(sideA, RIGHT*(adj3))
    )

    aA = DecimalNumber(
        a.get_value(),
        color = WHITE,
        num_decimal_places = 1,
        show_ellipsis = False
    ).scale(sc2)
    aA.add_updater(
        lambda mob: mob.set_value(a.get_value()).next_to(XA, RIGHT*(adj3))
    )

    aText_a = Tex(r"a").scale(sc2)
    aText_a.add_updater(
        lambda mob: mob.next_to(XA, RIGHT*(adj3))
    )

    ## side B

    XB = Tex(r"$\times$").scale(sc2)

    XB.add_updater(
        lambda mob: mob.next_to(sideB).next_to(sideB, RIGHT*(adj3))
    )

    aB = DecimalNumber(
        a.get_value(),
        color = WHITE,
        num_decimal_places = 1,
        show_ellipsis = False
    ).scale(sc2)

    aB.add_updater(
        lambda mob: mob.set_value(a.get_value()).next_to(XB, RIGHT*(adj3))
    )

    aText_b = Tex(r"a").scale(sc2)
    aText_b.add_updater(
        lambda mob: mob.next_to(XB, RIGHT*(adj3))
    )

    ## side C

    XC = Tex(r"$\times$").scale(sc2)
    XC.add_updater(
        lambda mob: mob.next_to(sideC).next_to(sideC, RIGHT*(adj3))
    )

    aC = DecimalNumber(
        a.get_value(),
        color = WHITE,
        num_decimal_places = 1,
        show_ellipsis = False
    ).scale(sc2)
    aC.add_updater(
        lambda mob: mob.set_value(a.get_value()).next_to(XC, RIGHT*(adj3))
    )

    aText_c = Tex(r"a").scale(sc2)
    aText_c.add_updater(
        lambda mob: mob.next_to(XC, RIGHT*(adj3))
    )

    # triangle updater

    t.add_updater(
        lambda mob: mob.become(Polygon(RIGHT + DOWN, RIGHT + UP, LEFT*2 + DOWN).scale(a.get_value()))
    )

    wholeTriangle = VGroup(t, A, B, C, sideA, sideB, sideC, aA, aB, aC, XA, XB, XC, righta)

    # animation

    self.play(DrawBorderThenFill(t), Write(righta))
    self.play(Write(A), Write(B), Write(C))
    self.play(Write(sideA), Write(sideB), Write(sideC), lag_ratio = 0.4)
    self.wait()
    self.play(sideA.animate.shift(0.5*LEFT+0.2*UP), sideB.animate.shift(0.2*LEFT))
    self.play(Write(XA), Write(aA), Write(XB), Write(aB), Write(XC), Write(aC))
    self.play(a.animate.set_value(1.5), righta.animate.shift(((1.5)*RIGHT+DOWN)*(0.5)))
    self.wait()
    self.play(a.animate.set_value(3), righta.animate.shift(((1.5)*RIGHT+DOWN)*(1.5)))
    self.wait()
    self.play(a.animate.set_value(0.7), righta.animate.shift(((1.5)*RIGHT+DOWN)*(-2.3)))
    self.wait()
    self.play(a.animate.set_value(1), righta.animate.shift(((1.5)*RIGHT+DOWN)*(0.3)))
    self.wait()

    # reset all the updaters on a number and transform them to a

    self.play(sideA.animate.shift(0.3*RIGHT))

    for i in [aA, aB, aC]:
      i.clear_updaters()

    self.play(Transform(aA, aText_a), Transform(aB, aText_b), Transform(aC, aText_c))
    self.wait(d)

    for i in [t, A, B, C, sideA, sideB, sideC, aA, aB, aC, XA, XB, XC, righta]:
      i.clear_updaters()

    self.play(wholeTriangle.animate.shift(LEFT*2))
    self.wait(d)

    AB = Line(DOWN+LEFT, UP+LEFT, color = YELLOW)
    BC = Line(4*LEFT+DOWN, UP+LEFT, color = YELLOW)
    AC = Line(DOWN+LEFT, 4*LEFT+DOWN, color = YELLOW)
    
    self.play(FadeIn(AB))
    self.play(FadeOut(AB))

    self.wait(d)

    self.play(FadeIn(BC))
    self.play(FadeOut(BC))
    
    self.wait(d)

    self.play(FadeIn(AC))
    self.play(FadeOut(AC))

    self.wait(d)

    AB_BC = Tex(r"$\frac{AB}{BC}$")

    self.play(AB_BC.animate.shift(2*RIGHT+2*UP)) #, FadeIn(AB_BC)) # make both happen at the same time
