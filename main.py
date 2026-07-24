from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Battery(BaseModel):
    battery_id:int | None = None
    voltage:float | None = None
    current:float | None = None
    temperature:float | None = None

@app.get('/')
def home():
    return {"message":"Battery Digital Twin Testing"}

# @app.get("/about")
# def about():
#     return {
#         "project":"AI Engineering Roadmap",
#         "author":"Harshit"
#     }

@app.get("/about")
def about():
    return {
        "project":"Battery Digital Twin",
        "author":"Harshit"
    }

@app.get("/battery/{battery_id}")
def get_battery(battery_id:int):
    return {'battery_id':battery_id}

# query 
@app.put("/battery/{battery_id}")
def update_battery(battery_id:int,battery:Battery):
    return {
        'message':f'Battery {battery_id} updated successfully',
        'battery':battery
    }

@app.delete("/battery/{battery_id}")
def delete_battery(battery_id:int):
    return {
        'message':f'Battery {battery_id} deleted successfully'
    }

@app.post("/battery")
def create_battery(battery:Battery):
    return battery
    