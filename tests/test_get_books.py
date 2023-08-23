import pytest
import json
from conftest import ResponseValidate
from schemas.books_schemas import Books, Book
from books_data import create_booking_data


def test_get_books(booker_api):
    r = booker_api.get("/booking")
    response = ResponseValidate(r)
    response.assert_status_code(200)
    response.validate(Books)


def test_get_book(booker_api):
    r = booker_api.get("/booking/1")
    print(r.json())
    response = ResponseValidate(r)
    response.assert_status_code(200)
    response.validate(Book)


@pytest.mark.create_booking
def test_create_booking(booker_api):
    json = create_booking_data
    r = booker_api.post("/booking", json=json)
    response  = ResponseValidate(r)
    print(r.json())