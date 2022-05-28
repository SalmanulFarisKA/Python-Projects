from manim import *

%manim -qm -v WARNING ManimAnim

class ManimAnim(Scene):
    def construct(self):

        # Define parameters

        x_min = -4
        x_max = 4
        x_step = 1

        y_min = -1
        y_max = 16
        y_step = 2

        # Create objects

        axes = NumberPlane(
            x_range=[
                x_min-1,
                x_max+1,
                x_step
            ],
            y_range=[
                y_min,
                y_max,
                y_step
            ],
            axis_config={
                "include_numbers": True,
                "include_tip": True
            },
            x_axis_config={
                "unit_size": 1,
                "numbers_to_exclude": [x_min-1, x_max+1]
            },
            y_axis_config={
                "unit_size": 1/y_step,
                "numbers_to_exclude": [y_max]
            }
        )

        axes.height = config.frame_height - 1

        func =  lambda x: x ** 2  # creating the graph with the axis object

        left_plot = axes.plot(func, x_range=[x_min, 0])
        right_plot = axes.plot(func, x_range=[0, x_max])

        left_plot.reverse_points()
        # as the plot comes from l to r instead of r to l

        func_tex = MathTex("f(x)=x^2")\
            .align_to(axes, UP).shift(LEFT*1.5)

        self.add(
            axes, left_plot, right_plot, func_tex
        )

        self.play(Write(axes), run_time=3)
        self.wait()
        self.play(
            Create(left_plot),
            Create(right_plot),
            run_time=3
        )
        self.wait()
        self.play(Write(func_tex))
        self.wait()
