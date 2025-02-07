# Number Classification API
Project Description
This project provides an API that takes a number and returns interesting mathematical properties about it, along with a fun fact. The API checks if the number is prime, perfect, odd, or even, and identifies if it is an Armstrong number. Additionally, a fun fact related to the number is retrieved using the Numbers API.

Setup Instructions
Prerequisites
Python 3.6 or higher
pip (Python package installer)
Steps to Run Locally:
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Hansonnnadi/Number-Classification-API.git
cd Number-Classification-API
Create and activate a virtual environment (optional but recommended):

On Windows:
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
On Mac/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
uvicorn main:app --reload
The app should now be running on http://localhost:8000.

Example API Requests/Responses
1. Get Mathematical Properties of a Number
Request:

typescript
Copy
Edit
GET /api/classify-number?number=371
Response (200 OK):

json
Copy
Edit
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
2. Invalid Request
Request:

typescript
Copy
Edit
GET /api/classify-number?number=alphabet
Response (400 Bad Request):

json
Copy
Edit
{
  "number": "alphabet",
  "error": true
}
Deployment Link
You can access the live API at: Your Deployed API Link

Link to Numbers API Documentation
To get more information on the fun facts used in the API, visit the Numbers API Documentation.

