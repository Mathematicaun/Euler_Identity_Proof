from manim import *
class EULER_IDENTITY(Scene):

    def construct(self):

        logo = ImageMobject(
            r'C:\Users\azahr\OneDrive\Documents\Files\Picturs\logo.png'
        ).shift(11.7*UP + 6.2*RIGHT).scale(.2).set_opacity(.9)

        background = ImageMobject(
            r'C:\Users\azahr\OneDrive\Documents\Files\Picturs\Leonhard_Euler.jpg')
        background.set_width(self.camera.frame_width)
        background.set_height(self.camera.frame_height)
        background.set_opacity(.25)
        self.camera.background_color='#131315'
        self.add(logo)

        title = MathTex(
            r'\textit{\textbf{Euler\'s Identity}}',
            font_size=160
        ).to_edge(UP, buff=-3)

        equation = MathTex(
            r'(E_{\mu}):',
            r'e',
            r'^{',
            r'i\pi',
            r'}',
            r'+1',
            r'=',
            r'0',
            font_size=150
        ).next_to(title, DOWN, buff=3)
        equation[3][0].set_color(YELLOW)
        equation[3][1].set_color(BLUE)

        let_proof = MathTex(
            r'\textit{Let\'s  Proof it}',
            font_size=100,
            fill_color=RED
        ).next_to(equation, DOWN, buff=4)

        box0 = SurroundingRectangle(equation[1], buff=.1, color='#FF6029')
        box1 = SurroundingRectangle(equation[3], buff=.1, color='#FF6029')
        box2 = SurroundingRectangle(equation[5], buff=.1, color='#FF6029')
        box3 = SurroundingRectangle(equation[6], buff=.1, color='#FF6029')
        box4 = SurroundingRectangle(equation[7], buff=.1, color='#FF6029')

        self.wait(.5)
        self.play(
                AnimationGroup(
                    FadeIn(
                        background,
                        run_time=1.5
                    ),
                    AnimationGroup(
                        Write(
                            title,
                            run_time=1.5
                        ),
                        Write(
                            equation,
                            run_time=1.5,
                        ),
                        lag_ratio=1.5
                    ),
                    lag_ratio=.5,
                )
        )

        self.wait()

        self.play(
            ReplacementTransform(box0, box1)
            )
        self.play(
            ReplacementTransform(box1, box2)
            )
        self.play(
            ReplacementTransform(box2, box3)
            )
        self.play(
            ReplacementTransform(box3, box4)
            )
        self.play(
            FadeOut(
                box4
            )
        )

        self.play(
            Write(
                let_proof
            )
        )

        self.wait(2)

        self.play(
            Write(
                let_proof,
                rate_func=lambda t: 1-t
            )
        )

        self.play(
            AnimationGroup(
                FadeOut(
                    title,
                    run_time=.3
                ),
                FadeOut(
                    equation,
                    run_time=.3
                ),
                FadeOut(
                    background,
                    run_time=.3
                ),
                run_time=.2,
                rate_func=smooth,
                lag_ratio=0
            )
        )

        proof = MathTex(
                r'\textit{\textbf{Proof}}',
                font_size=90,
        ).to_edge(UP, buff=-8)

        using_tylor_formulas1 = MathTex(
            r'e^x', r'\text{ Using }', r'Taylor Series',
            font_size=100
        ).next_to(proof, DOWN, buff=1.5)

        using_tylor_formulas1[0][1].set_color(RED)
        using_tylor_formulas1[2].set_color(GREEN)

        exp = MathTex(
            r'e^{x}',
            r'=\sum_{n\in\mathbb{N}}\frac{x^{n}}{n!}',
            '=',
            r'1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+...',
            font_size=80
        ).next_to(using_tylor_formulas1, DOWN, buff=2)

        exp[0][1].set_color(BLUE)
        exp[1][5].set_color(BLUE)
        exp[3][2].set_color(BLUE)
        exp[3][4].set_color(BLUE)
        exp[3][10].set_color(BLUE)

        for_x = MathTex(
            r'\text{For }',
            r'x=ix', r'\text{ :}',
            font_size=80
        ).next_to(exp, DOWN, buff=1).to_edge(LEFT, buff=1)

        for_x[1][0].set_color(BLUE)
        for_x[1][2].set_color(YELLOW)
        for_x[1][3].set_color(BLUE)

        exp1 = MathTex(
            r'e^{ix}',
            '=',
            r'1+ix+\frac{(ix)^2}{2!}+\frac{(ix)^3}{3!}+...}',
            font_size=80
        ).next_to(exp, DOWN, buff=2)

        exp1[0][1].set_color(YELLOW)
        exp1[0][2].set_color(BLUE)
        exp1[2][2].set_color(YELLOW)
        exp1[2][3].set_color(BLUE)
        exp1[2][6].set_color(YELLOW)
        exp1[2][7].set_color(BLUE)
        exp1[2][15].set_color(YELLOW)
        exp1[2][16].set_color(BLUE)

        i_proprety = MathTex(
            r'i^2=-1\text{, }i^3=-i\text{, }i^4=1\text{, }i^5=i\text{, }i^6=-i\text{ ...}',
            font_size=60,
            color=ORANGE
        ).next_to(exp1, DOWN, buff=1).to_edge(LEFT, buff=1)

        exp2 = MathTex(
            r'e^{ix}',
            '=',
            r'1+ix+\frac{-x^2}{2!}+\frac{-ix^3}{3!}+...}',
            font_size=80
        ).next_to(i_proprety, DOWN, buff=1)

        exp2[0][1].set_color(YELLOW)
        exp2[0][2].set_color(BLUE)
        exp2[2][2].set_color(YELLOW)
        exp2[2][3].set_color(BLUE)
        exp2[2][6].set_color(BLUE)
        exp2[2][13].set_color(YELLOW)
        exp2[2][14].set_color(BLUE)

        let_factor_by_i = MathTex(
            r'\text{Let factor by }i\text{ :}',
            font_size=80
        ).next_to(exp2, DOWN, buff=1).to_edge(LEFT, buff=1)

        let_factor_by_i[0][11].set_color(YELLOW)

        exp3 = MathTex(
            r'e^{ix}',
            '=',
            r'1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\frac{x^8}{8!}+...',
            font_size=80
        ).next_to(exp2, DOWN, buff=2.7).to_edge(LEFT, buff=.7)

        exp3[0][1].set_color(YELLOW)
        exp3[0][2].set_color(BLUE)
        exp3[2][2].set_color(BLUE)
        exp3[2][8].set_color(BLUE)
        exp3[2][14].set_color(BLUE)
        exp3[2][20].set_color(BLUE)

        exp4 = MathTex(
            r'\text{+ }',
            r'i',
            r'(x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!}+...)',
            font_size=80
        ).next_to(exp3, DOWN, buff=.5).to_edge(RIGHT, buff=.7)

        exp4[1].set_color(YELLOW)
        exp4[2][1].set_color(BLUE)
        exp4[2][3].set_color(BLUE)
        exp4[2][9].set_color(BLUE)
        exp4[2][15].set_color(BLUE)
        exp4[2][21].set_color(BLUE)

        cos = MathTex(
            r'cos(x)',
            '=',
            r'\sum_{n\in\mathbb{N}}\frac{(-1)^{n}x^{2n}}{2n!}',
            '=',
            r'1-\frac{x^2}{2!}+\frac{x^4}{4!}+...',
            font_size=67
        )

        cos[0][4].set_color(BLUE)
        cos[2][9].set_color(BLUE)
        cos[4][2].set_color(BLUE)
        cos[4][8].set_color(BLUE)

        sin = MathTex(
            r'sin(x)',
            '=',
            r'\sum_{n\in\mathbb{N}}\frac{(-1)^{n}x^{2n+1}}{(2n+1)!}',
            '=',
            r'x-\frac{x^3}{3!}+\frac{x^5}{5!}+...',
            font_size=67
        )

        sin[0][4].set_color(BLUE)
        sin[2][9].set_color(BLUE)
        sin[4][2].set_color(BLUE)
        sin[4][8].set_color(BLUE)

        self.play(
                AnimationGroup(
                    Write(
                        proof
                    ),
                    Write(
                        using_tylor_formulas1
                    ),
                    lag_ratio=1
                )
        )

        self.wait(.5)

        self.play(
            Write(
                exp,
                run_time=3
            )
        )

        self.wait()

        self.play(
            Write(
                for_x
            )
        )

        self.wait()

        self.play(
            Write(
                exp1,
                run_time=3
            )
        )

        self.wait()

        self.play(
            Write(
                i_proprety,
                run_time=4
            )
        )

        self.wait()

        self.play(
            Write(
                exp2,
                run_time=3
            )
        )

        self.wait()

        self.play(
            Write(
                let_factor_by_i
            )
        )

        self.wait()

        self.play(
            Write(
                exp3,
                run_time=3
            )
        )

        self.wait(0)

        self.play(
            Write(
                exp4,
                run_time=3
            )
        )

        self.wait()

        S_1 = VGroup(using_tylor_formulas1,
                     exp,
                     for_x,
                     exp1,
                     i_proprety,
                     exp2,
                     let_factor_by_i
                     )
        self.play(
            AnimationGroup(
                Write(
                    S_1,
                    run_time=.9,
                    rate_func=lambda t: 1-t
                )
            )
        )

        self.wait(.07)

        self.play(
            AnimationGroup(
                exp3.animate.next_to(proof, DOWN, buff=1.5),
                exp4.animate.next_to(proof, DOWN, buff=4),
                lag_ratio=.09
            )
        )

        self.play(
            AnimationGroup(
                Write(
                    cos
                ),
                cos.animate.next_to(proof, DOWN, buff=8),
                Write(
                    sin
                ),
                sin.animate.next_to(proof, DOWN, buff=11),
                lag_ratio=.5
            )
        )

        box1c = SurroundingRectangle(exp3[2], buff=.1, stroke_width=2, color='#00FFBE')
        box2c = SurroundingRectangle(cos[4], buff=.1, stroke_width=2, color='#00FFBE')

        box1s = SurroundingRectangle(exp4[2], buff=.1, stroke_width=2, color='#00FFBE')
        box2s = SurroundingRectangle(sin[4], buff=.1, stroke_width=2, color='#00FFBE')

        self.wait()

        self.play(
            ReplacementTransform(
                box2c, box1c
            ),
            run_time=3
        )

        COS = MathTex(
            r'cos(x)',
            font_size=80
        ).next_to(exp3[2], ORIGIN)
        COS[0][4].set_color(BLUE)

        SIN = MathTex(
            r'sin(x)',
            font_size=80
        ).next_to(exp4[2], ORIGIN)
        SIN[0][4].set_color(BLUE)

        self.play(
            AnimationGroup(
                FadeOut(
                    box1c
                ),
                ReplacementTransform(
                    exp3[2], COS
                ),
                lag_ratio=.5
            )
        )

        self.play(
            ReplacementTransform(
                box2s, box1s
            ),
            run_time=3
        )

        self.play(
            AnimationGroup(
                FadeOut(
                    box1s
                ),
                ReplacementTransform(
                    exp4[2], SIN
                ),
                lag_ratio=.5
            )
        )

        cosandsin = VGroup(
            COS,
            SIN,
            exp3,
            exp4
        )

        new_eq = MathTex(
            r'e^{ix}',
            '=',
            r'cos(x)+isin(x)',
            font_size=100
        ).next_to(proof, DOWN, buff=2)

        new_eq[0][1].set_color(YELLOW)
        new_eq[0][2].set_color(BLUE)
        new_eq[2][4].set_color(BLUE)
        new_eq[2][7].set_color(YELLOW)
        new_eq[2][12].set_color(BLUE)

        self.wait(.5)

        self.play(
            AnimationGroup(
                Transform(
                    cosandsin, new_eq
                ),
                AnimationGroup(
                    FadeOut(
                        cos
                    ),
                    FadeOut(
                        sin
                    ),
                    lag_ratio=0
                )
            )
        )

        self.wait(.3)

        for_pi = MathTex(
            r'\text{For }',
            r'x=\pi',
            r'\text{ :}',
            font_size=80
        ).next_to(new_eq, DOWN, buff=1).to_edge(LEFT, buff=2)

        for_pi[1][0].set_color(BLUE)
        for_pi[1][2].set_color(BLUE)

        self.play(
            Write(
                for_pi
            )
        )

        self.wait(.3)

        final_eq = MathTex(
            r'e^{i\pi}',
            '=',
            r'cos(\pi)',
            r'+i',
            r'sin(\pi)',
            font_size=120
        ).to_edge(ORIGIN)

        final_eq[0][1].set_color(YELLOW)
        final_eq[0][2].set_color(BLUE)
        final_eq[2][4].set_color(BLUE)
        final_eq[3][1].set_color(YELLOW)
        final_eq[4][4].set_color(BLUE)

        self.play(
            Write(
                final_eq
            )
        )

        one = MathTex(
            r'-1',
            font_size=120
        ).next_to(final_eq[2], ORIGIN)

        zero = MathTex(
            r'0',
            font_size=120
        ).next_to(final_eq[4], ORIGIN)

        self.play(
            AnimationGroup(
                Transform(
                    final_eq[2], one,
                    run_time=2
                ),
                Transform(
                    final_eq[4], zero,
                    run_time=2
                ),
                lag_ratio=0
            )
        )

        Euler_Identity = MathTex(
            r'e^{i\pi}+1=0',
            font_size=200
        ).to_edge(ORIGIN)

        Euler_Identity[0][1].set_color(YELLOW)
        Euler_Identity[0][2].set_color(BLUE)

        self.wait()

        self.play(
                ReplacementTransform(
                    final_eq, Euler_Identity
                )
            )

        self.play(
            Write(
                Euler_Identity,
                rate_func=lambda t: np.abs(np.tan(2)*t-1/2)
            )
        )

        self.wait()