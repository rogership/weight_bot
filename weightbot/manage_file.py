from datetime import datetime, date as dt
import json
from pathlib import Path
from collections import OrderedDict

def man_json(key: str, data: float, date="") -> json:
    """Receives data and dump on json file
       create file if it not exist
    
    param: key: key to be inserted in dictionary
    param: data: data to be dumped on json file
    param: file:
    param: date:
    
    return json file on format {date: {key: data}}    
    """
    #file = "/home/roger/Projetos/weight_bot/weightbot/data/data.json"
    file = Path("data/data.json")
    #file.mkdir(parents=True, exist_ok=True)
    
    
    if not date:
        dtObj = dt.today()
        date = f"{dtObj.strftime('%d/%m/%Y')}"
        
    try:
        with open(f"{file}", "r") as f:
            content = json.load(f)
    except Exception as e:
        with open(f"{file}", "w") as f:
            json.dump({}, f)
            content = {}
    
    with open(f"{file}", "w") as f:
        content[date] = {key: data}
        ordered = OrderedDict(sorted(content.items(), key = lambda x:datetime.strptime(x[0], '%d/%m/%Y')))
        json.dump(ordered, f, indent=4)
    
    
if __name__ == "__main__":
    man_json("peso", 3, date="17/06/2022")
    man_json("peso", 4, date="18/06/2022")
    man_json("peso", 85, date="17/06/2022")
    man_json("peso", 86)
    man_json("peso", 100, date="10/07/2022")
