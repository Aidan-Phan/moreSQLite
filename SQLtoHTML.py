import _sqlite3 as sq

print('starting..')
cnn = None
filename = "employees.db"

try:
    cnn = sq.connect(filename)
    print('database connected..')
    sql = ("SELECT * FROM employees")
    
    cur = cnn.cursor()
    cur.execute(sql)
    rst = cur.fetchall()
    print('records selected..')

    for i in rst:
        print(i)
finally:
    if cnn:
        cnn.close()
print('done')