from project import simple, medium, complex


def test_simple():
    password  = simple(10)
    assert len(password) == 10



def test_medium():
    password= medium(9)
    assert len(password) == 9

def test_complex():
    password = complex(12)
    assert len(password) == 12
