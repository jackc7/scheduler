import datetime

class Data:
    """Days school is on and days it's off.
    Starts October 11, 2020
    https://www.dedham.k12.ma.us/cms/lib/MA02213180/Centricity/ModuleInstance/2803/20%2021%20Dedham%20School%20Calendar.pdf
    """

    #      Sun.    Mon.    Tues.   Wed.    Thurs.  Fri.    Sat.   # Saturday's Date
    DAY = [False,  False,  True,   True,   True,   True,   False, # 2020-10-17
           False,  True,   True,   True,   True,   True,   False, # 2020-10-24
           False,  True,   True,   True,   True,   True,   False, # 2020-10-31
           False,  True,   False,  True,   True,   True,   False, # 2020-11-07
           False,  True,   True,   False,  True,   True,   False, # 2020-11-14
           False,  True,   True,   True,   True,   True,   False, # 2020-11-21
           False,  True,   True,   True,   False,  False,  False, # 2020-11-28
           False,  True,   True,   True,   True,   True,   False, # 2020-12-05
           False,  True,   True,   True,   True,   True,   False, # 2020-12-12
           False,  True,   True,   True,   True,   True,   False, # 2020-12-19
           False,  True,   True,   False,  False,  False,  False, # 2020-12-26
           False,  False,  False,  False,  False,  False,  False, # 2021-01-02
           False,  True,   True,   False,  True,   True,   False, # 2021-01-09
           False,  True,   True,   True,   True,   True,   False, # 2021-01-16
           False,  False,  True,   True,   True,   True,   False, # 2021-01-23
           False,  True,   True,   True,   True,   True,   False, # 2021-01-30
           False,  True,   True,   True,   True,   True,   False, # 2021-02-06
           False,  True,   True,   True,   True,   True,   False, # 2021-02-13
           False,  False,  False,  False,  False,  False,  False, # 2021-02-20
           False,  True,   True,   True,   True,   True,   False, # 2021-02-27
           False,  True,   True,   False,  True,   True,   False, # 2021-03-06
           False,  True,   True,   True,   True,   True,   False, # 2021-03-13
           False,  True,   True,   True,   True,   True,   False, # 2021-03-20
           False,  True,   True,   True,   True,   True,   False, # 2021-03-27
           False,  True,   True,   True,   True,   False,  False, # 2021-04-03
           False,  True,   True,   True,   True,   True,   False, # 2021-04-10
           False,  True,   True,   True,   True,   True,   False, # 2021-04-17
           False,  False,  False,  False,  False,  False,  False, # 2021-04-24
           False,  True,   True,   True,   True,   True,   False, # 2021-05-01
           False,  True,   True,   True,   True,   True,   False, # 2021-05-08
           False,  True,   True,   True,   True,   True,   False, # 2021-05-15
           False,  True,   True,   True,   True,   True,   False, # 2021-05-22
           False,  True,   True,   True,   True,   True,   False, # 2021-05-29
           False,  False,  True,   True,   True,   True,   False, # 2021-06-05
           False,  True,   True,   True,   True,   True,   False, # 2021-06-12
           False,  True,   True,   True,   True,   True,   False, # 2021-06-19
           False,  True,   True,   True,   True,   True,   False] # 2021-06-26

    # List of all dates in ISO format, corresponds to DAY list above.
    # Ordinal 737709 = 2020-10-11
    DATE = [str(datetime.date.fromordinal(737709 + x)) for x in range(len(DAY))]
    
    PATTERN = [2, 4, 6, 1, 3, 5, 7]

    CLASS_PATTERN = {1: [1, 7, 6, 5, 4],
                     2: [2, 1, 7, 6, 5],
                     3: [3, 2, 1, 7, 5],
                     4: [4, 3, 2, 1, 7],
                     5: [5, 4, 3, 2, 1],
                     6: [6, 5, 4, 3, 2],
                     7: [7, 6, 5, 4, 3]}

    
    def class_times(lunch: int) -> list:
        
        # TODO - Change based on new schedule.
        times = [["07:35:00", "08:44:00"],
                 ["08:49:00", "09:58:00"],
                 ["10:03:00", "11:12:00"]]
        
        if lunch == 0:
            times.append(["11:17:00", "12:56:00"])
        elif lunch == 1:
            times.append(["11:47:00","12:56:00"])
        elif lunch == 2:
            times += [["11:17:00", "11:49:00"], ["12:24:00", "12:56:00"]]
        elif lunch == 3:
            times.append(["12:26:00", "12:56:00"])
            
        times.append(["13:01:00", "14:10:00"])
        
        return times
    
    def all_data(day: int = None) -> list:
        """If you leave day as None, it will return all days.
        If you set it to an integer, it will return the given day.
        Day 0 = October 11, 2020
        """

        all_list = []
        p = 0

        for i in range(len(Data.DAY)):
            if Data.DATE[i] == "2020-11-02":
                p -= 4
            elif Data.DATE[i] == "2021-04-05":
                p -= 6

            if Data.DAY[i]:
                day_number = Data.PATTERN[p%7]
                all_list.append([Data.DAY[i], Data.DATE[i], Data.CLASS_PATTERN[day_number]])
                p += 1
            else:
                all_list.append([Data.DAY[i], Data.DATE[i], None])
        if day is None:
            return all_list
        else:
            return all_list[day]
