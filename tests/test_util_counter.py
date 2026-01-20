from util.counter import Counter


def test_counter_increments_and_resets():
    counter = Counter()

    assert counter.get_next() == 1
    assert counter.get_next() == 2

    counter.reset()

    assert counter.get_next() == 1
