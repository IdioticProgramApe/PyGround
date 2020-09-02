"""
1. Problem
----------

.. we have a sequence (container), 
   and we want to know which element most frequently appears
"""

from collections import Counter

def test_counter() -> None:
    """USE CASE
    
    :py:class:`Counter` can accept all hashable objects as inputs
    and return a :py:class:`dict` stores the mapping 
    between elements and their occurrence.
    
    .. example 1:
       
       >>> word_count['not']
       1
       >>> word_count['eyes']
       8
    
    .. example 2:
       
       >>> morewords = [
       ...    'why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes'
       ... ]
       ...
       >>> word_count.update(morewords)
       
    .. example 3:
       
       >>> a = Counter(words)
       >>> b = Counter(more_words)
       >>> a
       Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 
                'around': 2, "you're": 1, "don't": 1, 'under': 1, 'not': 1})
       >>> b
       Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 
                'you': 1, 'my': 1, 'why': 1})
       >>> # subtract counts
       >>> a - b
       Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 
                'around': 2, "you're": 1, "don't": 1, 'under': 1})
       >>> # combine counts
       >>> a + b
       Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
                'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1, 
                'looking': 1, 'are': 1, 'under': 1, 'you': 1})
    """
    
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 
        'my', 'eyes', "you're", 'under'
    ]
    
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    assert top_three == [('eyes', 8), ('the', 5), ('look', 4)]
