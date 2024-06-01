import requests
from pypdf import PdfReader

class HTTPDownloader:
    """
    class for downloading files using the http protocol
    """
    def __init__(self, url):
        """
        constructor
        take url and send a get request
        raise exceptions as necessary
        """
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
        """
        method to take the binary data and save it in a local file on the machine
        """
        name = self.url.split('/')[-1] if name == None else name
        path = "." if path == None else path
        self.path = f'{path}/{name}'
        with open(self.path, 'wb') as file:
            file.write(self.res.content)
    
    def is_valid_pdf(self):
        """
        method to make sure the file a valid pdf
        it is here and not in the PdfAnalyzer class because you would like to check it before treating the file as pdf
        """
        try:
            PdfReader(self.path)
            return True
        except:
            return False