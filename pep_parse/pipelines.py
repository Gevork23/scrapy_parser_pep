# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        self.status_summary = defaultdict(int)
        self.total = 0

    def process_item(self, item, spider):
        status = item['status']
        self.status_summary[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = RESULTS_DIR / f'status_summary_{now}.csv'

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            for status, count in self.status_summary.items():
                file.write(f'{status},{count}\n')
            file.write(f'Total,{self.total}\n')
