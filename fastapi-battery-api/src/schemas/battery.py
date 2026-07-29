from pydantic import BaseModel

class Battery(BaseModel):
    battery_id:int | None = None
    voltage:float | None = None
    current:float | None = None
    temperature:float | None = None

class BatteryResponse(BaseModel):
    battery_id: int
    voltage:float