from manim import *
class projectkedua(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #Judul
        judul = Title(f'Soal').scale(0.7).set_color(color='#F38181')
        self.add(judul)

        hasil_dari = Text('Nilai dari').scale(0.4)
        soal = MathTex(r' \sqrt{\sqrt[3]{\sqrt[3]{3^5 \times 3^6 \times 3^7}}}', r'=', r'\dots?').scale(0.5)
        grup_soal = VGroup(hasil_dari, soal).arrange(RIGHT).set_color(color='#EAFFD0')
        grup_soal.shift(UP*2)

        self.add(grup_soal)