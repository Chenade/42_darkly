import scrapy

class FolderSpider(scrapy.Spider):
    name = 'folderspider'
    start_urls = ['http://192.168.56.101/.hidden/']

    def parse(self, response):
        # Extracting folder names
        folders = response.css('a::text').extract()
        folders = [folder.strip('/') for folder in folders if folder.endswith('/')]

        # Following links to other folders
        for folder in folders:
            yield response.follow(folder, self.parse_folder)

    def parse_folder(self, response):
        # Extracting README file link
        readme_link = response.css('a[href$="README"]::attr(href)').get()
        if readme_link:
            yield response.follow(readme_link, self.parse_readme)

    def parse_readme(self, response):
        # Extracting and yielding README content
        readme_content = response.body.decode(response.encoding)
        folder_name = response.url.split('/')[-2]
        with open(f'{folder_name}_README.txt', 'w') as f:
            f.write(readme_content)

