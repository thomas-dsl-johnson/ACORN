"""
This is the entry point for running ACORN - Assess Causal Order Results Neatly
"""


if __name__ == "__main__":
    import lingam
    import pandas as pd
    import os
    from utils.storage import save, load
    filepath = "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500/sp500.csv"
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

    model = lingam.DirectLiNGAM()
    model.fit(X)
    print(model.causal_order_)
    save(model,"model.pkl")

    # model : lingam.DirectLiNGAM = load("model.pkl")
    # print(model.causal_order_)

