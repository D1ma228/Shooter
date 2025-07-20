import json 

def read_file():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data 
        
    except:
        return{
            "skin": "rocket.png",
            "money": 0

        }
    

def save_file(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False)
    