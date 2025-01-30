from flask import Flask, Response  
from datetime import datetime
import json  

app = Flask(__name__)  

@app.route('/', methods=['GET'])  
def get_info():  
    response = {
        "email": "daniellamodukpe@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + 'Z', 
        "github_url": "https://github.com/dany-gaga/HNG12_task"  
    }  
    json_response = json.dumps(response)
    return Response(json_response, mimetype = 'application/json')  

if __name__ == '__main__':  
    app.run(debug=True)  