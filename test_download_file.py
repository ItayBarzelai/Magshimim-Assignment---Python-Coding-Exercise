import unittest
import os
from DownloadFile import DownloadFile

class TestDownloadFile(unittest.TestCase):
    def setUp(self):
        self.urls = [
            'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf',
            'https://css4.pub/2015/textbook/somatosensory.pdf',
            'https://www.aquasec.com/wp-content/themes/aqua3/images/logo_aqua_dark.svg',
        ]

        self.imaginary_pdf_url = 'https://google.com/no_such_file.pdf'
        self.imaginary_server_url = 'https://nothing_to_see_here.com/for_read.pdf'

        self.files = [
            DownloadFile(url) for url in self.urls
        ]

    def tearDown(self):
        pass

    def test_200_status_code(self):
        for file in self.files:
            self.assertEqual(file.res.status_code, 200)

    def test_file_not_found(self):
        with self.assertRaises(Exception) as context:
            DownloadFile(self.imaginary_pdf_url)
        self.assertIn('File not found', str(context.exception))

    def test_cant_be_reached(self):
        with self.assertRaises(Exception) as context:
            DownloadFile(self.imaginary_server_url)
        self.assertIn("Can't be reached", str(context.exception))

    def test_saved_correctyl(self):
        for file in self.files:
            file.save_file()

        for file, url in zip(self.files, self.urls):
            with open(file.path, 'rb') as f:
                self.assertEqual(f.read(), DownloadFile(url).res.content)

        for file in self.files:
            os.remove(file.path)

if __name__ == '__main__':
    unittest.main()