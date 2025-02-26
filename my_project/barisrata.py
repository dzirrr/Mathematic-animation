from manim import *

class latihan1(Scene):
    def construct(self):

        teks1 = MathTex(r"& \sqrt{20} + \sqrt{5}", r"\\&= \sqrt{4}\sqrt{5} + \sqrt{5}" r"\\&= 2\sqrt{5} - \sqrt{5}").scale(0.5)
        teks1.set_color_by_gradient(RED, BLUE)
        teks2 = Text("Semangatin dong gaes").scale(0.3)
        teks2.next_to(teks1, DOWN).set_color(BLUE)
    
        self.play(Write(teks1))
    
        #self.play(Write(teks1), run_time=3)
        #self.play(Transform(teks1, teks2), run_time=1)
        #self.wait()



        