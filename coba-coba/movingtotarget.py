from manim import *

class MoveToTarget(Scene):
    def construct(self):

        teks = Text("coba animasiin ini keatas terus keciliin")
        teks.generate_target()
        teks.target.shift(UP*2+LEFT).scale(0.5).set_color(RED)

        
        teks2 = MathTex(r'\sqrt{5}')
        akar5 = MathTex(r'=', r'\sqrt{5}')
        kotak = SurroundingRectangle(teks2)

        self.play(Write(teks2)) 
        self.play(Create(kotak)) 
        self.play(ReplacementTransform(teks2, akar5.next_to(kotak, RIGHT)))
        self.wait()

        # self.add(kotak, teks2.move_to(tengah)) 
        # self.add(akar5.next_to(kotak, RIGHT))

        # self.play(MoveToTarget(teks))
        # self.play(MoveToTarget(teks2))
        # self.wait()