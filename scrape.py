import scrapy


class CFSpider(scrapy.Spider):
    name = 'cf'
    start_urls = ['http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html']

    def parse(self, response):
        def pairwise(it):
            it = iter(it)
            while True:
                yield next(it), next(it)

        dl = response.css('.variablelist dl')[0]

        for dt, dd in pairwise(dl.xpath('./dt | ./dd')):
            yield {
                    'name': dt.css('a::attr(name)').extract(),
                    'action': dd.css('a.link::attr(href)').extract()
                    }
