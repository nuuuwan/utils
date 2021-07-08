"""Utils related to lists and dicts."""


def dict_list_to_index(dict_list, key):
    """Given a list of dicts, returns an index mapping each dict item
    to the dict.
    """
    return dict(
        zip(
            list(
                map(
                    lambda d: d.get(key, None),
                    dict_list,
                )
            ),
            dict_list,
        )
    )


def unique(lst):
    """Get unique values from list."""
    return list(set(lst))


def flatten(list_of_list):
    """Flatten list of lists."""
    flattened_list = []
    for lst in list_of_list:
        flattened_list += lst
    return flattened_list


def sort_dict_items_by_key(_dict):
    """Sort dict items by key."""
    return sorted(
        _dict.items(),
        key=lambda item: item[0],
    )


def dict_get(_dict, keys):
    """Get dict values by keys."""
    return [_dict[key] for key in keys]


def dict_set(_dict, keys, values):
    """Set dict values by keys."""
    for key, value in zip(keys, values):
        _dict[key] = value
    return _dict
