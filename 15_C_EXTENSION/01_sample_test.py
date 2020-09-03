import _sample_wrapper as sample
    
    
def test_gcd() -> None:
    assert 7 == sample.gcd(35, 42)
    
def test_in_mandel() -> None:
    assert 1 == sample.in_mandel(0., 0., 500)
    assert 0 == sample.in_mandel(2., 1., 500)
    
def test_divide() -> None:
    assert (5, 2) == sample.divide(42, 8)
    
def test_avg() -> None:
    assert 2. == sample.avg([1., 2., 3.])
    
def test_distance() -> None:
    p1 = sample.Point(1, 2)
    p2 = sample.Point(4, 5)
    assert abs(sample.distance(p1, p2) - 4.242640687119285) < 1e-15

