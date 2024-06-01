import requests
from pypdf import PdfReader

class DownloadFile:
    def __init__(self, url):
        self.url = url
        try:
            self.res = requests.get(url)
        except Exception as e:
            if type(e) is requests.exceptions.ConnectionError:
                raise Exception("Can't be reached")
        if self.res.status_code == 404:
            raise Exception("File not found")
        elif self.res.status_code != 200:
            raise Exception("Download failed")

    def save_file(self, name=None, path=None):
        name = self.url.split('/')[-1] if name == None else name
        path = "." if path == None else path
        self.path = f'{path}/{name}'
        with open(self.path, 'wb') as file:
            file.write(self.res.content)
    
    def is_valid_pdf(self):
        try:
            PdfReader(self.path)
            return True
        except:
            return False