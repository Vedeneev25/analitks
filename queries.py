import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que
import tkinter as tk
from tkinter import *
from tkinter import ttk

conn = psycopg2.connect(dbname='Rent', user='postgres', 
                        password='1234', host='localhost', port = "5432")
cursor = conn.cursor()
# Топ 5 по виду деятельности по году, по месяцам
def query1(lima, date_year, start_date_mon, finish_date_mon):
    query1 = ("SELECT " + lima+ " , SUM(revenue) as rev FROM rent " +
               " where date_part('year', rent.date) = " + date_year + 
                " and date_part('month', rent.date) >= " + start_date_mon +
                " and date_part('month', rent.date) <= " +finish_date_mon +
                " group by " + lima + 
                " order by rev desc " +
                " limit 5" )
    return query1

def query2 (lima, date_year, start_date_mon, finish_date_mon,revenue):
    query1 =("select" +lima +"."+lima+" sum" + revenue + "as rev from rent, city" +
            "where rent."+lima+" = city.city_id " +
            "and date_part('year', rent.date) = " + date_year + 
            "and date_part('month', rent.date) >= " + start_date_mon +
            "and date_part('month', rent.date) <= " + finish_date_mon +
            "group by city.city")



def cities():
    query = "SELECT city from city"
    cursor.execute(query)
    record = cursor.fetchmany(size=5)
    return record
