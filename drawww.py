import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que


def draw(record):
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

