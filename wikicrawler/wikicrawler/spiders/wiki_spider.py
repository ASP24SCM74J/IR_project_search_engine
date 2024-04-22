import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']

    custom_settings = {
        'DEPTH_LIMIT': 3,          # Maximum depth of crawl
        'CLOSESPIDER_PAGECOUNT': 100,  # Maximum number of pages to crawl
        'AUTOTHROTTLE_ENABLED': True  # Enables auto-throttling to manage download rate
    }

    def start_requests(self):
        with open('urls.txt', 'rt') as f:
            start_urls = [url.strip() for url in f.readlines()]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
