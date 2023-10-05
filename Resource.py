import sqlite3
import pandas

def remove_duplicate_and_sort_lst(lst_tuple):
    lst = []
    for i in lst_tuple:
        lst.extend(list(i))
    lst.sort(reverse=True)
    lst = remove_duplicate(lst)
    return lst
def remove_duplicate(x):
  return list(dict.fromkeys(x))

def identify_pre_end_time(Pre_station, cur_startTime):
    # InputData:   Pre_station str cur_startTime int 
    # Output: [pre_endtime, pre_starttime]

    con = sqlite3.connect("Routine.db")
    c =con.cursor()

    # lọc dữ liệu resource 
    # lấy wc từ pre_station 
    c.execute('select work_center from routine where cur = (?)',[Pre_station])
    pre_wc = c.fetchone()
    print("pre_wc: ", pre_wc)

    if pre_wc == None:
        print("error prestation: ", Pre_station)
        return [(0.0,)]
    
    # lấy định mức nguồn lực từ pre_WC
    c.execute('select manpower from resource where wc_code = (?)',(pre_wc))
    resource_default = c.fetchone()
    # print('default resource: ',resource_default)

    #nguồn lực đang sử dụng
    c.execute('select manpower from routine where cur = (?)',[Pre_station])
    resource_usage = c.fetchone()

    # tinh gap
    c.execute('select ((setup_time + cycle_time + Waiting_Time)/manpower) as gap from routine where cur = (?)', [Pre_station])
    # gap = c.fetchone()
    gap = (1,)

    # pre end time = cur start time
    pre_endtime = cur_startTime
    
    c.execute('select count(erp) from routine where work_center = (?)', pre_wc)
    max_row = c.fetchone()

    for irow in range(1, max_row[0]+1):
        pre_starttime = pre_endtime - gap[0]
        pre_dt = (pre_wc[0], pre_endtime, pre_starttime)  # xem lại chỗ pre_station bên dưới
        print("pre_data -- (pre_wc[0], pre_endtime, pre_starttime, Pre_station): ", pre_dt)
        c.execute(''' 
                select sum(manpower) from routine
                            where work_center = (?)
                                and end >= (?)
                                and start <= (?)
                                AND check_node = TRUE
                ''', pre_dt)
        
        resource_max = c.fetchone()
        if resource_max == (None,):
            resource_max = (0.0,)
        
        print("resource_accumulate: ", resource_max)
        print("resource_usage: ", resource_usage)
        print("resource_default: ", resource_default)
        
        if ((resource_max[0] + resource_usage[0]) <= resource_default[0]): # 
            result = [pre_endtime, pre_starttime]
            return result
            break
        else:
            c.execute(''' select start, end
                    from Routine 
                    WHERE 
                    end <(?)
                    and work_center = (?)
                    and check_node = TRUE ''',( pre_endtime , pre_wc[0]))
            endtime_lst = c.fetchall()
            
            endtime_lst = remove_duplicate_and_sort_lst(endtime_lst)
            print(endtime_lst)
            if endtime_lst == []:
                pre_endtime = pre_starttime
            else:
                pre_endtime = max(endtime_lst)
                endtime_lst.remove(pre_endtime)
    con.commit()
    con.close()
