"""
1. Problem
==========

.. There is a sequence of dictionary or object instances, 
   we want to group these data based on some specific field
"""

from operator import itemgetter
from itertools import groupby


def test_groupdata() -> None:
    """USE CASE
    
    to use :pymeth:`groupby`, we need to first sort the data by specific
    field(s), and then, :pymeth:`groupby` can check each element and
    group them
    
    however, if what we want is only categorize the data,
    using :py:class:`defaultdict(list)` could be a better choice.
    """
    
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
    ]
    
    # 1st step: sort the data by field 'date'
    rows.sort(key=itemgetter('date'))
    
    # 2nd step: group the items sharing the same date
    
    checklist = {
        '07/04/2012': [
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
        ],
        '07/03/2012': [
            {'address': '2122 N CLARK', 'date': '07/03/2012'}
        ],
        '07/02/2012': [
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'}
        ],
        '07/01/2012': [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
        ]
    }
    
    for date, item in groupby(rows, key=itemgetter('date')):
        date_, item_ = checklist.popitem()
        assert date == date_
        
        for i, i_ in zip(item, item_):
            assert i == i_


"""
2. Problem
==========

.. based on the actual use, sometimes we need to modify/filter the data
   using some specific rules
"""

from itertools import compress
from typing import Any

def test_filterdata() -> None:
    """USE CASE
    
    if the filter rules are quite obvious can use the generator or
    the list comprehension to solve the problem
    
    .. example 1:
   
       >>> # simplest method: using list comprehension
       >>> mylist = (1, 4, -5, 10, -7, 2, 3, -1)
       >>> [n for n in mylist if n > 0]
       [1, 4, 10, 2, 3]
       >>> [n for n in mylist if n < 0]
       [-5, -7, -1]
    
    .. example 2:
    
       >>> # can store the filtered information in a generator
       >>> pos = (n for n in mylist if n > 0)
    """
    
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    
    def is_int(val: str) -> bool:
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    
    ivals = list(filter(is_int, values))
    assert ivals == ['1', '2', '-3', '4', '5']
    

def test_compress() -> None:
    
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE'
    ]
    
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    
    more5 = [n > 5 for n in counts]
    compressed_addresses = list(compress(addresses, more5))
    assert compressed_addresses == [
        '5800 E 58TH', 
        '1060 W ADDISON',
        '4801 N BROADWAY'
    ]