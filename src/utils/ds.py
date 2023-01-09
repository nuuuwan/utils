"""Utils related to lists and dicts."""
from warnings import warn

from utils.Dict import Dict
from utils.List import List


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
    warn(PendingDeprecationWarning)
    """Get unique values from list."""
    return List(lst).unique().tolist()


def flatten(list_of_list):
    warn(PendingDeprecationWarning)
    """Flatten list of lists."""
    return List(list_of_list).flatten().tolist()


def sort_dict_items_by_key(_dict):
    warn(PendingDeprecationWarning)
    """Sort dict items by key."""
    return Dict(_dict).items_sorted_by_key()


def dict_get(_dict, keys):
    warn(PendingDeprecationWarning)
    """Get dict values by keys."""
    return Dict(_dict).extract_keys(keys).x


def dict_list_get_values_for_key(dict_list, key):
    """Get values for keys."""
    return [d[key] for d in dict_list]


def dict_set(_dict, keys, values):
    warn(PendingDeprecationWarning)
    """Set dict values by keys."""
    for key, value in zip(keys, values):
        _dict[key] = value
    return _dict


def get_count(iter, func_get_keys):
    """Count the instances of some arbitrary attribute among an iter's items"""
    key_to_count = {}
    for item in iter:
        keys = func_get_keys(item)
        for key in keys:
            key_to_count[key] = key_to_count.get(key, 0) + 1
    return key_to_count
