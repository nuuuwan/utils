from utils.file.XSVFile import XSVFile

DELIMITER_CSV = ','


class CSVFile(XSVFile):
    def __init__(self, path):
        return XSVFile.__init__(self, path, DELIMITER_CSV)
