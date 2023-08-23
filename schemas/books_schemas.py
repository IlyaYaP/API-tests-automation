from pydantic import BaseModel
from pydantic import Field
from typing import Union

class Books(BaseModel):
    bookingid: int


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class Book(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Union[str, None]