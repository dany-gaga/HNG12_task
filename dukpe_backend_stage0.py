from flask import Flask, jsonify  
from flask_cors import CORS  
from datetime import datetime 
from collections import OrderedDict 

app = Flask(__name__)  
CORS(app)  # Enable CORS for all routes  

@app.route('/', methods=['GET'])  
def get_info():  
    response = OrderedDict([  
        ("email": "daniellamodukpe@gmail.com"),  
        ("current_datetime": datetime.utcnow().isoformat() + 'Z'),  
        ()"github_url": "https://github.com/dany-gaga/HNG12_task")  
                           ]) 
    return jsonify(response)  

if __name__ == '__main__':  
    app.run(debug=True)  