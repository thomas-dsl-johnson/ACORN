import lingam
from algorithms.causal_order.causal_order_result import CausalOrderResult


class EndToEndResult:
    """
    EndtoEndLingamResult encapsulates the result of finding the causal order and model from a dataset
    """

    def __init__(self, causal_order_result: CausalOrderResult, model: lingam.DirectLiNGAM):
        self.causal_order_result = causal_order_result
        self.model: lingam.DirectLiNGAM = model

    def __str__(self):
        return str(self.causal_order_result)
