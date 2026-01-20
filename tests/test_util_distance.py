from util.distance import Distance


def test_distance_round_trip():
    ingame = 128.0
    meters = Distance.from_ingame_to_meters(ingame)
    converted = Distance.from_meters_to_ingame(meters)

    assert meters == ingame / 64.0 * 0.9144
    assert converted == ingame
