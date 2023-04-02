from flask import Flask,render_template,request
import pickle
from model import Recommendation
import pymysql as sql


app= Flask(__name__)

conn=sql.connect(host='localhost',port=3306,user='root',password='Jaishree',db='STUDENT')

con=conn.cursor()

model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def main():
   return render_template("index.html")


@app.route("/login",methods=["POST",'GET'])
def login():
    if request.method == "POST":
        username=request.form['user']
        password=request.form['pass']
        con.execute("select * from login where username=%s and password=%s",(username,password))
        a=con.fetchone()
        if a:
            return render_template("input.html")
        else:
            return render_template("index.html",msg='Invalid user/password!!!!')


@app.route('/recommend',methods=['POST','GET'])
def recommend():
    name=request.form['name']
    data=model.predict(name)
    return render_template("output.html",data=data)

'''if __name__=='__main__':
    app.run(port=3300)'''
    
if __name__=="__main__":
    app.run(debug=True)
    