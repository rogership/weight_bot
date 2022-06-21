import datetime
import json
import os

def data_json(key: str, data: float, date="") -> json:
    """Receives data and dump on json file
    
    param: key: key to be inserted in dictionary
    param: data: data to be dumped on json file
    
    return json file on format {date: {key: data}}    
    """
    if not date:
        dateObj = datetime.date.today()
        date = f"{dateObj.day}/{dateObj.month}/{dateObj.year}"
        
    try:
        with open("data.json", "r") as f:
            content = json.load(f)
    except Exception as e:
        with open("data.json", "w+") as f:
            json.dump({}, f)
            content = {}
    
    with open("data.json", "w") as f:
        content[date] = {key: data}
        json.dump(content, f, indent=4)
    
    
if __name__ == "__main__":
    data_json("peso", 3, date="17/06/2022")
    data_json("peso", 4, date="18/06/2022")
    data_json("peso", 85, date="17/06/2022")
