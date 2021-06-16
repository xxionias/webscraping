# -*- coding: utf-8 -*-
import scrapy
import json
    
# # read file
# with open('../Downloads/stories_encoded.json', 'r') as f:
#     data=f.read()

# # parse file
# data = json.loads(data)

# profile_urls = []
# for e in data:
#     profile_urls.append(e['linkOfAuthorProfile'])

class ProfileSpider(scrapy.Spider):
    name = 'profile'

#   start_urls = profile_urls
    start_urls = "https://medium.com/@luckylwk"

    def parse(self, response):
        for profile in response.xpath(""):
            yield {
                'profileName': profile.xpath(".//div[@class='my ah']/h2[@class='az lt dm bb dj gc dl']/text()").get(),
                'description': profile.xpath(".//div[@class='mz ah']/p[@class='az b ba bb bx']/text()").get(),
                'followers': profile.xpath(".//div[@class='n t']/descendant::div[@class='dp dq t']/a[@class='dr ds by bz ca cb cc cd ce bk dt du cf dv dw']/text()").get()
            }