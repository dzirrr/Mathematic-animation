from manim import *

class SoalAkar5(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #Tulis Soal
        soal = MathTex(r"\sqrt{20}", r"-", r"\sqrt{5}", r"= \dots ?").scale(0.5).shift(UP)
        #Teks
        teks1 = Text('Bagaimana menyelesaikan soal tersebut?', font_size=27, color=RED).scale(0.5).shift(UP*3)
        teks2 = Text('Kotakin aja boy!', color=RED, font_size=30).scale(0.7).shift(UP*3)
        
        #Animasi Soal
        self.play(Write(soal))
        self.wait(2)
        #Animasi Teks
        self.play(Write(teks1), run_time=1)
        self.play(FadeOut(teks1))
        self.wait(0.5)
        self.play(GrowFromCenter(teks2))
       
        # Misalkan Kotak
        misal = MathTex('Misalkan', r'\rightarrow', color=TEAL).scale(0.5).shift(LEFT*1.2+UP*1.8)
        akar5 = MathTex(r'\sqrt{5}').scale(0.5)
        kotak = SurroundingRectangle(akar5, buff=0.1)
        kotak.next_to(misal, RIGHT)
        akar = MathTex(r"=", r"\sqrt{5}").scale(0.5)
        hapus = VGroup(misal, akar5, akar, kotak)
        #Animasi Misalkan
        self.play(Write(misal)) 
        self.play(Write(akar5.next_to(misal, RIGHT)))
        self.play(Write(kotak))
        self.play(ReplacementTransform(akar5.next_to(misal, RIGHT), akar.next_to(kotak, RIGHT)))
        self.wait()

        #Simplifikasi
        s1 = MathTex(r"=\sqrt{4}\sqrt{5}", r"-", r"\sqrt{5}").next_to(soal, DOWN).scale(0.5)
        s1a = MathTex(r"=\sqrt{4}", r"\sqrt{5}", r"-", r"\sqrt{5}").next_to(soal, DOWN).scale(0.5)
        #Perkotakan
        kotak_s1a1 = SurroundingRectangle(s1a[1], buff=0)
        kotak_s1a2 = SurroundingRectangle(s1a[3], buff=0)
         
        #Animasi Simplifikasi
        self.play(Transform(soal[0].copy(), s1[0]))
        self.play(Transform(soal[1].copy(), s1[1]))
        self.play(Transform(soal[2].copy(), s1[2]))
        self.wait()
        self.play(Create(kotak_s1a1))
        self.play(Create(kotak_s1a2))

        #akar 4 kotak
        akar4 = MathTex(r"=\sqrt{4}").scale(0.5).next_to(s1, DOWN).shift(LEFT*0.5)
        kotak_1a = SurroundingRectangle(s1a[1], buff=0).next_to(akar4, buff=0.1)
        min = MathTex(r'-').scale(0.5).next_to(kotak_1a, buff=0.1)
        kotak_1b = SurroundingRectangle(s1a[3], buff=0).next_to(min, buff=0.1)
        grup1 = VGroup(akar4, kotak_1a, min, kotak_1b)
        #akar 2 kotak
        akar2 = MathTex(r"= 2").scale(0.5).next_to(akar4, DOWN).shift(LEFT*0.001)
        kotak_2a = SurroundingRectangle(s1a[1], buff=0).next_to(akar2, buff=0.1)
        min2 = MathTex(r'-').scale(0.5).next_to(kotak_2a, buff=0.1)
        kotak_2b = SurroundingRectangle(s1a[3], buff=0).next_to(min2, buff=0.1)
        grup2 = VGroup(akar2, kotak_2a, min2, kotak_2b)


        #Animasi akar 4
        self.play(Transform(s1a[0], akar4), run_time=1.5)
        self.play(Transform(kotak_s1a1, kotak_1a))
        self.play(Transform(s1a[2], min))
        self.play(Transform(kotak_s1a2, kotak_1b))
        #Animasi akar2
        self.play(Transform(akar4, akar2))
        self.play(Transform(kotak_1a.copy(), kotak_2a))
        self.play(Transform(min.copy(), min2))
        self.play(Transform(kotak_1b.copy(), kotak_2b))
        self.wait()

        #hasil
        sama = MathTex(r'=').scale(0.5).next_to(grup2, DOWN).shift(LEFT*0.5)
        kotak_3 = SurroundingRectangle(s1a[1], buff=0).next_to(grup2, DOWN, buff=0.1)
        grup3 = VGroup(sama, kotak_3).next_to(grup2, DOWN).shift(LEFT*0.3)
        hasil = MathTex(r"=\sqrt{5}").scale(0.5).next_to(grup2, DOWN).shift(LEFT*0.3)

        #Animasi Hasil
        self.play(ReplacementTransform(grup2, grup3))
        self.remove(grup3)
        self.play(Transform(grup3, hasil))
        self.play(Indicate(hasil))
        self.play(self.camera.frame.animate.scale(0.2).move_to(hasil))
        self.wait()
        self.play(Restore(self.camera.frame))

        #Hasil akhir
        jadi = MathTex(r"\sqrt{20}", r"-", r"\sqrt{5}", r"= \sqrt{5}").scale(0.5).shift(UP)
        self.play(TransformMatchingTex(Group(hasil, soal), jadi), run_time=1.5)
        self.play(jadi.animate.scale(2))
        self.play(self.camera.frame.animate.scale(1).move_to(jadi))
        

        self.wait(2)

        
        
        
       


        
        