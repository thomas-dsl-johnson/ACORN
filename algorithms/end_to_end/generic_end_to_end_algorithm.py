import abc
import time
import typing
import os
import lingam
import pandas as pd
from algorithms.causal_order.causal_order_result import CausalOrderResult
from algorithms.end_to_end.end_to_end_result import EndToEndResult


class GenericEndToEndAlgorithm:
    """
    An abstract base class representing a generic algorithm that produces a causal order and model
    """
    @abc.abstractmethod
    def run(self, df: pd.DataFrame) -> lingam.DirectLiNGAM :
        """
        Run the End to End Order Algorithm

        Parameters
        ----------
        df : pd.DataFrame,
             The training data, with shape (n_samples, n_features) where
             - n_samples is the number of samples
             - n_features is the number of features

        Returns
        ----------
        model : lingam.DirectLiNGAM
            A fitted DirectLiNGAM model containing the estimated causal order.
            The causal order can be accessed via model.causal_order_ as a list of feature indices.
        """
        raise NotImplementedError

    @staticmethod
    def __get_df(filepath: str) -> pd.DataFrame:
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
        return X

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
        df = self.__get_df(filepath)
        beg = time.time()
        model = self.run(df)
        end = time.time()
        time_taken = end - beg
        return CausalOrderResult(model.causal_order_, time_taken)

    def get_end_to_end_result(self, filepath: str) -> EndToEndResult:
        """
        Run the Causal Order Algorithm

        Parameters
        ----------
        filepath : str
            The path to the file to load the training IT_monitoring from.
            Only .csv, .xls, and .xlsx files are currently supported.

        Returns
        ----------
        result : EndToEndResult
            An object that encapsulates the estimated causal order and the fitted DirectLiNGAM model.
            - `result.causal_order_result.causal_order` gives the causal order as a list of feature indices.
            - `result.causal_order_result.time` gives the time taken in seconds.
            - `result.model` gives access to the full fitted lingam.DirectLiNGAM model.
        """
        df = self.__get_df(filepath)
        beg = time.time()
        model = self.run(df)
        end = time.time()
        time_taken = end - beg
        causal_order_result = CausalOrderResult(model.causal_order_, time_taken)
        return EndToEndResult(causal_order_result, model)
