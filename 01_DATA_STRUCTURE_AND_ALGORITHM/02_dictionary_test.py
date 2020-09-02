"""
1. Problem
==========

.. We want to create a subjected dictionary.

*subjective dictionary* is a dictionary 
where one key can map to multiple values,
therefore it has an another name `multidict`.
"""

from collections import defaultdict

def test_defaultdict() -> None:
    """USE CASE
    
    Compare the following codes
    ---------------------------

    .. code-block:: python
        :linenos:
        
        d = {}
        for key, value in pairs:
            if key not in d:
                d[key] = []
            d[key].append(value)
        
    .. code-block:: python
        :linenos:
        
        d = default(list)
        for key, value in pairs:
            d[key].append(value)  
    """
    
    # 1. in these multiple values, it can have same values
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(1)
    d['a'].append(4)
    assert d == {'a': [1, 1, 4]}


    # 2. in these multiple values, each one of them is unique
    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(1)
    d['a'].add(4)
    assert d == {'a': {1, 4}}

    # 3. if for each key, it maps to different data structure...
    d = {}
    d.setdefault('a', list()).append(1)
    d.setdefault('a', list()).append(1)
    d.setdefault('b', set()).add(2)
    d.setdefault('b', set()).add(2)
    assert d == {'a': [1, 1], 'b': {2}}


"""
2. Problem
==========

.. create a dictionary which can control the item order
   (same when perform recursive or sequential ops)
"""

from collections import OrderedDict

def test_ordereddict() -> None:
    """USE CASE
    
    Since :py:class:`OrderedDict` has internally a *Doubly linked list*，
    compared to ordinary :py:class:`dict`, it's twice bigger in term of size
    
    Need to think whether what :py:class:`OrderedDict` brings can overcome 
    its shortage in size.
    """
    
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    keys = ['grok', 'spam', 'bar', 'foo']
    for key in d:
        assert key == keys.pop()
    

"""
3. Problem
==========

.. min, max, sort. etc ops in `dict`
"""

def test_dictorderops() -> None:
    """USE CASE
    
    Use :pymeth:`zip` to invert `keys` and `values` in a `dict`,
    and then use :pymeth:`min` and :pymeth:`max` get the results.
    
    Be aware of that :pymeth:`zip` generates a one-time iterator, 
    can *only* be used once.
    """
    
    price = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # Get the cheapest and the most expensive stock
    min_price = min(zip(price.values(), price.keys()))
    assert min_price == (10.75, 'FB')

    max_price = max(zip(price.values(), price.keys()))
    assert max_price == (612.78, 'AAPL')
    
    
"""
4. Problem
==========

.. &, - etc set ops

However values in dict do not support set ops 
because values can allow duplicates.
""" 

def test_dictsetops() -> None:
    """USE CASE
    
    Filter some keys in a dictionary
    
    .. code-block:: python
        :linenos:
        
        c = {key: a[key] for key in a.keys - {'z', 'w'}}
    """
    
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    
    # find keys in common
    common_keys = a.keys() & b.keys()
    assert common_keys == {'x', 'y'}
    
    # find keys in a that not in b
    diff_keys = a.keys() - b.keys()
    assert diff_keys == {'z'}
    
    # find (key, value) pair in common
    common_pair = a.items() & b.items()
    assert common_pair == {('y', 2)}
