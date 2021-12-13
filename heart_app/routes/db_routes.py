from flask import Blueprint, render_template,request

import pandas as pd
import os

from dotenv import load_dotenv, find_dotenv
import psycopg2




bp = Blueprint('db', __name__, url_prefix='/db')

@bp.route('/',methods=['GET','POST'],strict_slashes=False)

def db_search():
    load_dotenv(find_dotenv())  

    connection = psycopg2.connect(
    host = os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
    )

                                                                                
    cur = connection.cursor()
    data0 = request.form['heartdiseaseorattack']
    data1 = request.form['highbp']
    data2 = request.form['highchol']
    data3 = request.form['bmi']
    data4 = request.form['smoker']
    data5 = request.form['stroke']
    data6 = request.form['physactivity']
    data7 = request.form['fruits']
    data8 = request.form['genhlth']
    data9 = request.form['sex']
    data10 = request.form['age']
    data11 = request.form['greenvege']
    data12 = request.form['asthma']
    


    
    
    read_list = [float(data0),float(data1), float(data2), float(data3), float(data4),
    float(data5), float(data6), float(data7), float(data8),float(data9), float(data10), float(data11),float(data12)]
    

    
    cur.execute("""
    INSERT INTO heart_disease (heartdiseaseorattack, highbp, highchol, bmi, smoker, stroke, physactivity, fruits, genhlth, sex, age, greenvege, asthma)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",read_list)

    connection.commit()
    
    
    
    return render_template('message.html',video_file="video/pulseT1.mp4")
