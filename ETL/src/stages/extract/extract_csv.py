import pandas as pd

class ExtractCSV:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path, encoding="latin1")
