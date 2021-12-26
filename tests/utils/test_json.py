from importlib import import_module
from pwrcord.exceptions.validation import InvalidJsonError
from pwrcord.utils.json import ORJSON_AVAILABLE, JsonUtil
import pytest


def test_best_parser_detection():
    # Import the best library available for json
    module = None

    try:
        module = import_module("json")
    except ModuleNotFoundError:
        pass

    try:
        module = import_module("orjson")
    except ModuleNotFoundError:
        pass

    if module is None:
        raise ModuleNotFoundError("Cannot use any json parsing module")

    # Check if imported library is consistent with best available
    assert module.__name__ == "json" if not ORJSON_AVAILABLE else "orjson"


class TestJsonUtilValidation:
    # TODO invalid/valid Bytearray and PWRCordType

    def test_valid_json_string(self, example_valid_json_string):
        assert JsonUtil.validate(example_valid_json_string)

    def test_valid_json_bytes(self, example_valid_json_bytes):
        assert JsonUtil.validate(example_valid_json_bytes)

    def test_invalid_json_string(self, example_invalid_json_string):
        assert not JsonUtil.validate(example_invalid_json_string)

    def test_invalid_json_bytes(self, example_invalid_json_bytes):
        assert not JsonUtil.validate(example_invalid_json_bytes)

    def test_invalid_type(self):
        assert not JsonUtil.validate(1)


class TestJsonUtilEnsure:
    # TODO invalid/valid Bytearray and PWRCordType
    def test_dict_ensure_dict(self, example_dict):
        assert JsonUtil.ensure_dict(example_dict) == example_dict

    def test_valid_string_ensure_dict(self, example_valid_json_string, example_dict):
        assert JsonUtil.ensure_dict(example_valid_json_string) == example_dict

    def test_valid_bytes_ensure_dict(self, example_valid_json_bytes, example_dict):
        assert JsonUtil.ensure_dict(example_valid_json_bytes) == example_dict

    def test_invalid_string_ensure_dict(self, example_invalid_json_string):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_dict(example_invalid_json_string)

    def test_invalid_bytes_ensure_dict(self, example_invalid_json_bytes):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_dict(example_invalid_json_bytes)

    def test_invalid_type_ensure_dict(self):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_dict(1)

    def test_dict_ensure_string(self, example_dict, example_valid_json_string):
        if ORJSON_AVAILABLE:
            assert JsonUtil.ensure_string(
                example_dict
            ) == example_valid_json_string.replace(" ", "")
        else:
            assert JsonUtil.ensure_string(example_dict) == example_valid_json_string

    def test_valid_string_ensure_string(self, example_valid_json_string):
        assert (
            JsonUtil.ensure_string(example_valid_json_string)
            == example_valid_json_string
        )

    def test_valid_bytes_ensure_string(
        self, example_valid_json_bytes, example_valid_json_string
    ):
        assert (
            JsonUtil.ensure_string(example_valid_json_bytes)
            == example_valid_json_string
        )

    def test_invalid_string_ensure_string(self, example_invalid_json_string):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_string(example_invalid_json_string)

    def test_invalid_bytes_ensure_string(self, example_invalid_json_bytes):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_string(example_invalid_json_bytes)

    def test_invalid_type_ensure_string(self):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_string(1)

    def test_dict_ensure_bytes(self, example_dict, example_valid_json_bytes):
        if ORJSON_AVAILABLE:
            assert JsonUtil.ensure_bytes(
                example_dict
            ) == example_valid_json_bytes.replace(b" ", b"")
        else:
            assert JsonUtil.ensure_bytes(example_dict) == example_valid_json_bytes

    def test_valid_string_ensure_bytes(
        self, example_valid_json_string, example_valid_json_bytes
    ):
        assert (
            JsonUtil.ensure_bytes(example_valid_json_string) == example_valid_json_bytes
        )

    def test_valid_bytes_ensure_bytes(self, example_valid_json_bytes):
        assert (
            JsonUtil.ensure_bytes(example_valid_json_bytes) == example_valid_json_bytes
        )

    def test_invalid_string_ensure_bytes(self, example_invalid_json_string):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_bytes(example_invalid_json_string)

    def test_invalid_bytes_ensure_bytes(self, example_invalid_json_bytes):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_bytes(example_invalid_json_bytes)

    def test_invalid_type_ensure_bytes(self):
        with pytest.raises(InvalidJsonError):
            assert JsonUtil.ensure_bytes(1)
