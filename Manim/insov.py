# Integral solver that takes input, uses sympy to evaluate it and displays it with manim animation engine

# command:
# python -m manim insov.py Equations -pql

from sympy import *
from manim import *

# Take a function as an input and then make a manim program to write that function and output its indefinite integral. DONE

# A program with GUI that writes the indefinite integral of a function as per what we type in the textbox and outputs the the video
# of the result when we click solve button

init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')

integrand = cos(x)*x**2

definite = True

if not definite:

    integrandLatex = latex(integrand)

    sol = simplify(integrate(integrand))
    solLatex = latex(sol)

    class Equations(Scene):

        def construct(self):

            eq = Tex(f"$\int{integrandLatex}~dx$").scale(2).shift(2*UP+2*LEFT)

            solEq = Tex(f"$={solLatex}$").scale(2).next_to(eq, RIGHT)

            self.wait()
            self.play(Write(eq))
            self.wait()
            self.play(Write(solEq))
            self.wait()

else:

    uppBound = 10
    lowBound = 0

    integrandLatex = latex(integrand)

    sol = simplify(integrate(integrand))
    solLatex = latex(sol)

    uppSol = sol.subs(x, uppBound)
    uppSolLatex = latex(uppSol)
    lowSol = sol.subs(x, lowBound)
    lowSolLatex = latex(lowSol)

    finSol = simplify(uppSol - lowSol)
    finSolLatex = latex(finSol)

    class Equations(Scene):

        def construct(self):

            eqText = "$\int_{"+str(lowBound)+"}^{" + str(uppBound) + \
                "} " + str(integrandLatex) + "~dx$"
            eq = Tex(eqText).shift(2*UP)

            solEqText = ((f"$={str(solLatex)}" + r"\right|_{" +
                         str(lowBound)) + "}^{") + str(uppBound) + "}$"

            solEq = Tex(solEqText).next_to(eq, DOWN)

            subEq = Tex(
                f"$=\left({uppSolLatex}\\right) - \left({lowSolLatex}\\right)$").next_to(solEq, DOWN)

            finEq = Tex(f"$={finSolLatex}$").next_to(subEq, DOWN)

            self.wait()
            self.play(Write(eq))
            self.wait()
            self.play(Write(solEq))
            self.wait()
            self.play(Write(subEq))
            self.wait()
            self.play(Write(finEq))
            self.wait()
