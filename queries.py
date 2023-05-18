# Топ 5 по виду деятельности по году, по месяцам
def query1(lima, date_year, start_date_mon, finish_date_mon):
    query1 = ("SELECT " + lima+ " , SUM(revenue) as rev FROM rent " +
               " where date_part('year', rent.date) = " + date_year + 
                " and date_part('month', rent.date) > " + start_date_mon +
                " and date_part('month', rent.date) < " +finish_date_mon +
                " group by " + lima + 
                " order by rev desc " +
                " limit 5" )
    return query1
