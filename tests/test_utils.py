import pytest
from src.utils import *


def test_get_executed_operations():
    assert get_executed_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert get_executed_operations([{}]) == []


def test_sort_operations_date():
    assert sort_operations_date([{"date": "2019-08-26T10:50:58.294041"}]) == [{"date": "2019-08-26T10:50:58.294041"}]


def test_change_date():
    assert change_date([{"date": "2019-08-26T10:50:58.294041"}]) == ["26.08.2019"]


def test_mask_card_number():
    assert (mask_card_number([{"from": "Maestro 1596837868705199", "description": "Перевод организации"}]) ==
            ["Maestro 1596 83** **** 5199"])


def test_mask_amount_number():
    assert mask_amount_number([{"to": "Счет 64686473678894779589"}]) == ["** 7958"]
