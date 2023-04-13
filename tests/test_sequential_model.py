from manim_tensorflow.keras import Sequential
from manim_tensorflow.keras.layers import Dense
from manim import *


class SequentialScene(Scene):
    def construct(self):
        model = Sequential([
            Dense(units=64),
            Dense(units=32),
            Dense(units=1),
        ])

        self.play(Write(model))
