import scrapy
import sys

class FolderSpider(scrapy.Spider):
    name = 'folderspider'
    start_urls = ['http://192.168.56.101/.hidden']

    def parse(self, response, path=''):
        folders = response.css('a::text').extract()
        folders = [folder.strip('/') for folder in folders if folder.endswith('/')]

        # Following each folder link and passing the current path
        for folder in folders:
            yield response.follow(folder, self.parse_folder, meta={'path': path + '/' + folder})

    def parse_folder(self, response):
        readme_link = response.css('a[href$="README"]::attr(href)').get()

        # Following the README link and passing the current path
        if readme_link:
            yield response.follow(readme_link, self.parse_readme, meta={'path': response.meta['path'] + '/'})
        
        folders = response.css('a::text').extract()
        folders = [folder.strip('/') for folder in folders if folder.endswith('/')]
        for folder in folders:
            yield response.follow(folder, self.parse_folder, meta={'path': response.meta['path'] + '/' + folder})

    def parse_readme(self, response):
        readme_content = response.body.decode(response.encoding)
        if 'flag' in readme_content:
            with open('output.txt', 'a') as f:
                f.write(f"Path: {start_urls}{response.meta['path']} | Content:\n{readme_content}\n\n")
            sys.exit()

