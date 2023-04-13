from manim.mobject.types.vectorized_mobject import VGroup


class Layer(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
