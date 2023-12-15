from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import Session
import time

Base = declarative_base()


class PEP(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(Text)
    status = Column(Text)


class PepParsePipeline:
    statuses: dict = {}

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        pep = PEP(
            number=item['number'],
            name=item['name'],
            status=item['status']
        )
        self.statuses[item['status']] = self.statuses.get(
            item['status'], 0) + 1
        self.session.add(pep)
        self.session.commit()
        return item

    def close_spider(self, spider):
        now = time.localtime()
        now = time.strftime("%Y-%m-%d_%H_%M_%S", now)
        with open(f'results/status_summary_{now}.csv',
                  mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for i in self.statuses.keys():
                total += self.statuses[i]
                f.write(f'{i},{self.statuses[i]}\n')
            f.write(f'Total,{total}\n')
        self.session.close()
