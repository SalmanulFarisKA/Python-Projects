from manim import *
from colour import Color

# %%manim -qm -v WARNING Trig

class Trig(Scene):
  def construct(self):

    adj = 0.3
    adj2 = 0.7
    adj3 = 0.3
    sc = 0.9
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

    XA = Tex(r"$\times$").scale(sc2)

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

    # triangle updater

    # triangle = VGroup(t, righta)

    t.add_updater(
        lambda mob: mob.become(Polygon(RIGHT + DOWN, RIGHT + UP, LEFT*2 + DOWN).scale(a.get_value()))
    )

    # animation

    self.play(DrawBorderThenFill(t), Write(righta))
    self.play(Write(A), Write(B), Write(C))
    self.play(Write(sideA), Write(sideB), Write(sideC), lag_ratio = 0.4)
    self.wait()
    self.play(sideA.animate.shift(0.5*LEFT+0.2*UP), sideB.animate.shift(0.2*LEFT))
    self.play(Write(XA), Write(aA), Write(XB), Write(aB), Write(XC), Write(aC))
    self.play(a.animate.set_value(1.5), righta.animate.shift(((1.5)*RIGHT+DOWN)*(0.5)))
    self.wait(0.5)
    self.play(a.animate.set_value(3), righta.animate.shift(((1.5)*RIGHT+DOWN)*(1.5)))
    self.wait(0.5)
    self.play(a.animate.set_value(0.7), righta.animate.shift(((1.5)*RIGHT+DOWN)*(-2.3)))
    self.wait(0.5)
    self.play(a.animate.set_value(1), righta.animate.shift(((1.5)*RIGHT+DOWN)*(0.3)))
    self.wait()
