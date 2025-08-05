import lingam
import numpy as np
from algorithms.causal_order.causal_order_result import CausalOrderResult
from algorithms.causal_order.generic_causal_order_algorithm import CausalOrder


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
    def from_model(self, model: lingam.DirectLiNGAM, time_taken: float, algorithm_type: str, algorithm_name: str, target: str) -> 'EndToEndResult':
        causal_order_result = CausalOrderResult(model.causal_order_, time_taken, algorithm_type, algorithm_name, target)
        return self(causal_order_result, model.adjacency_matrix_, model=model)

    @classmethod
    def from_matrix(self,  result: tuple[np.ndarray, CausalOrder], time_taken: float, algorithm_type: str, algorithm_name: str, target: str) -> 'EndToEndResult':
        estimated_summary_matrix_continuous, causal_order = result
        causal_order_result = CausalOrderResult(causal_order, time_taken, algorithm_type, algorithm_name, target)
        return self(causal_order_result, estimated_summary_matrix_continuous,)

    def __str__(self) -> str:
        # time_taken = self.causal_order_result.time_taken
        # causal_order = self.causal_order_result.causal_order
        # algorithm_name = self.causal_order_result.algorithm_name
        # target_file = self.causal_order_result.target_file
        # msg_target_file = "Target File: " + target_file
        # msg_algorithm_name = "Algorithm: " + algorithm_name
        # msg_causal_order = "Causal Order: " + str(causal_order)
        # msg_time_taken = "time taken: " + str(time_taken) + "seconds"
        return str(self.causal_order_result)
