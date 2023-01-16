import time


class TIMEZONE_OFFSET:
    LK = -19_800
    GMT = 0


class TimeUnit:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def __truediv__(self, other):
        if isinstance(other, TimeUnit):
            return self.seconds / other.seconds
        if isinstance(other, float) or isinstance(other, int):
            return TimeUnit(self.seconds / other)
        raise TypeError(
            f'unsupported operand type(s) for /: {type(self)} and {type(other)}'
        )

    def __mul__(self, other):
        return TimeUnit(self.seconds * other)


SECOND = TimeUnit(1)
MINUTE = SECOND * 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7
FORTNIGHT = WEEK * 7

AVG_YEAR = DAY * 365.25
AVG_QTR = AVG_YEAR / 4
AVG_MONTH = AVG_YEAR / 12


class SECONDS_IN:
    MINUTE = MINUTE / SECOND
    HOUR = HOUR / SECOND
    DAY = DAY / SECOND
    WEEK = WEEK / SECOND
    FORTNIGHT = FORTNIGHT / SECOND

    AVG_MONTH = AVG_MONTH / SECOND
    AVG_QTR = AVG_QTR / SECOND
    AVG_YEAR = AVG_YEAR / SECOND


class DAYS_IN:
    AVG_MONTH = AVG_MONTH / DAY
    AVG_QTR = AVG_QTR / DAY
    AVG_YEAR = AVG_YEAR / DAY


class TimeDelta:
    def __init__(self, dut: int = 0):
        self.dut = dut

    def __eq__(self, other) -> bool:
        return self.dut == other.dut

    def humanize(self):
        dut = self.dut
        if dut < 60:
            return f'{dut:.0f}sec'
        dut /= 60
        if dut < 60:
            return f'{dut:.0f}min'
        dut /= 60
        if dut < 24:
            return f'{dut:.0f}hr'
        dut /= 24
        return f'{dut:.0f}day'


class Time:
    def __init__(self, ut: int = None):
        if ut is None:
            ut = time.time()
        self.ut = ut

    def __eq__(self, other) -> bool:
        return self.ut == other.ut

    def __sub__(self, other) -> TimeDelta:
        return TimeDelta(self.ut - other.ut)

    def __add__(self, other: TimeDelta):
        return Time(self.ut + other.dut)

    @staticmethod
    def now():
        return Time()


class TimeFormat:
    def __init__(self, format_str: str, timezone_offset=0):
        self.format_str = format_str
        self.timezone_offset = timezone_offset

    @property
    def dut_timezone(self):
        return time.timezone - self.timezone_offset

    def parse(self, time_str: str) -> Time:
        ut = (
            time.mktime(time.strptime(time_str, self.format_str))
            - self.dut_timezone
        )
        return Time(ut)

    def stringify(self, t: Time) -> str:
        return time.strftime(
            self.format_str, time.localtime(t.ut + self.dut_timezone)
        )


TIME_FORMAT_DATE_ID = TimeFormat('%Y-%m-%d')
TIME_FORMAT_TIME_ID = TimeFormat('%Y-%m-%d %H:%M:%S')
