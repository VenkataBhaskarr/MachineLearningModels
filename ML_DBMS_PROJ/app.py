from flask import Flask,render_template,request
# from flask_mysqldb import MySQL
import pickle
import numpy as np

# export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
model = pickle.load(open('iri.pkl','rb'))
app = Flask(__name__)


app.config['MYSQL_HOST']     = '127.0.0.1'
app.config['MYSQL_USER']     = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB']       = 'testSet'
# mysql = MySQL(app)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/indexing')
def dunno():
    return render_template('indexing.html')
@app.route('/datas',methods=['GET', 'POST'])
def datas():
    if request.method == 'POST':
      data11 = request.form['a']
      data21 = request.form['b']
      data31 = request.form['c']
      data41 = request.form['d']
      data51 = request.form['e']
      data61 = request.form['sub']
      data71 = request.form['prof']
    #   cur = mysql.connection.cursor()
    #   cur.execute("INSERT INTO `Professors` VALUES (%s,%s,%s,%s,%s,%s,%s)",(data61,data71,data11,data21,data31,data41,data51))
    #   mysql.connection.commit()
      return "success"
    return render_template('datas.html')


@app.route('/predict',methods=['POST'])
def indexing():
    maindata = request.form['subject']
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    arr = np.array([[data1,data2,data3,data4,data5,data6]])
    pred = model.predict(arr)

    return render_template('after.html',data = pred)


if __name__ == '__main__':
    app.run(debug=True)