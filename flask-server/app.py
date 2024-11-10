from flask import Flask, jsonify
import mysql.connector
import json
from pinotdb import connect

def db():
    # connect mysql
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root12345", database="sushmademo")
    if (mydb):
        mycursor = mydb.cursor()
        # create database if not exists
        mycursor.execute("CREATE DATABASE IF NOT EXISTS sushmademo")
        dbresult = []
        mycursor.execute('''SELECT * FROM WORKER''')
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        rv = mycursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        print("json.dumps(json_data)",json.dumps(json_data))
        # close connection of mycursor & mydb
        mycursor.close()
        mydb.close()
        print("dbresult1:",json.dumps(json_data))
        # return data from DB
        return json.dumps(json_data)

    else:
        return "Connection Error"


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to My API"


@app.route('/data', methods=['GET'])
def get():
    dbresult = db()
    import json
    with open('../data.json', 'w', encoding='utf-8') as f:
        json.dump(dbresult, f, ensure_ascii=False, indent=4)
        response = jsonify(dbresult)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


@app.route('/apache_pinot_transcripts', methods=['GET'])
def get_pinot_trans():
    conn = connect(host='34.71.204.44', port=8099)
    curs = conn.cursor()
    curs.execute("""select * from transcript""")
    row_headers=[x[0] for x in curs.description] #this will extract row headers
    rv = curs.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    print("json.dumps(json_data)",json.dumps(json_data))
    with open('../apachet.json', 'w') as f:
        json.dump(json_data, f)
    json_data = json.dumps(json_data)
    response = jsonify(json_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    curs.close()
    return response

@app.route('/apache_pinot', methods=['GET'])
def get_pinot():
    conn = connect(host='34.71.204.44', port=8099)
    curs = conn.cursor()
    curs.execute("""select * from callsdata""")
    row_headers=[x[0] for x in curs.description] #this will extract row headers
    rv = curs.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    print("json.dumps(json_data)",json.dumps(json_data))
    with open('../apache.json', 'w') as f:
        json.dump(json_data, f)
    json_data = json.dumps(json_data)
    response = jsonify(json_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    curs.close()
    return response

if __name__ == "__main__":
    app.run(port=5555,host='0.0.0.0',debug=False)

