import ollama
import json
# import jsonify
from fastapi import FastAPI
from pydantic import BaseModel


# Example usage: Provide a list of ingredients
"""user_ingredients = ["tomatoes", "onions", "garlic", "basil"]
recipes = generate_recipes(Item(title="Vegan Dinner Party", items=user_ingredients, quantities=5))
print(recipes)


class Item(BaseModel):
    title: str
    items: str
    quantities: float"""

app = FastAPI()

@app.get("/planmeals")
def return_string(cusine: str| None = None, leftovers: str| None = None, serving: int=0, meal: int=0, dietaryrestrictions: str | None = None):
    print(cusine)
    get_data = cusine + '_' + leftovers + '_' + str(serving) + '_' + str(meal) + '_' + dietaryrestrictions
    print(get_data)
    data = generate_meals(get_data)
    return(data)


def generate_meals(get_data):
    input_prompt = 'Your are a chef with decades of experience. You are required to return ten recipes. You will be provided with a string with words separated by underscores containing requirements that these recipes must adhere to. You will return a json response with three fields the title, items and quantity. They quantities are to be in mg, kg, ml or lr where appropriate.'
    input =  input_prompt + get_data
    response = ollama.generate(model='llama3', stream=False, prompt = input)
    pretty_data = response["response"]
    return(pretty_data)

#item = Item(title="Vegan Dinner Party", items="Vegan recipes", quantities=5)
#print(create_item(item))
