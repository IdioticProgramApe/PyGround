"""
1. Problem
----------

.. sort a dictionary based on its key(s)
"""

from operator import itemgetter


def test_itemgetter() -> None:
    """USE CASE
    
    normally, use :py:`lambda` function can also work since `key` parameter
    need a callable function to get the item
    
    still, :pymeth:`itemgetter` has a better performance.
    
    :pymeth:`min` and :pymeth:`max` have same usage as :pymeth:`sorted`.
    """
    
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    
    rows_by_name = sorted(rows, key=itemgetter('fname'))
    assert rows_by_name == [
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
    ]
    
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    assert rows_by_uid == [
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    
    # if multiple
    rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
    assert rows_by_lname == [
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}
    ]
    

"""
2. Problem
==========

.. sort different instances from a same class, 
   which hasn't the comparison method implemented.
"""

from operator import attrgetter

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        
    def __repr__(self) -> str:
        return f'User({self.user_id})'


def test_attrgetter() -> None:
    """USE CASE
    
    like :pymeth:`itemgetter`, :pymeth:`attrgetter` can accept multiple
    inputs, and has a better performance compared to :py:`lambda`.
    """
    
    users = [User(23), User(3), User(99)]
    sorted_users = sorted(users, key=attrgetter('user_id'))
    assert sorted_users[0].user_id == 3
    assert sorted_users[1].user_id == 23
    assert sorted_users[2].user_id == 99
