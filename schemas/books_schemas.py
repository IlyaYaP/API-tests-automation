from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate


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
    additionalneeds: str