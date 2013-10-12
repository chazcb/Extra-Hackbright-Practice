list_of_things = [
    'a',
    'b',
    ['a', 'b', ['c', 'd']],
    1,
    2,
    3,
    [1, 2, 5, ['d', 'b', 'c']],
]


def count_unique(some_iterable):
    """
    Returns a dictionary where the keys are unique items found within the
    passed nested list, and the value of each key is the number of times
    that item shows up in the passed nested list.

    For example:
        >>> count_unique(['a', [2, 'a', 'c', ['b', 'd']], 'b'])
        {'a': 2, 2: 1, 'c': 1, 'b': 2, 'd': 1}
    """
    return {}

print count_unique(list_of_things)


def common_items(list1, list2):
    """
    Returns a dictionary of all items found in both nested list1 and nested list2.

    The dictionary's key is the item, and the value is the sum of the number of times the
    item appears in each list.

    For example:
        >>> common_items(['a', 'b', 'b', 'c'], ['a', 'b', 'd'])
        {'a': 2, 'b': 3}
    """
    return {}

print common_items(list_of_things, [1, 2, 'b', 'c', ['q', 5]])


def merge_dictionaries(some_iterable):
    """
    Given a list of dictionaries, merge each dictionary into the previous
    dictionary such that the last dictionary's keys override the previous.

    For example:
        >>> merge_dictionaries([{'a': 1, 'b': 2}, {'a': 3}, {'a': 4}])
        {'a': 4, 'b': 2}
    """
    return {}

print merge_dictionaries([{'a': 1, 'b': 2, 'c': 3}, {'a': 'doge'}, {'b': 'wow'}, {'z': 'trasure', 'b': 'so wow'}])
