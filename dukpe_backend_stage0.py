from flask import Flask, jsonify  
from flask_cors import CORS  
from datetime import datetime  

app = Flask(__name__)  
CORS(app)  # Enable CORS for all routes  

@app.route('/', methods=['GET'])  
def get_info():  
    response = {  
        "email": "daniellamodukpe@gmail.com",  # Replace with your email  
        "current_datetime": datetime.utcnow().isoformat() + 'Z',  
        "github_url": "https://github.com/dany-gaga/HNG12_task"  # Update with your GitHub URL  
    }  
    return jsonify(response)  

if __name__ == '__main__':  
    app.run(debug=True)  