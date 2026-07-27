from fastapi import APIRouter
from schemas.battery import Battery,BatteryResponse

router = APIRouter()

@router.get('/')
def home():
    return {"message":"Battery Digital Twin Testing"}

# @app.get("/about")
# def about():
#     return {
#         "project":"AI Engineering Roadmap",
#         "author":"Harshit"
#     }

@router.get("/about")
def about():
    return {
        "project":"Battery Digital Twin",
        "author":"Harshit"
    }

@router.get("/battery/{battery_id}")
def get_battery(battery_id:int):
    return {'battery_id':battery_id}

# query 
@router.put("/battery/{battery_id}")
def update_battery(battery_id:int,battery:Battery):
    return {
        'message':f'Battery {battery_id} updated successfully',
        'battery':battery
    }

@router.delete("/battery/{battery_id}")
def delete_battery(battery_id:int):
    return {
        'message':f'Battery {battery_id} deleted successfully'
    }

@router.post("/battery",response_model=BatteryResponse,status_code=201)
def create_battery(battery:Battery):
    return battery
    