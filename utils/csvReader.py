import pandas as pd
from pathlib import Path
from typing import List, Tuple, Optional


class CSVReader:
    @staticmethod
    def read_csv(file_path: str) -> List[dict]:
        df = pd.read_csv(file_path)
        df = df.dropna(how='all')
        return df.to_dict(orient='records')
