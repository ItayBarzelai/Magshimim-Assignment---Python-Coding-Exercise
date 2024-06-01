import unittest
import os
from PdfAnalyzer import PdfAnalyzer
from HTTPDownloader import HTTPDownloader
from datetime import datetime

class TestPdfAnalyzer(unittest.TestCase):
    """
    unittest class that will run the pdf analyzer related tests 
    """
    @classmethod
    def setUpClass(cls):
        """
        setUpClass method that will run once before all tests
        - gather the info that is required to compare for each document
        - download and save test files
        """
        cls.pdfs_info = [
            {
                'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
                'author': 'Evangelos Vlachogiannis',
                'title': None,
                'length': 1,
                'creation_date': datetime(2007, 2, 23, 17, 56, 37)
            },
            {
                'url': 'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf',
                'author': 'Accelio Corporation',
                'title': 'PDF Bookmark Sample',
                'length': 4,
                'creation_date': datetime(2001, 10, 26, 13, 39, 34)
            },
            {
                'url': 'https://css4.pub/2015/textbook/somatosensory.pdf',
                'author': None,
                'title': 'Anatomy of the Somatosensory System',
                'length': 4,
                'creation_date': None
            }
        ]

        cls.files = [
            HTTPDownloader(url['url']) for url in cls.pdfs_info
        ]

        for file in cls.files:
            file.save_file()

        cls.pdfs = [
            PdfAnalyzer(file.path) for file in cls.files
        ]
        
    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass method that will run once after all tests
        - delete all test files
        """
        for file in cls.files:
            os.remove(file.path)

    def test_author(self):
        """
        test if author is correct
        """
        for pdf, pdf_url in zip(self.pdfs, self.pdfs_info):
            self.assertEqual(pdf.get_author(), pdf_url['author'])

    def test_title(self):
        """
        test if title is correct
        """
        for pdf, pdf_url in zip(self.pdfs, self.pdfs_info):
            self.assertEqual(pdf.get_title(), pdf_url['title'])

    def test_legth(self):
        """
        test if length of document is correct
        """
        for pdf, pdf_url in zip(self.pdfs, self.pdfs_info):
            self.assertEqual(pdf.get_length(), pdf_url['length'])
    
    def test_creation_date(self):
        """
        test if creation date (accuracy of a day) is correct
        """
        for pdf, pdf_url in zip(self.pdfs, self.pdfs_info):
            try:
                self.assertEqual(pdf.get_creation_date().year, pdf_url['creation_date'].year)
                self.assertEqual(pdf.get_creation_date().month, pdf_url['creation_date'].month)
                self.assertEqual(pdf.get_creation_date().day, pdf_url['creation_date'].day)
            except:
                self.assertEqual(pdf.get_creation_date(), None)

    def test_file_extension_pdf(self):
        """
        test if the file extension is pdf
        """
        for file in self.files:
            self.assertEqual(file.path.split('.')[-1], 'pdf')
    
    def test_pdf_validity(self):
        """
        test if the pdf file is valid
        """
        for file in self.files:
            self.assertTrue(file.is_valid_pdf())


if __name__ == '__main__':
    """
    run only if this file is called directly
    """
    unittest.main()