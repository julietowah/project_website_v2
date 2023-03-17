from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB = [
  {
    "id": 1,
    "title": "accountant",
    "location": "lagos"
   
  },
  {
    "id": 2,
    "title": "web designer",
    "location": "lagos",
    "salary": "N350,000" 
  },
  {
    "id": 3,
    "title": "graphic design",
    "location": "Enugu",
    "salary": "N500,000" 
  }

]

@app.route("/")
def hello_world():
  return render_template('home.html', job=JOB)
  
@app.route("/job")
def list_job():
  return jsonify(JOB)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)