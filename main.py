import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que

conn = psycopg2.connect(dbname='Rent', user='postgres', 
                        password='1234', host='localhost', port = "5432")
cursor = conn.cursor()
# Выполнение SQL-запроса
lima = "deal"
date_year = input("year")
start_date_mon = input("sd")
finish_date_mon = input("fd")
cursor.execute( que.query1(lima, date_year, start_date_mon, finish_date_mon))
# Получить результат
record = cursor.fetchmany(size=5)
print("htp ", record)
da =[]
rev = []
i=0
while i < len(record):
    da.append(record[i][0])
    rev.append(record[i][1])
    i+=1
print(da)
print(rev)
print(sum(rev))
plt.bar(da,rev, label = "Величина прибыли")
plt.show()

cursor.close()
conn.close()