"""
To use this script. first use the setup.py in py_src to do a install,
after doing so, a module sample module will appear in your env
"""

import pytest
from array import array

import numpy as np

import sample

def test_capi_basics() -> None:
    assert 7 == sample.gcd(35, 42)
    assert 1 == sample.in_mandel(0., 0., 500)
    assert 0 == sample.in_mandel(2., 1., 500)
    assert (5, 2) == sample.divide(42, 8)


def test_capi_buffer() -> None:
    assert 2. == sample.avg(array('d', [1, 2, 3]))
    assert 2. == sample.avg(np.array([1., 2., 3.]))
    with pytest.raises(TypeError):
        assert 2. == sample.avg([1., 2., 3.])
    with pytest.raises(TypeError):
        assert 2. == sample.avg(b"HELLO")
    
    a = np.array([[1., 2., 3.], [4., 5., 6.]])
    with pytest.raises(ValueError):
        assert 4.5 == sample.avg(a[:, 2])
    with pytest.raises(TypeError):
        assert 3.5 == sample.avg(a)
    
    assert 2. == sample.avg(a[0])
        
        
def test_capi_capsule() -> None:
    p1 = sample.Point(2, 3)
    p2 = sample.Point(4, 5)
    assert type(p1).__name__ == 'PyCapsule'
    assert type(p2).__name__ == 'PyCapsule'
    
    d = sample.distance(p1, p2)
    assert abs(d - 2.8284271247461903) < 1e-15


def test_capi_ptexample() -> None:
    try:
        import ptexample
        p = sample.Point(2, 3)
        ptexample.print_point(p)
    except:
        assert 0
    assert 1
    