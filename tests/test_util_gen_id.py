import time

import util.gen_id as gen_id
from util.now_ms import now_ms


def test_now_ms_returns_int_and_advances():
    first = now_ms()
    time.sleep(0.001)
    second = now_ms()

    assert isinstance(first, int)
    assert second >= first


def test_gen_id_increments_on_same_timestamp(monkeypatch):
    gen_id._last_ms = 0
    gen_id._inc = 0

    monkeypatch.setattr(gen_id, "now_ms", lambda: 123456789)

    first = gen_id.gen_id()
    second = gen_id.gen_id("suffix")

    assert first == "123456789.0"
    assert second == "123456789.1_suffix"
