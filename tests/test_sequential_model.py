from manim_tensorflow.keras.sequential import Sequential
from manim_tensorflow.keras.layers.dense import Dense
from manim import *


class SequentialScene(Scene):
    def construct(self):
        model = Sequential([
            Dense(units=64, color=RED),
            Dense(units=32, color=GREEN),
            Dense(units=1, color=BLUE),
        ])

        self.play(Write(model))
