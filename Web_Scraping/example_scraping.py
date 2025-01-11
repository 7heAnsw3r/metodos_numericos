import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'Epn'
    start_urls = ['https://www.epn.edu.ec']

    def parse(self, response):
        for title in response.css('h1::text'):
            print({'Title': title.get()})
            yield {'Title': title.get()}
