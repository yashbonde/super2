"""
These are a bunch of primary functions with a twist. Helps getting lot of repetetive
block coding out of the way.
@yashbonde - 28th July, 2020
"""

def map2(*func, data):
    raise NotImplementedError()

listfilter_equal = lambda _list, _key, _val: list(filter(lambda x: x.get(_key) == _val, _list))
listfilter_notequal = lambda _list, _key, _val: list(filter(lambda x: x.get(_key) != _val, _list))