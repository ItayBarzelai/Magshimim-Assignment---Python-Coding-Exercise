from pypdf import PdfReader

class PdfFile:
    def __init__(self, path):
        self.path = path
        try:
            self.reader = PdfReader(self.path)
        except:
            raise Exception("Not a valid pdf file")

    def read_file(self):
        text = ""
        for page in self.reader.pages:
            text += page.extract_text()
            text += "\n"
        return text

    def get_author(self):
        return self.reader.metadata.author
    
    def get_title(self):
        return self.reader.metadata.title
    
    def get_length(self):
        return len(self.reader.pages)
    
    def get_creation_date(self):
         return self.reader.metadata.creation_date
