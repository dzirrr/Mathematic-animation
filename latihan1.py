from manim import *

class latihan1(Scene):
    def construct(self):

        teks1 = Text("Saya lagi belajar Manim")
        teks1.set_color_by_gradient(RED, BLUE)
        teks2 = Text("Semangatin dong gaes")
        teks2.next_to(teks1, DOWN).set_color(BLUE)
        kotak = SurroundingRectangle(teks1)

        # self.play(Create(teks1), Create(teks2))
        # self.wait()

        kotakin = Square().scale(0.5)
        teks3 = Text("= Saya lagi belajar Manim").next_to(teks1, UP)
        kotakin.next_to(teks3, LEFT)
    
        # self.play(Create(kotakin)) 
        #self.play(Write(teks3))
        #self.play(Write(teks1), run_time=3)
        #self.play(Transform(teks1, teks2), run_time=1)
        #self.wait()

        