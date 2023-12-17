from sqlalchemy.ext.declarative import declarative_base
import time
from pathlib import Path

Base = declarative_base()
BASE_DIR = Path(__file__).parent


class PepParsePipeline:
    statuses: dict = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses[item['status']] = self.statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now = time.localtime()
        now = time.strftime("%Y-%m-%d_%H_%M_%S", now)
        sequence = 'Статус,Количество\n'
        with open(f'{BASE_DIR}/results/status_summary_{now}.csv',
                  mode='w', encoding='utf-8') as f:
            total = 0
            for status in self.statuses.keys():
                total += self.statuses[status]
                sequence += f'{status},{self.statuses[status]}\n'
            f.write(sequence+f'Total,{total}\n')
