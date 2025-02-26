"""
Transformations: Manim Tutorials
"""

from manim import *

class Transforms(Scene):
    def construct(self):
       
        formula_one = MathTex(
            r"\lim_{\theta \rightarrow a} \frac{ \sin{\theta} }{\theta} = 1",
            color = ORANGE,
            font_size=60
        ).to_edge(LEFT, buff=1)

        formula_two = MathTex(
            r"\lim_{\theta \rightarrow a} \frac{ \tan{\theta} }{\theta} = 1",
            color=ORANGE,
            font_size=60
        ).to_edge(RIGHT, buff=1)

        # <------ Fade To Color ------>
        self.play(
            Write(formula_one)
        )
        self.wait(2)

        self.play(
            FadeToColor(formula_one, color=YELLOW),
            run_time=1.5
        )

        # <------- Replacement Transform ------->
        self.play(
            FadeIn(formula_one)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(formula_one.copy(), formula_two),
            run_time=1.5
        )
        self.wait(2)