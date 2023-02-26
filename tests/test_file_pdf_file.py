from unittest import TestCase

from utils import PDFFile

TEST_PDF_FILE = PDFFile('tests/example.pdf')


class TestPDFFile(TestCase):
    def test_n_pages(self):
        self.assertEqual(TEST_PDF_FILE.n_pages, 16)

    def test_tables(self):
        table_files = TEST_PDF_FILE.table_files
        self.assertEqual(len(table_files), 5)
