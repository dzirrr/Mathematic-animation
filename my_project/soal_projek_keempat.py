from manim import *
class projectkedua(Scene):
    def construct(self):
        #Judul
        judul = Title(f'Soal UTBK/CPNS').scale(0.5).set_color(color='#F38181')
        self.add(judul)

        soal = MathTex(r'2^{30}+2^{30}+2^{30}+2^{30}=\cdots').scale(0.5)
        soal.shift(UP*2)

        self.add(soal)