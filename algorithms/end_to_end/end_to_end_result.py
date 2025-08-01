import lingam
import numpy as np

from algorithms.causal_order.causal_order_result import CausalOrderResult


class EndToEndResult:
    """
    EndtoEndLingamResult encapsulates the result of finding the causal order and model from a dataset
    """

    def __init__(self, causal_order_result: CausalOrderResult, summary_matrix: np.ndarray,
                 model: lingam.DirectLiNGAM = None):
        self.causal_order_result = causal_order_result
        self.summary_matrix = summary_matrix
        self.model: lingam.DirectLiNGAM = model

    @classmethod
    def from_model(self, model: lingam.DirectLiNGAM, time_taken: float) -> 'EndToEndResult':
        causal_order_result = CausalOrderResult(model.causal_order_, time_taken)
        return self(causal_order_result, model.adjacency_matrix_, model=model)

    def __str__(self) -> str:
        return str(self.causal_order_result)
