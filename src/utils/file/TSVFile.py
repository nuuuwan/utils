from utils.file.XSVFile import XSVFile

DELIMITER_TSV = '\t'


class TSVFile(XSVFile):
    def __init__(self, path):
        return XSVFile.__init__(self, path, DELIMITER_TSV)
