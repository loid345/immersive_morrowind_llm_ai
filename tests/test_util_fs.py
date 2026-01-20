from util.fs import read_json_cp1251, write_json_cp1251


def test_read_write_json_cp1251(tmp_path):
    payload = {"message": "Привет, Морровинд"}
    path = tmp_path / "data.json"

    result = write_json_cp1251(str(path), payload)

    assert result == payload
    assert read_json_cp1251(str(path)) == payload
