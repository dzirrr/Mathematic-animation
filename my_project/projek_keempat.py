from manim import *

class Projek_keempat(Scene):
    def construct(self):
        #Tulis Soal
        soal = MathTex(r"2^{30}+2^{30}+2^{30}+2^{30}=\cdots ?").scale(0.5).shift(UP)
        #Teks
        teks1 = Text('Bagaimana menyelesaikan soal tersebut?', font_size=27, color=RED).scale(0.5).shift(UP*3)
        teks2 = Text('Kotakin aja boy!', color=RED, font_size=30).scale(0.7).shift(UP*3)
        
        #Animasi Soal
        self.play(Write(soal))
        self.wait(2)
        #Animasi Teks
        self.play(Write(teks1), run_time=1)
        self.play(FadeOut(teks1))
        self.play(GrowFromCenter(teks2))
        self.wait()
       
        # Misalkan Kotak
        misal = MathTex('Misalkan', r'\rightarrow', color=TEAL).scale(0.5).shift(LEFT*1.2+UP*1.8)
        duapuluh = MathTex(r'2^{30}').scale(0.5)
        kotak_misalkan = SurroundingRectangle(duapuluh, buff=0.1)
        kotak_misalkan.next_to(misal, RIGHT)
        duapangkattigatiga = MathTex(r"=", r"2^{30}").scale(0.5)

        #Animasi Misalkan
        self.play(Write(misal)) 
        self.play(Write(duapuluh.next_to(misal, RIGHT)))
        self.play(Write(kotak_misalkan))
        self.play(ReplacementTransform(duapuluh.next_to(misal, RIGHT), duapangkattigatiga.next_to(kotak_misalkan, RIGHT)))
        self.wait()

        #Langkah 1
        langkah1 = MathTex(r"=2^{30}+2^{30}+2^{30}+2^{30}").next_to(soal, DOWN).scale(0.5)
        langkah1b = MathTex(r"=", r"2^{30}", r"+", r"2^{30}", r"+", r"2^{30}", r"+", r"2^{30}").next_to(soal, DOWN).scale(0.5)
        #Perkotakan
        kotak1 = SurroundingRectangle(langkah1b[1], buff=0)
        kotak2 = SurroundingRectangle(langkah1b[3], buff=0)
        kotak3 = SurroundingRectangle(langkah1b[5], buff=0)
        kotak4 = SurroundingRectangle(langkah1b[7], buff=0)
    
        #Animasi Langkah 1
        self.play(Transform(soal.copy(), langkah1))
        self.wait()
        self.play(Create(kotak1), run_time=0.5)
        self.play(Create(kotak2), run_time=0.5)
        self.play(Create(kotak3), run_time=0.5)
        self.play(Create(kotak4), run_time=0.5)
        self.wait()

        #Langkah 2
        kotak = VGroup(kotak1, kotak2, kotak3, kotak4)
        empat = MathTex(r"=4").next_to(langkah1, DOWN).scale(0.5).shift(LEFT*1)
        kotak_langkah2 = SurroundingRectangle(langkah1b[1], buff=0).next_to(empat, buff=0.1)
        langkah2 = VGroup(empat, kotak_langkah2)
        
        #Animasi langkah 2
        self.play(Transform(kotak, langkah2), run_time=1.5)
        self.wait()
    
        #Langkah 3
        dua_pangkat_dua = MathTex(r"=2^2 \times").next_to(langkah2, DOWN).scale(0.5)
        dua_pangkat_tigapuluh = MathTex(r" 2^{30}").next_to(dua_pangkat_dua, buff=0).scale(0.5)
        langkah3 = VGroup(dua_pangkat_dua, dua_pangkat_tigapuluh)

        #Animasi langkah 3
        self.play(Transform(langkah2, langkah3))
        self.wait()

        #Langkah 4
        dua_pangkat_tigatiga = MathTex(r"= 2^{32}").next_to(langkah3, DOWN).scale(0.5).shift(LEFT*0.1)
        self.play(Transform(langkah3, dua_pangkat_tigatiga))
        self.play(Indicate(dua_pangkat_tigatiga))
        self.wait()

        #Hasil akhir
        self.remove(teks1)
        self.remove(teks2)
        self.remove(misal)
        self.remove(duapuluh)
        self.remove(kotak_misalkan)
        self.remove(duapangkattigatiga)
        jadi = MathTex(r"2^{30}+2^{30}+2^{30}+2^{30}=2^{32}").scale(0.5).shift(UP)
        self.play(TransformMatchingTex(Group(dua_pangkat_tigatiga, soal), jadi), run_time=1.5)
        self.play(jadi.animate.scale(1.5))
      

        self.wait(2)
