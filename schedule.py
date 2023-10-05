import PySimpleGUI as sg
import pandas as pd
import sqlite3
import Resource



def printall(data):
    print('Print all line: ')
    for item in data:
        print(item,'\n')

def LPS():
    con = sqlite3.connect("Routine.db")
    c =con.cursor() 
    # xử lý dữ liệu đầu vào
    c.execute("select * from Routine")
    c.execute('update routine set end = 0')
    c.execute('update routine set start = 0')
    c.execute('update routine set check_node = False')
    c.execute('update routine set check_node = 1 where rowid = 1')
    c.execute('select max(rowid) from routine')
    con.commit()
    
    countID = c.fetchall()
    count = countID[0][0]

    for i in range(1, count+1):
        # processing time 
        sql = 'select setup_time+cycle_time+waiting_time from routine where rowid={}'.format(i)
        c.execute(sql)
        # pt = c.fetchall()
        pt = [(1,)]

        # current start time 
        sql = 'select end from routine where rowid = {}'.format(i)
        c.execute(sql)
        endtime =c.fetchall()
        print("line: ",i, ' \t cur end time:', endtime[0][0])
        starttime =endtime[0][0]-pt[0][0]

        # update start time  
        lst = (str(starttime),str(i))
        c.executemany('update routine set start = (?) where rowID = (?)', [lst])

        # pre-station 
        sql = 'select pre from routine where rowid = {}'.format(i)
        c.execute(sql)
        pres = c.fetchall()

        # lap va chen end time cho tram ke tiep = start time tram hien tai 
        if pres==None:
            continue
            
        # xử lý dữ liệu pres
        if str(pres).find('|') ==-1:
            pres = [(str(pres[0][0])+"|",)]
        print("cac tram con: ",pres)
        
        # ghi thoi gian end time theo mã pre_station
        for pre in pres[0][0].split('|'):
            
            # lựa trạm cho pre_station để chèn thời gian kết thúc
            if pre =="" or pre == "None":
                break
            c.execute('select end from routine where cur = (?)',[pre])
            pre_endtime = c.fetchall()
            
            # xu ly loi end time 
            if pre_endtime==[]:
                pre_endtime=[(0.0,)]

            # xác định thời gian trống để sắp công việc -- them ham vao day
            # pre_endtime = str(min(starttime,pre_endtime[0][0]))
            result = Resource.identify_pre_end_time(pre, starttime )

            pre_endtime = result[0]
            pre_starttime = result[1]
            print("pre_startion: ", pre, "\t identify pre end time output pre_endtime : ", pre_endtime)

            # chèn công việc
            c.execute('update routine set end =(?), start=(?) where cur = (?)',(pre_endtime, pre_starttime, pre))
            c.execute("UPDATE  Routine  set check_node = TRUE WHERE  cur =(?)",[pre])
            con.commit()
    c.execute('select * from routine')
    items = c.fetchall()
    # printall(items)

    con.commit()
    con.close()

LPS()