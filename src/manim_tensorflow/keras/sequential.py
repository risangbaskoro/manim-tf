from manim.mobject.types.vectorized_mobject import VGroup

from manim import *
from manim_tensorflow.engine.base_layer import Layer


class Sequential(VGroup):
    def __init__(
            self,
            layers: Layer | list[Layer],
            sequence_config: dict | None = None,
    ):
        VGroup.__init__(self)

        self.sequence_config = {
            "edge_stroke_width": 1,
        }

        if sequence_config is not None:
            self.sequence_config = merge_dicts_recursively(self.sequence_config, sequence_config)

        for index, layer in enumerate(layers):
            if index == 0:
                self.add(layer)
            else:
                prev_layer = layers[index - 1]
                layer.next_to(prev_layer, 2 * RIGHT)  # TODO: Make next_to dynamic by rotating 90 degrees
                edges = self._create_edges(prev_layer, layer)
                self.add(layer)
                self.add(edges)

        self.center()

    def _create_edges(
            self,
            prev_layer: Layer,
            layer: Layer,
    ) -> VGroup:
        edges = VGroup()
        for prev_node in prev_layer.get_nodes():
            for node in layer.get_nodes():
                if not isinstance(prev_node, Dot) and not isinstance(node, Dot):
                    edge = Line(
                        prev_node.get_edge_center(RIGHT),  # TODO: Make get_edge_center dynamic
                        node.get_edge_center(LEFT),  # TODO: Make get_edge_center dynamic
                        stroke_width=self.sequence_config["edge_stroke_width"],
                    )
                    edges.add(edge)

        return edges
