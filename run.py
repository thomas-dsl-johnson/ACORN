"""
This is the entry point for running ACORN - Assess Causal Order Results Neatly
"""


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
"""

if __name__ == "__main__":
    # import lingam
    # import utils.storage as storage
    # import lingam
    # import numpy as np
    # import os
    # model : lingam.DirectLiNGAM = storage.load("model.pkl")
    # print(model.causal_order_)
    #
    # print("Model created. Saving data")
    # dest = "../" + os.path.dirname(".")
    # # Write causal_order.txt
    # with open(dest + "/causal_order.txt", "w") as file:
    #     file.write(", ".join(map(str, model.causal_order_)))
    # print("Causal Order Saved to " + dest + "/causal_order")
    # # Write summary_matrix.npy
    # np.save(dest + "/summary_matrix.npy", model.adjacency_matrix_)
    # print("Summary matrix saved to " + dest + "/summary_matrix")
    # # Write pickle file
    # storage.save(model, dest + "/model.pkl", save_to_default=False)
    # print("Model saved to " + dest + "/model.pkl")

    if __name__ == '__main__':
        from algorithms.end_to_end.original.direct_lingam_end_to_end_algorithm import DirectLingamEndToEndAlgorithm
        x = DirectLingamEndToEndAlgorithm()
        x.get_and_save_end_to_end_result(
            "/Users/thomasjohnson/Desktop/UROP/ACORN/data/ground_truth_not_available/sp500_5_columns/sp500_5_columns.xlsx")




