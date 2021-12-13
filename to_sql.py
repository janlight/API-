import os

from dotenv import load_dotenv, find_dotenv
import psycopg2

load_dotenv(find_dotenv())  

connection = psycopg2.connect(
    host = os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)



import csv, codecs




cur = connection.cursor()
cur.execute("DROP TABLE IF EXISTS heartdisease;")

create_table = """CREATE TABLE heartdisease (
                            Id INT PRIMARY KEY,
                            HeartDiseaseorAttack FLOAT,
                            HighBP FLOAT,
                            HighChol FLOAT,
                            BMI FLOAT,
                            Smoker FLOAT,
                            Stroke FLOAT,
                            PhysActivity FLOAT,
                            Fruits FLOAT,
                            GenHlth FLOAT,
                            Sex FLOAT,
                            Age FLOAT,
                            GreenVege FLOAT,
                            Asthma FLOAT
                            )"""
    
    
cur.execute(create_table)


read_list = []
read_list_col = []
with open('heart_disease_health_indicators_BRFSS2015(codestates3).csv', 'r') as f:
    file_read = csv.reader(f, delimiter=',')
    line_count = 0
    for line in file_read:
        if line_count == 0:
            read_list_col.append(line)
        else:    
            read_list.append(line)
        line_count += 1            

for i in range(len(read_list)):
    read_list[i].insert(0,i)   

for row in read_list:
    cur.execute("""
    INSERT INTO heartdisease (Id, HeartDiseaseorAttack, HighBP, HighChol, BMI, Smoker, Stroke, PhysActivity, Fruits, GenHlth, Sex, Age, GreenVege, Asthma)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",row)

connection.commit()