import abc
import time
import typing
import os
import pandas as pd
from algorithms.causal_order.causal_order_result import CausalOrderResult

CausalOrder: typing.TypeAlias = list[int]


class GenericCausalOrderAlgorithm:
    """
    An abstract base class representing a generic algorithm that produces a causal order
    """

    @abc.abstractmethod
    def run(self, df: pd.DataFrame) -> CausalOrder:
        """
        Run the Causal Order Algorithm

        Parameters
        ----------
        df : pd.DataFrame,
             The training IT_monitoring, with shape (n_samples, n_features) where
             - n_samples is the number of samples
             - n_features is the number of features

        Returns
        ----------
        causal_order : CausalOrder,
            The causal order. A CausalOrder is a list[int] where
            each integer represents the index of a feature in the training IT_monitoring.
        """
        raise NotImplementedError

    def get_causal_order_result(self, filepath: str) -> CausalOrderResult:
        """
        Run the Causal Order Algorithm

        Parameters
        ----------
        filepath : str
            The path to the file to load the training IT_monitoring from.
            Only .csv, .xls, and .xlsx files are currently supported.

        Returns
        ----------
        causalOrderResult : CausalOrderResult
            An object containing:
            - `causal_order`: list of feature indices representing the causal order.
            - `time_taken`: time taken to compute the causal order, in seconds.
        """
        file_extension = os.path.splitext(filepath)[1].lower()
        if file_extension == '.csv':
            X = pd.read_csv(filepath)
        elif file_extension in ['.xls', '.xlsx']:
            X = pd.read_excel(filepath)
        else:
            raise ValueError(
                f"Unsupported file type: '{file_extension}'. "
                "Only .csv, .xls, and .xlsx files are currently supported."
            )
        beg = time.time()
        causal_order = self.run(X)
        end = time.time()
        time_taken = end - beg
        return CausalOrderResult(causal_order, time_taken)
