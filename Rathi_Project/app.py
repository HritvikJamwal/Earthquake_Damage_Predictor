from flask import Flask,request,render_template
import joblib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/input_data',methods=['POST','GET'])
def predict():
    
    filename = 'finalized_model.sav'
    loaded_model = joblib.load(filename)
    filename = 'scaler.sav'
    scaler=joblib.load(filename)
    
    a=request.form['field1']
    b=request.form['field2']
    c=request.form['field3']
    d=request.form['field4']
    e=request.form['field5']
    f=request.form['field6']
    g=request.form['field7']
    h=request.form['field8']
    
    x=[[a,b,c,d,e,f,g,h]]
    x=scaler.transform(x)
    result = loaded_model.predict(x)[0]
    print(result)
    if result ==5:
        return render_template('result.html',info='Grade: 5 (Reconstruction Required)')
    elif result==4:
       return render_template('result.html',info='Grade: 4 (Major Repair Required)')
    elif result==3:
       return render_template('result.html',info='Grade: 3 (Major Repair Required)')
    elif result==2:
       return render_template('result.html',info='Grade: 2 (Minor Repair Required)')
    elif result==1:
       return render_template('result.html',info='Grade: 1 (No Need of Repair)')
    
        
    
    
    
if __name__ == '__main__':
    app.run()