import time
from main import hello



def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1


def test_hello_full_name():
    assert hello('Jane', 'Smith') == "Hello, Jane Smith!"


