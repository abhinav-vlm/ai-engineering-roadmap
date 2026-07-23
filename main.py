from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message":"Hello"}

@app.get("/about")
def about():
    return {
        "project":"AI Engineering Roadmap",
        "author":"Harshit"
    }

@app.get("/battery/{battery_id}")
def get_battery(battery_id:int):
    return {'battery_id':battery_id}

# query 
@app.get("/students")
def get_roll_marks(roll_no:int,marks:int):
    return {
        'roll_no':roll_no,
        "marks":marks
    }