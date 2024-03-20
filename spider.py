import scrapy
import sys

class FolderSpider(scrapy.Spider):
    name = 'folderspider'
    start_urls = ['http://192.168.56.101/.hidden/']

    def parse(self, response):
        folders = response.css('a::text').extract()
        folders = [folder.strip('/') for folder in folders if folder.endswith('/')]

        for folder in folders:
            yield response.follow(folder, self.parse_folder)

    def parse_folder(self, response):
        readme_link = response.css('a[href$="README"]::attr(href)').get()
        if readme_link:
            yield response.follow(readme_link, self.parse_readme)
        
        folders = response.css('a::text').extract()
        folders = [folder.strip('/') for folder in folders if folder.endswith('/')]
        for folder in folders:
            yield response.follow(folder, self.parse_folder)

    def parse_readme(self, response):
        readme_content = response.body.decode(response.encoding);
        if 'flag' in readme_content:
            with open(f'output.txt', 'a') as f:
                f.write(readme_content)
            sys.exit()
        folder_name = response.url.split('/')[-2]
