import requests


class Downloader:
    
    def __init__(self, url):
        self.url = url
        self.html = ''
    
    def download_page(self):
        req = requests.get(self.url)
        self.html = req.text
        return 
