# HNG12_Stage_0
A journey with the HNG botcamp: https://hng.tech/hire/python-developers

## Description
This project is about building a simple API that shows my registered email address, the current datetime as an ISO 8601 formatted 
timestamp, and the GitHub URL of the project's codebase.

## Setup instructions
1. clone the repository in the specific directory where you would like the repository to be cloned:
   git clone https://github.com/dany-gaga/HNG12_task
2. In your local terminal navigate to the cloned directory using: cd HNG12_task
3. Install all dependencies in the requirements.txt file: `pip install -r requirements.txt`
4. Run the application using: python dukpe_backend_stage0.py

## API Endpoint  
https://dukpe.pythonanywhere.com/ 
  
### Example Response  
{
  "email": "daniellamodukpe@gmail.com",
  "current_datetime": "2025-01-30T10:21:54.148477Z",
  "github_url": "https://github.com/dany-gaga/HNG12_task"
}
