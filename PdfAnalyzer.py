from pypdf import PdfReader

class PdfAnalyzer:
    """
    class for pdf analyzing
    """
    def __init__(self, path):
        """
        constructor
        take path of a file and creating a reader instance (pypdf)
        """
        self.path = path
        try:
            self.reader = PdfReader(self.path)
        except:
            raise Exception("Not a valid pdf file")

    def read_file(self):
        """
        return all text on all pages
        """
        text = ""
        for page in self.reader.pages:
            text += page.extract_text()
            text += "\n"
        return text

    def get_author(self):
        """
        return author of document
        """
        return self.reader.metadata.author
    
    def get_title(self):
        """
        return title of document
        """
        return self.reader.metadata.title
    
    def get_length(self):
        """
        return length of document
        """
        return len(self.reader.pages)
    
    def get_creation_date(self):
        """
        return creation date of document
        """
        return self.reader.metadata.creation_date
