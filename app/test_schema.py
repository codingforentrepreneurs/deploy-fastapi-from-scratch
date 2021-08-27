import schema
import pytest
from pydantic import parse_obj_as
from pydantic.error_wrappers import ValidationError
from typing import List

def test_entry_create_schema_valid():
    data = {"title": "Hello world"}
    obj = schema.EntryCreateSchema(**data)
    assert obj.title == data['title']


def test_entry_create_schema_strips_data_valid():
    data = {"title": "Hello world", "abc": "123"}
    obj = schema.EntryCreateSchema(**data)
    obj_keys = obj.dict().keys()
    assert len(obj_keys) == 2
    assert set(obj_keys) != set(data.keys())
    


def test_entry_create_schema_title_len_valid():
    max_length = 100
    title_ = "".join(["a" for x in range(max_length)])
    data = {"title": title_}
    schema.EntryCreateSchema(**data)

def test_entry_create_schema_title_len_invalid():
    max_length = 100
    with pytest.raises(ValidationError):
        title_ = "".join(["a" for x in range(max_length + 1)])
        data = {"title": title_}
        schema.EntryCreateSchema(**data)


def test_entry_create_schema_invalid():
    with pytest.raises(ValidationError):
        data = {"content": "Hello world"}
        schema.EntryCreateSchema(**data)


def test_entries_list_schema_invalid_ids():
    items = [
        {"title": "Hello world", "content": "again"},
        {"title": "Hello worlder", "content": "abc"},
    ]
    with pytest.raises(ValidationError):
        obj_list = parse_obj_as(List[schema.EntryListSchema], items)


def test_entries_list_schema_valid_ids():
    items = [
        {"id": 1, "title": "Hello world", "content": "again"},
        {"id": 2, "title": "Hello worlder", "content": "abc"},
    ]
    obj_list = parse_obj_as(List[schema.EntryListSchema], items)
    first_obj = obj_list[0]
    assert len(first_obj.dict().keys()) == 5