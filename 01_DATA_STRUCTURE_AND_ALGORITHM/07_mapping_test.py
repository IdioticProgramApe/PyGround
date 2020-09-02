"""
1. Problem
==========

.. Sometimes if we always use postion like indices to visit elements
   or tuples, it can be quite confusing. Therefore we wish to use names
   to do the visit
"""

from collections import namedtuple

def test_namedtuple() -> None:
    """USE CASE
    
    using index to visit element often depends on the position,
    if we add extra data, the index will expire. But instead we use 
    :py:class:`namedtuple`, there won't be any problems
    
    .. code-block:: python
        :linenos:
        
        from collections import namedtuple
        
        Stock = namedtuple('Stock', ['name', 'shares', 'prices'])
        def compute_cost(records):
            total = 0.
            for rec in records:
                s = Stock(*rec)
                total += s.shares * s.prices
            return total
            
    of course, if `records` is a set of objects which contains 
    such attributes, there is no need to create :py:class:`namedtuple`.
    """
    
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    
    sub = Subscriber('python@example.com', '2020-09-02')
    assert sub.addr == 'python@example.com'
    assert sub.joined == '2020-09-02'
    assert len(sub) == 2
    
    addr, joined = sub
    assert addr == 'python@example.com'
    assert joined == '2020-09-02'
    
    sub = sub._replace(joined='2019-09-02')
    assert sub.joined == '2019-09-02'


"""
2. Problem
==========

.. Sometimes we have multiple mappings, and we want to merge them 
   to perform some op that need all of them
"""

from collections import ChainMap

import pytest

def test_chainmap() -> None:
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    
    c = ChainMap(a, b)
    assert set(c.keys()) == set(['z', 'y', 'x'])
    assert set(c.values()) == set([3, 2, 1])
    
    # the modification will always happend to the 1st mapping
    with pytest.raises(KeyError):
        del c['y']
        
    # scopes 
    values = ChainMap()
    values['x'] = 1
    
    values = values.new_child()
    values['x'] = 2
    
    values = values.new_child()
    values['x'] = 3
    
    for i in range(2, 0, -1):
        values = values.parents
        assert values['x'] == i
    