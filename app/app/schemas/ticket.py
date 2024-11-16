from typing import Optional
from pydantic import BaseModel

class TicketCreate(BaseModel):
    purchase_id: int
    passenger_id: int
    ticket_code: str
    departure_time: str
    arrival_time: str
    status: Optional[str] = "issued"  

    class Config:

        orm_mode = True
        

class TicketResponse(BaseModel):
    id: int
    purchase_id: int
    passenger_id: int
    ticket_code: str
    departure_time: str
    arrival_time: str
    status: str

    class Config:
        orm_mode = True
        
        
class TicketUpdate(BaseModel):
    purchase_id: Optional[int]
    passenger_id: Optional[int]
    ticket_code: Optional[str]
    departure_time: Optional[str]
    arrival_time: Optional[str]
    status: Optional[str]

    class Config:
        orm_mode = True


class TicketDelet(BaseModel):
    purchase_id: Optional[int]
    passenger_id: Optional[int]
    ticket_code: Optional[str]
    departure_time: Optional[str]
    arrival_time: Optional[str]
    status: Optional[str]

    class Config:
        orm_mode = True