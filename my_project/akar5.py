from manim import *

class SoalAkar5(Scene):
    def construct(self):
    
        soal = MathTex(r"\sqrt{20} - \sqrt{5} = \dots ?").scale(.5).shift(UP)
        jadi = MathTex(r"\sqrt{20} - \sqrt{5} = \sqrt{5}").scale(.5).shift(UP)

        ingat = MathTex(r"ingat", r"\rightarrow", r"\sqrt{20} = \sqrt{4}\sqrt{5} = 2\sqrt{5}")
        ingat.set_color(RED).scale(.5).to_corner(UL, buff=.2)

        simp = MathTex(r"\sqrt{4}\sqrt{5} - \sqrt{5}")
        simp.next_to(soal, DOWN, buff=0.5).scale(.5)
        simp2 = MathTex(r"2\sqrt{5} - \sqrt{5}")
        simp2.next_to(simp, DOWN, buff=0.5).scale(.5)
        
        
        hasil = MathTex(r"= \sqrt{5}")
        hasil.next_to(simp2, DOWN, buff=0.5).scale(.5)

        self.add(soal, simp, ingat, simp2)

        self.play(Write(soal), run_time=2)
        self.wait(2)
        self.play(Create(ingat), run_time=1)
        self.wait(1)
        self.play(Transform(ingat.copy(), simp), run_time=1.5)
        self.wait(1)
        self.play(ReplacementTransform(simp .copy(), simp2), run_time=1.5) 
        self.play(ReplacementTransform(simp2.copy(), hasil), run_time=1.5) 
        self.play(Indicate(hasil))
        self.remove(soal)
        self.play(ReplacementTransform(hasil.copy(), jadi), run_time=1) 
        self.wait(3)