import scrapy
from pep_parse.items import PepParseItem

class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org"]

    def parse(self, response):
        all_peps = response.css('a[href^="pep"]')
        print(all_peps)
        print(234)
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)


    def parse_pep(self, response):
        resp = response.css('h1.page-title::text').get()
        num = int(resp.split()[1])
        title = resp.split()[3:]
        status = response.css('dt:contains("Status") + dd').get().split('</abbr>')[0].split('>')[-1]
        yield PepParseItem({
            'number': num,
            'name': ' '.join(title),
            'status': status
        })
        
