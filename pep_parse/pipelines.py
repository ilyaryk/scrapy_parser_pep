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
        with open(f'{BASE_DIR}/results/status_summary_{now}.csv',
                  mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for i in self.statuses.keys():
                total += self.statuses[i]
                f.write(f'{i},{self.statuses[i]}\n')
            f.write(f'Total,{total}\n')
