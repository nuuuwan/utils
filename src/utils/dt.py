"""Utils related to simple data types"""


def parse_float(float_str, default=None):
    """Parse float."""
    float_str = float_str.replace(',', '')
    float_str = float_str.replace('-', '0')
    try:
        return (float)(float_str)
    except ValueError:
        return default


def parse_int(int_str, default=None):
    """Parse int."""
    int_str = int_str.replace(',', '')
    int_str = int_str.replace('-', '0')
    try:
        return (int)(int_str)
    except ValueError:
        return default
