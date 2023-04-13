from manim_tensorflow.module import Module
from manim_tensorflow.engine.base_layer import Layer

from manim import *


class Dense(Layer, Module):
    def __init__(
            self,
            units: int,
            units_config: dict | None = None,
            max_units: int = 6,
            **kwargs,
    ):
        Layer.__init__(self, **kwargs)

        self.units_config = {
            "neuron_radius": 0.15,
            "color": self.get_color(),
            "neurons_direction": DOWN,
            "neurons_buff": MED_SMALL_BUFF,
        }

        if units_config is not None:
            self.units_config = merge_dicts_recursively(self.units_config, units_config)

        self.units = units
        self.max_units = max_units

        self.neurons = self._create_neurons(self.units, self.units_config, self.max_units)
        self.add(*self.neurons)

    def _create_neurons(
            self,
            units: int,
            units_config: dict,
            max_units: int,
    ) -> Layer:
        neurons = Layer()
        num_units = units
        dots = []

        if units > max_units:
            num_units = self.max_units + 1
            dots = [Dot() for _ in range(3)]

        for _ in range(num_units):
            if _ == num_units // 2 and units > max_units:
                neurons.add(*dots)
            else:
                neuron = Circle(
                    radius=units_config["neuron_radius"],
                    color=units_config["color"],
                )
                neurons.add(neuron)

        neurons.arrange(
            units_config["neurons_direction"],
            buff=units_config["neurons_buff"],
        )

        return neurons
