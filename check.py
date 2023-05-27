import matplotlib.pyplot as plt
import queries as que

#cityes = [ "KRR", "AAQ", "AER"]
#vals = [279123530.19, 120408540.56, 2081275193.21]
#fig1, ax1 = plt.subplots()
#ax1.pie(vals, labels=cityes)
#plt.show()


def draw(record):
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


draw(que.pie(lima = "city", pokaz = "revenue", date_year='2022', start_date_mon="1",finish_date_mon="3"))