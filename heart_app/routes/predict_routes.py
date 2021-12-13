from flask import Blueprint, render_template,request
import pickle
import pandas as pd
bp = Blueprint('predict', __name__, url_prefix='/predict')

@bp.route('/', methods=['POST'],strict_slashes=False)

def predict():

    model = pickle.load(open('model.pkl','rb'))
    data0 = request.form['highbp']
    data1 = request.form['highchol']
    data2 = request.form['bmi']
    data3 = request.form['smoker']
    data4 = request.form['stroke']
    data5 = request.form['physactivity']
    data6 = request.form['fruits']
    data7 = request.form['genhlth']
    data8 = request.form['sex']
    data9 = request.form['age']
    data10 = request.form['greenvege']
    data11 = request.form['asthma']
    


    
    df_p = pd.DataFrame(
        data=[[float(data0),float(data1), float(data2), float(data3), float(data4),
        float(data5), float(data6), float(data7), float(data8),float(data9), float(data10), float(data11)]], 
        columns=['highbp','highchol','bmi','smoker','stroke','physactivity','fruits','genhlth','sex','age','greenvege','asthma']
    )

    # 예측
    pred = model.predict(df_p)[0]
    
    y_pred = int(pred)
    return render_template('predict.html', data=y_pred, video_file="video/pulseT.mp4")
