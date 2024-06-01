import unittest
import os
from HTTPDownloader import HTTPDownloader

class TestHTTPDownloader(unittest.TestCase):
    """
    unittest class that will run the http downloader related tests 
    """
    def setUp(self):
        """
        setUp method that will run once before any test
        - gather the urls for a variety of situations
        - download files
        """
        self.urls = [
            'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf',
            'https://css4.pub/2015/textbook/somatosensory.pdf',
            'https://www.aquasec.com/wp-content/themes/aqua3/images/logo_aqua_dark.svg',
        ]

        self.imaginary_pdf_url = 'https://google.com/no_such_file.pdf'
        self.imaginary_server_url = 'https://nothing_to_see_here.com/for_read.pdf'

        self.files = [
            HTTPDownloader(url) for url in self.urls
        ]

    def tearDown(self):
        """
        tearDown method that will run once after any test
        doesn't do anything, there for any future need
        """
        pass

    def test_200_status_code(self):
        """
        test if status code is 200
        """
        for file in self.files:
            self.assertEqual(file.res.status_code, 200)

    def test_file_not_found(self):
        """
        test raising error for file not found
        """
        with self.assertRaises(Exception) as context:
            HTTPDownloader(self.imaginary_pdf_url)
        self.assertIn('File not found', str(context.exception))

    def test_cant_be_reached(self):
        """
        test raising error for server that can't be reached
        """
        with self.assertRaises(Exception) as context:
            HTTPDownloader(self.imaginary_server_url)
        self.assertIn("Can't be reached", str(context.exception))

    def test_saved_correctyl(self):
        """
        test for making sure the file has been saved correctly
        - compare the file content to the original file
        """
        for file in self.files:
            file.save_file()

        for file, url in zip(self.files, self.urls):
            with open(file.path, 'rb') as f:
                self.assertEqual(f.read(), HTTPDownloader(url).res.content)

        for file in self.files:
            os.remove(file.path)

if __name__ == '__main__':
    """
    run only if this file is called directly
    """
    unittest.main()