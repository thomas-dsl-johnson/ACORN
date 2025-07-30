import abc
import time
import typing
import os
import pandas as pd

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

    def get_causal_order_result(self, filepath: str) -> (CausalOrder, float):
        """
        Run the Causal Order Algorithm

        Parameters
        ----------
        filepath : str
            The path to the file to load the training IT_monitoring from.
            Only .csv, .xls, and .xlsx files are currently supported.

        Returns
        ----------
        causal_order : CausalOrder,
            The causal order. A CausalOrder is a list[int] where
            each integer represents the index of a feature in the training IT_monitoring.
        time_taken : float
            The time taken to run the Causal Order algorithm in seconds.
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
        return causal_order, time_taken
