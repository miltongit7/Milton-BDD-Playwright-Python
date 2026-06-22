from pathlib import Path
from playwright.sync_api import Page

class CommonUtils:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def getCsvData() -> list[tuple[str, str, str]]:
        import csv

        csv_path = Path(__file__).resolve().parents[1] / "testData" / "testData.csv"
        data: list[tuple[str, str, str]] = []

        with csv_path.open(newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader if row and not all(cell.strip().startswith('#') for cell in row)]

        if not rows:
            return data

        header = [cell.strip().lower() for cell in rows[0]]
        if len(header) >= 2 and header[0] == "username" and header[1] == "password":
            with csv_path.open(newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    username = row.get("username", "").strip()
                    password = row.get("password", "").strip()
                    test_name = row.get("test_name", "").strip()
                    if username and password:
                        data.append((username, password, test_name))
        else:
            for row in rows:
                if len(row) < 2:
                    continue
                username = row[0].strip()
                password = row[1].strip()
                test_name = row[2].strip() if len(row) >= 3 else ""
                if username and password:
                    data.append((username, password, test_name))

        return data
