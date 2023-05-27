import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que


def plot(record):
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

def pie(record):
    citiyes =[]
    vals = []
    i=0
    while i < len(record):
        citiyes.append(record[i][0])
        vals.append(record[i][1])
        i+=1
    print(citiyes)
    print(vals)
    #print(sum(rev))
    fig1, ax1 = plt.subplots()
    ax1.pie(vals, labels=citiyes)
    plt.show()