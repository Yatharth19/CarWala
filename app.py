import numpy as np
from flask import Flask,render_template,request
import pickle
# import sklearn

car_num=pickle.load(open('car_num.pkl','rb'))
fuel_num=pickle.load(open('fuel_num.pkl','rb'))
seller_type_num=pickle.load(open('seller_type_num.pkl','rb'))
transmission_num=pickle.load(open('transmission_num.pkl','rb'))
owner_num=pickle.load(open('owner_num.pkl','rb'))
predictor=pickle.load(open('predictor.pkl','rb'))



app=Flask(__name__)

@app.route('/')

def hello():
    return render_template('car.htm')

@app.route('/predict',methods=['POST'])
def predict():
    car_info = np.zeros(10)
    l=list()
    for x in request.form.values():
        l.append(x)
    car_info[2]=car_num[l[0]]                #name
    car_info[0]=int(l[1])           #year
    car_info[1]=int(l[2])           #km_driven
    car_info[3]=fuel_num[l[3]]                #fuel
    car_info[7]=float(l[4])                #mileage
    car_info[5]=transmission_num[l[5]]                #transmission
    car_info[8]=float(l[6])         #engine
    car_info[9]=float(l[7])         #max_power
    car_info[6]=owner_num[l[8]]                #owner
    car_info[4]=seller_type_num[l[9]]                #seller_type

    ans=predictor.predict([car_info])[0]
    return render_template('car.htm',car_price="Car Price Should be Rs.{}".format(ans))



if __name__ == "__main__":
    app.run(debug=True,port=5500)