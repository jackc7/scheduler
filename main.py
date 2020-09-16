from data import Data
import event_creator

# Instructions to get started:  

# Open main.py.  
# Fill in classes, description, and calendar_id.  
# Run main.py.

# List names of periods from 1 to 7 here 
classes = {
    1:"Wood 2",
    2:"Forensic Science",
    3:"English 4",
    4:"Study", 
    5:"Economics", 
    6:"AP Environmental Science", 
    7:"Calculus"
    }

description = { # Optional: Leave strings blank for nothing.
    1:"Period 1",
    2:"Period 2",
    3:"Period 3",
    4:"Period 4", 
    5:"Period 5", 
    6:"Period 6", 
    7:"Period 7"
    }

# Find your Calendar ID and put it here. Leave as None to use your default calendar.
calendar_id = "bbghk1ec8mrg8etls5vfbemh2g@group.calendar.google.com"

def day(day: int, day_of_school_year: int):
    if not Data.DAY[day_of_school_year]:
        return f"No school on day {str(day_of_school_year)}"
    
    # Very bad code, ignore.
    if   day == 1: schedule = [[classes[1], description[1]],[classes[7], description[7]],[classes[6], description[6]],[classes[5], description[5]],[classes[4], description[4]]]
    elif day == 2: schedule = [[classes[2], description[2]],[classes[1], description[1]],[classes[7], description[7]],[classes[6], description[6]],[classes[5], description[5]]]
    elif day == 3: schedule = [[classes[3], description[3]],[classes[2], description[2]],[classes[1], description[1]],[classes[7], description[7]],[classes[6], description[6]]]
    elif day == 4: schedule = [[classes[4], description[4]],[classes[3], description[3]],[classes[2], description[2]],[classes[1], description[1]],[classes[7], description[7]]]
    elif day == 5: schedule = [[classes[5], description[5]],[classes[4], description[4]],[classes[3], description[3]],[classes[2], description[2]],[classes[1], description[1]]]
    elif day == 6: schedule = [[classes[6], description[6]],[classes[5], description[5]],[classes[4], description[4]],[classes[3], description[3]],[classes[2], description[2]]]
    elif day == 7: schedule = [[classes[7], description[7]],[classes[6], description[6]],[classes[5], description[5]],[classes[4], description[4]],[classes[3], description[3]]]
    else: return "Not a valid day. Only accepts integer between 1 and 7."
    
    class_times = [["07:35:00", "08:35:00"], ["08:40:00", "09:40:00"], ["09:45:00", "10:45:00"], ["11:25:00", "12:25:00"], ["12:30:00", "13:30:00"]]
    event_list = []
    
    for i in range(5):
        event = {
            "summary": f"{schedule[i][0]}",
            "location": f"{schedule[i][1]}",
            "description": "Dedham High School",
            "start": {
                "dateTime": f"{Data.DATE[day_of_school_year]}T{class_times[i][0]}-04:00",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{Data.DATE[day_of_school_year]}T{class_times[i][1]}-04:00",
                "timeZone": "America/New_York",
            }
        }
        event_list.append(event)
    return event_list

def first_month():
    pattern = Data.PATTERN

    for a in range(41):
        if not Data.DAY[a]:
            continue
        
        for i in day(pattern[0], a):
            event_creator.new(i, calendar_id=calendar_id)
        
        pattern = pattern[1:] + pattern[0:1]

if __name__ == "__main__":
    first_month()