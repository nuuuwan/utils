class TimeDelta:
    def __init__(self, dut: int = 0):
        self.dut = dut

    def __eq__(self, other) -> bool:
        return self.dut == other.dut

    def humanize(self):
        dut = self.dut

        for dut_limit, label in [
            (60, 'second'),
            (60, 'minute'),
            (24, 'hour'),
            (7, 'day'),
            (None, 'week'),
        ]:
            if not dut_limit or dut < dut_limit:
                if dut == 1:
                    return f'{dut}{label}'
                return f'{dut}{label}s'
            else:
                dut /= dut_limit
