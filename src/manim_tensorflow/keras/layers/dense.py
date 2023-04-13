from manim_tensorflow.engine.base_layer import Layer
from manim.mobject.geometry.arc import Circle, Dot
from manim.constants import DOWN

from manim import *


class Dense(Layer):
    def __init__(
            self,
            units: int,
            units_config: dict | None = None,
            max_units: int = 6,
            **kwargs,
    ):
        Layer.__init__(self, **kwargs)

        self.units_config = {
            "radius": 0.2,
            "color": self.get_color(),
            "nodes_direction": DOWN,
        }

        if units_config is not None:
            self.units_config = merge_dicts_recursively(self.units_config, units_config)

        self.units = units
        self.max_units = max_units

        self.nodes = self._create_nodes(self.units, self.units_config, self.max_units)
        self.add(*self.nodes)

    def _create_nodes(
            self,
            units: int,
            units_config: dict,
            max_units: int,
    ) -> Layer:
        nodes = Layer()
        num_units = units
        dots = []

        if units > max_units:
            num_units = self.max_units + 1
            dots = [Dot() for _ in range(3)]

        for _ in range(num_units):
            if _ == num_units // 2 and units > max_units:
                nodes.add(*dots)
            else:
                node = Circle(
                    radius=units_config["radius"],
                    color=units_config["color"],
                )
                nodes.add(node)

        nodes.arrange(units_config["nodes_direction"], buff=0.1)

        return nodes
