#!/usr/bin/python3
import psycopg2
from flask import *
from werkzeug.contrib.fixers import ProxyFix
import sys
import secrets

app=Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/post_message', methods=['GET','POST'])
def post_message():
        
        if request.method=='POST':
            print("request")
            print(type(request.form))
            save_in_database(request.get_json())

        return redirect('/')
@app.route('/get_messages',methods=['GET'])
def get_messages():
    print("to do")
    out = jsonify(print_chat())
    print(out)
    return out
def save_in_database(messages):
    try:
        print("what the database got")
        print(messages)
        
        cursor.execute("INSERT INTO messages (messages,subject) VALUES (%s,%s)",
            (messages['messages'],messages['subject']))
        conn.commit()
    except:
        print(sys.exc_info()[0])




#prints chat to list of list objects
#format:
#[("messages":"foo","subject":"bar")..]
def print_chat():
    out_list = []
    try:
        cursor.execute("SELECT messages,subject FROM messages;")

        while(True):#fetching data 
            data=cursor.fetchone()
            print(data)
            if(data is None):
                break
            message=""
            subject=""
            username=""
            try:
                message=data[0]
            except:
                print("message not found")
            try:
                subject=data[1]
            except:
                print("subject not found")
            try:
                username=data[2]
            except:
                print("username not found")
            out_data={"messages":message,"subject":subject,
            "username":username}

            out_list.append(out_data);
            print(data)
        print(out_list)
    except:
        print(sys.exc_info()[0])
        print("oops")
    return out_list
conn = psycopg2.connect(dbname="chat",user=secrets.user,password=secrets.password,host=secrets.host)
cursor = conn.cursor()
print(cursor.execute('SELECT * FROM messages'))
rows=cursor.fetchall()
print(rows)


temp_args=""
if len(sys.argv)==1:
	temp_args=sys.argv[0]

if __name__ == '__main__': 
	if temp_args=="debug":
		app.debug=True
		app.run(host='0.0.0.0',port=5000,debug=True)
	else:
		app.wsgi_app = ProxyFix(app.wsgi_app)
		app.run()
