import csv
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"


class PepParsePipeline:
    def open_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        self.status_summary = {}
        self.total = 0

    def process_item(self, item, spider):
        status = item["status"]
        self.status_summary[status] = self.status_summary.get(status, 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = RESULTS_DIR / f"status_summary_{now}.csv"

        with open(
            file_path,
            "w",
            encoding="utf-8",
            newline="",
        ) as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            rows = [("Статус", "Количество")]
            rows.extend(self.status_summary.items())
            rows.append(("Total", self.total))
            writer.writerows(rows)
