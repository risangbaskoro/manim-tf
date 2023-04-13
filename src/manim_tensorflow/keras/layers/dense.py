from manim_tensorflow.module import Module
from manim_tensorflow.engine.base_layer import Layer

from manim import *


class Dense(Layer, Module):
    def __init__(
            self,
            units: int,
            neurons_config: dict | None = None,
            max_units: int = 6,
            input_shape: tuple[int, int] | None = None,
            **kwargs,
    ):
        Layer.__init__(self, **kwargs)

        self.neurons_config = {
            "neuron_radius": 0.15,
            "color": self.get_color(),
            "neurons_direction": DOWN,
            "neurons_buff": MED_SMALL_BUFF,
        }

        if neurons_config is not None:
            self.neurons_config = merge_dicts_recursively(self.neurons_config, neurons_config)

        self.units = units
        self.max_units = max_units

        self.neurons = self._create_neurons(self.units, self.neurons_config, self.max_units)
        self.add(*self.neurons)

    def _create_neurons(
            self,
            units: int,
            neurons_config: dict,
            max_units: int,
    ) -> Layer:
        neurons = Layer()
        num_neurons = units
        dots = []

        if units > max_units:
            num_neurons = self.max_units + 1
            dots = VGroup(*[Dot(radius=.05) for _ in range(3)])
            dots.arrange(neurons_config["neurons_direction"], buff=neurons_config["neurons_buff"]/3)

        for _ in range(num_neurons):
            if _ == num_neurons // 2 and units > max_units:
                neurons.add(*dots)
            else:
                neuron = Circle(
                    radius=neurons_config["neuron_radius"],
                    color=neurons_config["color"],
                )
                neurons.add(neuron)

        neurons.arrange(
            neurons_config["neurons_direction"],
            buff=neurons_config["neurons_buff"],
        )

        return neurons
