import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            'section#numerical-index a.pep::attr(href)'
        ).getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css(
            'dl.rfc2822.field-list.simple dd.field-even::text'
        ).get()
        name = response.css('h1.page-title::text').get()
        status = response.css(
            'abbr::text'
        ).get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )