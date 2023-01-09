class Dict:
    def __init__(self, d={}):
        assert isinstance(d, dict)
        self.d = d

    def keys(self):
        return self.d.keys()

    def values(self):
        return self.d.values()

    def items(self):
        return self.d.items()

    def items_sorted_by_key(self):
        return sorted(
            self.d.items(),
            key=lambda item: item[0],
        )

    def items_sorted_by_value(self):
        return sorted(
            self.d.items(),
            key=lambda item: item[1],
        )

    def len(self):
        return len(self.d)

    def __eq__(self, other):
        if isinstance(other, Dict):
            return self.d == other.d
        if isinstance(other, dict):
            return self.d == other
        return False

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value

    def __delitem__(self, key):
        del self.d[key]

    def iter(self):
        return iter(self.d)

    def extract_keys(self, keys):
        return Dict(
            dict(
                list(
                    filter(
                        lambda item: item[0] in keys,
                        self.d.items(),
                    )
                )
            )
        )

    def __str__(self):
        return self.d.__str__()

    def __repr__(self):
        return self.d.__repr__()
