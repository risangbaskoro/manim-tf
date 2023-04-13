from manim import *
from manim_tensorflow.keras.layers.dense import Dense


class DenseScene(Scene):
    def construct(self):
        layer1 = Dense(units=10, color=RED)
        layer2 = Dense(units=4, color=GREEN).next_to(layer1, RIGHT)
        layer3 = Dense(units=3, color=BLUE).next_to(layer2, RIGHT)

        group = VGroup(layer1, layer2, layer3).move_to(ORIGIN).arrange(RIGHT, buff=2)

        self.play(Write(group))
