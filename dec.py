from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)
user= "manoj"
main= "7OGijOnHjduC54qK3eiuPw=="
@app.route('/', methods=["GET", "POST"])
def home():
     return render_template('login.html')

@app.route('/amd', methods=["GET", "POST"])
def lol():
     passe= request.form["pswrd"]
     use= request.form["userid"];
     if passe==main and use==user :
      return "Login Successful"
     else: 
      return "Wrong password"




if __name__ == "__main__":
    app.run(debug=True)

