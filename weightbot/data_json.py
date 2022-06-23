import datetime
import json
from pathlib import Path

def add_data(key: str, data: float, file: str, date="") -> json:
    """Receives data and dump on json file
       create file if it not exist
    
    param: key: key to be inserted in dictionary
    param: data: data to be dumped on json file
    param: file:
    param: date:
    
    return json file on format {date: {key: data}}    
    """
    file = "/home/roger/Projetos/weight_bot/weightbot/data/data.json"
    if not date:
        dbj = datetime.date.today()
        date = f"{dbj.day}/{dbj.month}/{dbj.year}"
        
    try:
        with open(f"{file}", "r") as f:
            content = json.load(f)
    except Exception as e:
        with open(f"{file}", "w+") as f:
            json.dump({}, f)
            content = {}
    
    with open(f"{file}", "w") as f:
        content[date] = {key: data}
        json.dump(content, f, indent=4)

def del_data(key: str, data: float, file: str, date="") -> json:
    """
    """    
    pass

if __name__ == "__main__":
    add_data("peso", 3, date="17/06/2022")
    add_data("peso", 4, date="18/06/2022")
    add_data("peso", 85, date="17/06/2022")
    add_data("peso", 86)
