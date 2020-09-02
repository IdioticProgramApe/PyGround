"""
1. Problem
==========

.. remove the duplicates, maintain the original order at the same time
   in a sequence

A *sequence* is a container, can be `list`, `set`, etc. 
"""
from typing import Any, Hashable, Iterable, Callable

def dedupe(
    items: Iterable[Any], 
    key: Callable[[Any], Hashable] = None
) -> Any:
    """Remove the duplicates in a sequence without change order

    :param items: input sequence needs processing
    :type items: Iterable[Any]
    :param key: callback function to make input hashable, defaults to None
    :type key: Callable[[Any], Hashable], optional
    :yield: return hashable value from key if key is not `None`
    :rtype: Iterator[Any]
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            

def test_dedupe() -> None:
    """USE CASE
    
    what's more, if the task doesn't have order requirement,
    a simple :py:class:`set` is enough
    
    since :py:class:`set` will remove the duplicate during its creation.
    """
    
    # 1. basic use, without callback function
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    assert list(dedupe(a)) == [1, 5, 2, 9, 10]
    
    # 2. with a key callback function
    b = [{'x': 1, 'y': 2}, 
         {'x': 1, 'y': 3}, 
         {'x': 1, 'y': 2}, 
         {'x': 2, 'y': 4}]
    
    dedupe_b = [{'x': 1, 'y': 2},
                {'x': 1, 'y': 3},
                {'x': 2, 'y': 4}]
    
    assert list(dedupe(b, key=lambda d: (d['x'], d['y']))) == dedupe_b
    
    # 3. try an another key callback on same sequence
    dedupe_b_2 = [{'x': 1, 'y': 2},
                  {'x': 2, 'y': 4}]
    
    assert list(dedupe(b, key=lambda d: d['x'])) == dedupe_b_2
    

"""
2. Problem
----------

.. To remove the hard coded index slince, 
   the hard code is bad for readability and future maintenance.
"""


def test_slice() -> None:
    """USE CASE
    
    :py:class:`slice` will generate a indexing object,
    it has 3 basic methods, :pymeth:`start`, :pymeth:`stop`,
    :pymeth:`step` and :pymeth:`indices`
    
    :pymeth:`indices` will automatically map the slice to a specific size
    without causing boundary overstep
    
    .. example 1:
       
       >>> items = [0, 1, 2, 3, 4, 5, 6]
       >>> a = slice(2, 4)
       >>> items[2:4]
       [2, 3]
       >>> items[a]
       [2, 3]
       >>> items[a] = [10, 11]
       >>> items
       [0, 1, 10, 11, 4, 5, 6]
       >>> del items[a]
       [0, 1, 4, 5, 6]
       
    .. example 2: 
       
       >>> a = slice(10, 50, 2)
       >>> a.start
       10
       >>> a.stop
       50
       >>> a.step
       2
       
    .. example 3:
    
       >>> s = 'HelloWorld'
       >>> a.indices(len(s))
       (5, 10, 2)
       >>> for i in range(*a.indices(len(s))):
       ...     print(s[i])
       ...
       W
       r
       d
       >>> 
    """
    
    # a made-up flat file 
    # (a type record which doesn't have relations between data)
    record = '....................100 ................513.25.........'
    
    SHARES = slice(20, 23)
    PRICE = slice(40, 46)
    
    cost = int(record[SHARES]) * float(record[PRICE])
    assert cost == 51325.

