import scrapy
import re
class NWinnerItem(scrapy.Item):
    country = scrapy.Field()
    name = scrapy.Field()
    link_text = scrapy.Field()
class NWinnerSpider(scrapy.Spider):

    name  = 'winner_list'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ["http;//en.wikipedia.org ... of_Nobel_laureats_by_country"]

    def parese(self, response):
        h2s = response.xpath('//h2')

        for h2 in h2s:
            country = h2.xpath('span[@class="mw-headline"]''text()').extract()
            if country:
                winners = h2.xpath('following-sibling::ol[1]')
                for w in winners.xpath('descendant-or-self::text()').extract():
                    yield NWinnerItem(country=country[0], name=text[0], link_text = ' '.join(text))