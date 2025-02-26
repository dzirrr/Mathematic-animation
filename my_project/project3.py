from manim import *

class Project3(Scene):
    def construct(self):

        #Titik kota
        titik1 = Dot([-1, -3, 0])
        titik2 = Dot([-1, 1, 0])
        titik3 = Dot([1, -3, 0])
        titik4 = Dot([1, -1, 0])
        titik5 = Dot([1, -2, 0])
        #Teks Kota
        k1 = Text('Kota 1').scale(0.3).next_to(titik1, RIGHT)
        k2 = Text('Kota 2').scale(0.3).next_to(titik2, RIGHT)
        k3 = Text('Kota 3').scale(0.3).next_to(titik3, RIGHT)  
        k4 = Text('Kota 4').scale(0.3).next_to(titik4, RIGHT)
        k5 = Text('Kota 5').scale(0.3).next_to(titik5, RIGHT)
        #Kota
        kota1 = VGroup(titik1, k1)
        kota2 = VGroup(titik2, k2)
        kota3 = VGroup(titik3, k3)
        kota4 = VGroup(titik4, k4)
        kota5 = VGroup(titik5, k5)
        
        #Garis kota
        kota_1ke2 = Line(titik1.get_center(), titik2.get_center()).set_color(ORANGE)
        kota_3ke4 = Line(titik3.get_center(), titik4.get_center()).set_color(ORANGE)
        
        #Teks 1
        teks1 = Text("Jika antara kota 1 dan 2 adalah \n dua kali antara kota 3 dan 4", t2c={"dua kali antara kota 3 dan 4":YELLOW})
        teks1.scale(0.3).shift(UP*2.5)
        self.play(Write(teks1))
        #Animasi kota 3 ke 4
        self.play(Create(titik3), Create(k3))
        self.play(Create(titik4), Create(k4))
        self.play(Create(kota_3ke4))
        #Animasi kota 1 dan 2 2x kota 3 dan 4
        garis_kota_3ke4 = VGroup(k3, kota3, k4, kota4,  kota_3ke4)
        kota2_2x_kota_3ke4 = VGroup(k1, kota1, k2, kota2, kota_1ke2)
        self.play(Transform(garis_kota_3ke4.copy(), kota2_2x_kota_3ke4), run_time=2)

        #Animasi kota 5
        self.play(Create(titik5), Create(k5), run_time=1.5)
        self.wait()
        #Teks 2
        teks2 = Text("Kota 5 terletak di tengah-tengah \n antara kota 3 dan 4.", t2c={"di tengah-tengah antara kota 3 dan 4":YELLOW})
        teks2.scale(0.3).shift(UP*2.5)
        self.play(FadeOut(teks1), run_time=0.5)
        self.play(Write(teks2))
        #Animasi kota 5 pindah ke garis 1 dan 2
        self.play(kota5.animate.shift(LEFT*2+UP))

        #Brace
        dot5 = Dot([-1, -1, 0])
        dot_3ke1 = Dot([-1, -2, 0])
        dot_4ke5 = Dot([-1, 0, 0])
        ket_5ke1 = BraceBetweenPoints(titik1, dot5, direction=LEFT).set_color(YELLOW)
        ket_3ke1 = BraceBetweenPoints(titik1, dot_3ke1, direction=LEFT).set_color(YELLOW)
        ket_4ke5 = BraceBetweenPoints(dot_4ke5, titik2, direction=LEFT).set_color(YELLOW)
        #Teks 3
        teks3 = Text('Lalu diketahui juga bahwa kota 3 ke kota 1 \n sama dengan jarak kota 4 ke kota 2,', t2c={"kota 3 ke kota 1 sama dengan jarak kota 4 ke kota 2":YELLOW})
        teks3.scale(0.3).shift(UP*2.5)
        self.play(FadeOut(teks2), run_time=0.5)
        self.play(Write(teks3))

        #Teks 4 
        teks4 = Text('yakni setengah jarak kota 1 dan kota 5', color=YELLOW)
        teks4.scale(0.3).next_to(teks3, DOWN)
        self.play(Write(teks4))
        #Animasi brace
        self.play(Create(ket_5ke1))
        self.wait()
        self.play(Transform(ket_5ke1, ket_3ke1))
        self.wait()
        self.play(Transform(ket_3ke1, ket_4ke5))
        self.wait()
        #Kota 345
        kota_345 = VGroup(kota3, kota4, kota_3ke4)
        self.play(kota_345.animate.shift(LEFT*2+UP))
        self.wait()
        #Lepas brace
        self.remove(ket_5ke1, ket_3ke1, ket_4ke5)

        self.play(FadeOut(teks3), FadeOut(teks4), run_time=0.5)
        teks5 = Text('Jadi dua kota yang jaraknya paling jauh \n adalah Kota 1 ke Kota 2')
        teks5.scale(0.3).shift(UP*2.5)
        self.play(Write(teks5))
        self.play(Indicate(kota1))
        self.play(Indicate(kota2))
        self.wait(2)