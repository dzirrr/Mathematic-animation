from manim import *
class projectkedua(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #Judul
        judul = Title(f'Solusi').scale(0.7).set_color(color='#F38181')
        self.add(judul)

        #Tulis soal
        hasil_dari = Text('Nilai dari').scale(0.4)
        soal = MathTex(r' \sqrt{\sqrt[3]{\sqrt[3]{3^5 \times 3^6 \times 3^7}}}', r'=', r'\dots?').scale(0.5)
        grup_soal = VGroup(hasil_dari, soal).arrange(RIGHT).set_color(color='#EAFFD0')
        grup_soal.shift(UP*2)
        #Animasi soal
        self.play(Write(grup_soal))
        self.wait(2)

        #Ingat
        ingat = Text('Ingat:').scale(0.3).set_color(color='#FCE38A')
        igt1 = MathTex('\\sqrt[n]{x} = x^{\\frac{1}{n}}').scale(0.5).next_to(ingat, DOWN, buff=0.1).set_color(color='#FCE38A')
        igt2 = MathTex('x^n \\times x^m = x^{n+m}').scale(0.5).next_to(igt1, DOWN, buff=0.1).set_color(color='#FCE38A')
        igt3 = MathTex('(x^n)^m = x^{n \\times m}').scale(0.5).next_to(igt2, DOWN, buff=0.1).set_color(color='#FCE38A')
        grup_ingat = VGroup(ingat, igt1, igt2, igt3)
        grup_ingat.shift(UP*1.2+LEFT*1.2)
        #Animasi ingat
        self.play(Write(ingat))
        self.play(Write(igt1))
        self.wait()
        self.play(Write(igt2))
        self.wait()
        self.play(Write(igt3))
        self.wait()

        #Jawab
        jawab = Text('Jawab:').scale(0.3).next_to(igt3, DOWN).set_color(color='#EAFFD0')
        # self.play(DrawBorderThenFill(jawab))
        

        #Langkah penyelesaian
        l = MathTex(r' \sqrt{ \sqrt[3]{\sqrt[3]{3^5 \times 3^6 \times 3^7}}}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l1 = MathTex(r'\left( \sqrt[3]{\sqrt[3]{3^5 \times 3^6 \times 3^7}} \right)^\frac{1}{2}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l2 = MathTex(r'\left( \left(\sqrt[3]{3^5 \times 3^6 \times 3^7} \right)^\frac{1}{3} \right)^\frac{1}{2}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l3 = MathTex(r'\left(\left(\left(3^5 \times 3^6 \times 3^7 \right)^\frac{1}{3} \right)^\frac{1}{3} \right)^\frac{1}{2}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l4 = MathTex(r'\left(\left(\left(3^{5+6+7} \right)^\frac{1}{3} \right)^\frac{1}{3} \right)^\frac{1}{2}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l5 = MathTex(r'\left(\left(\left(3^{18} \right)^\frac{1}{3} \right)^\frac{1}{3} \right)^\frac{1}{2}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l6 = MathTex(r'\left(\left(3^{18} \right)^\frac{1}{3} \right)^\frac{1}{6}\\').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l7 = MathTex(r'\left(3^{18} \right)^\frac{1}{18}\\').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l8 = MathTex(r'3^{\frac{18}{18}}').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l9 = MathTex(r'3^1').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')
        l10 = MathTex(r'3').scale(0.5).shift(DOWN).set_color(color='#EAFFD0')

        self.play(ReplacementTransform(soal[0].copy(), l), run_time=1.5)
        self.wait()
        self.play(self.camera.frame.animate.scale(0.8).move_to(l))
        self.remove(l)
        self.play(Transform(l, l1))
        self.wait()
        self.remove(l, l1)
        self.play(Transform(l1, l2))
        self.wait()
        self.remove(l, l1, l2)
        self.play(Transform(l2, l3))
        self.wait()
        self.remove(l, l1, l2, l3)
        self.play(Transform(l3, l4))
        self.wait()
        self.remove(l, l1, l2, l3, l4)
        self.play(Transform(l4, l5))
        self.wait()
        self.remove(l, l1, l2, l3, l4, l5)
        self.play(Transform(l5, l6))
        self.wait()
        self.remove(l, l1, l2, l3, l4, l5, l6)
        self.play(Transform(l6, l7))
        self.wait()
        self.remove(l, l1, l2, l3, l4, l5, l6, l7)
        self.play(Transform(l7, l8))
        self.wait()
        self.remove(l, l1, l2, l3, l4, l5, l6, l7, l8)
        self.play(Transform(l8, l9))
        self.remove(l, l1, l2, l3, l4, l5, l6, l7, l8, l9)
        self.play(Transform(l9, l10))
        self.play(Restore(self.camera.frame))
        self.play(Indicate(l10))
        self.wait()

        #Hasil akhir
        self.add(grup_soal)
        jadi = MathTex(r' \sqrt{\sqrt[3]{\sqrt[3]{3^5 \times 3^6 \times 3^7}}}', r'=3').scale(0.5).next_to(hasil_dari, RIGHT)
        self.remove(soal)
        self.play(ReplacementTransform(Group(l10, soal), jadi))
        self.wait()
        self.remove(jawab, soal, ingat, igt1, igt2, igt3, jadi, hasil_dari)
        self.play(jadi.animate.shift(DOWN+LEFT).scale(1.5))
        
        self.wait()