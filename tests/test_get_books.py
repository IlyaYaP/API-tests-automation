import pytest
import json
from conftest import ResponseValidate
from schemas.books_schemas import Books, Book

def test_get_books(booker_api):
    r = booker_api.get("/booking")
    response = ResponseValidate(r)
    response.assert_status_code(200)
    response.validate(Books)

def test_get_book(booker_api):
    r = booker_api.get("/booking/1")
    response = ResponseValidate(r)
    response.assert_status_code(200)
    response.validate(Book)
    print(r.json())