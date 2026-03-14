import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        yield response.follow("numerical/", callback=self.parse_numerical)

    def parse_numerical(self, response):
        pep_links = response.css(
            "section#numerical-index a::attr(href)"
        ).getall()
        for link in pep_links:
            if link != "../pep-0000/":
                yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css("h1.page-title::text").get()
        match = re.search(r"PEP\s+(\d+)\s+–\s+(.+)", title)
        number, name = match.groups()

        status = response.xpath(
            '//dt[contains(., "Status")]/following-sibling::dd[1]/abbr/text()'
        ).get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
