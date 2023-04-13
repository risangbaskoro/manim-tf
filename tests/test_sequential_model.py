from manim_tensorflow.keras import Sequential
from manim_tensorflow.keras.layers import Dense
from manim import *


class SequentialScene(Scene):
    def construct(self):
        model = Sequential([
            Dense(64, max_units=16),
            Dense(32, max_units=16),
            Dense(4),
            Dense(1),
        ])

        self.play(Write(model))
        self.wait()
