from fastapi import FastAPI
from enum import Enum # Importing FastAPI and enum for creating an API

app = FastAPI()

class AvailableCuisines(str, Enum):
    indian = "indian"
    chinese = "chinese"
    italian = "italian"

food_items = {
    "indian": ["Biryani", "Paneer Tikka", "Samosa"],
    "chinese": ["Noodles", "Spring Rolls", "Dumplings"],
    "italian": ["Pizza", "Pasta", "Lasagna"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine, "Cuisine not found")

# New endpoint: Get cuisine for a given food item
@app.get("/find_cuisine/{item_name}")
async def find_cuisine(item_name: str):
    item_name_lower = item_name.lower()
    for cuisine, items in food_items.items():
        if any(item.lower() == item_name_lower for item in items):
            return {
                "item": item_name,
                "cuisine": cuisine,
                "all_items_in_cuisine": items
            }
    return {"message": "Food item not found in any cuisine."}


        





"""from fastapi import FastAPI
app = FastAPI()
@app.get("/hello/{name}") #First API endpoint
async def hello(name):
    return f"Welcome To FastAPI {name}"
"""