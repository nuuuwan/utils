import time


class TimeDelta:
    def __init__(self, dut):
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
    def __init__(self, ut):
        self.ut = ut

    def __eq__(self, other) -> bool:
        return self.ut == other.ut

    def __sub__(self, other) -> TimeDelta:
        return TimeDelta(self.ut - other.ut)

    @staticmethod
    def now():
        return Time(time.time())


class TimeFormat:
    def __init__(self, format_str: str):
        self.format_str = format_str

    def parse(self, time_str: str) -> Time:
        ut = time.mktime(time.strptime(time_str, self.format_str))
        return Time(ut)

    def stringify(self, t: Time) -> str:
        return time.strftime(self.format_str, time.localtime(t.ut))
