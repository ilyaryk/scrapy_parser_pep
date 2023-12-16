from pathlib import Path

BOT_NAME = "pep_parse"
BASE_DIR = Path(__file__).parent
SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    f'{BASE_DIR}results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },

}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
