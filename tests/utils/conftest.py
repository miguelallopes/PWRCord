import pytest


@pytest.fixture
def example_dict():
    return {
        "op": 4,
        "d": {
            "guild_id": None,
            "channel_id": None,
            "self_mute": True,
            "self_deaf": False,
            "self_video": False,
        },
    }


@pytest.fixture
def example_valid_json_string():
    return '{"op": 4, "d": {"guild_id": null, "channel_id": null, "self_mute": true, "self_deaf": false, "self_video": false}}'


@pytest.fixture
def example_valid_json_bytes():
    return b'{"op": 4, "d": {"guild_id": null, "channel_id": null, "self_mute": true, "self_deaf": false, "self_video": false}}'


@pytest.fixture
def example_invalid_json_string():
    return '{"op":4,"d":{"guild_id":Null,"channel_id":null,"self_mute":true,"self_deaf":false,"self_video":false}}'


@pytest.fixture
def example_invalid_json_bytes():
    return b'{"op":4,"d":{"guild_id":Null,"channel_id":null,"self_mute":true,"self_deaf":false,"self_video":false}}'
