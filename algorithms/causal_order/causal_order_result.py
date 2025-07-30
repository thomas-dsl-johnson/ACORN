class CausalOrderResult:
    """
    CausalOrderResult encapsulates the result of finding the causal order from a dataset
    """
    def __init__(self, causal_order: list[int], time_taken: float = None):
        self.causal_order = causal_order
        self.time_taken = time_taken

    def __str__(self) -> str:
        sb = "Causal order: "
        sb += str(self.causal_order)
        if self.time_taken is not None:
            sb += ", time taken: "
            sb += str(self.time_taken)
            sb += " seconds"
        return sb.strip()