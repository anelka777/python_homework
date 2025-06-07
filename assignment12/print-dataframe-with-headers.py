import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        total_rows = len(self)

        for start in range(0, total_rows, 10):
            end = start + 10
            print("\n" + "-" * 40)
            print(f"Rows {start} to {min(end, total_rows) - 1}")
            print("-" * 40)
            print(self.iloc[start:end])


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
