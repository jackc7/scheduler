from data import Data
import event_creator
import datetime
import yaml

with open("config.yml", "r") as config_yaml:
    config = yaml.load(config_yaml, Loader=yaml.FullLoader)

classes = config["classes"]
description = config["description"]
calendar_id = config["calendar_id"]


def day(day_number: int, day_of_school_year: int):
    if not Data.DAY[day_of_school_year]:
        return f"No school on day {str(day_of_school_year)}"
    
    print()
    
    # Constructs schedule for the day.        
    schedule = [[classes[Data.all_data(day_of_school_year)[2][x]], description[Data.all_data(day_of_school_year)[2][x]]] for x in range(5)]
    
    if datetime.date.fromordinal(737709 + day_of_school_year).weekday() == 2:
        class_times = Data.wednesday_times()
    else:
        class_times = Data.class_times()
    
    event_list = []

    for i, x in enumerate(class_times):
        event = {
            "summary": f"{schedule[i][0]}",
            "location": f"{schedule[i][1]}",
            "description": "Dedham High School",
            "start": {
                "dateTime": f"{Data.DATE[day_of_school_year]}T{x[0]}-04:00",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{Data.DATE[day_of_school_year]}T{x[1]}-04:00",
                "timeZone": "America/New_York",
            }
        }
        event_list.append(event)
    return event_list


def main():
    """Adds all classes to calendar."""

    pattern = Data.PATTERN

    print("Working... This will take a while.")
    for a, x in enumerate(Data.DAY):
        if not x:
            continue
        print(Data.DATE[a])
        pattern = Data.all_data(a)[2]

        for i in day(pattern[0], a):
            event_creator.new(i, calendar_id=calendar_id)
            print(i["summary"] + ", " + i["location"] + f"\n    Starts: " + i["start"]["dateTime"] + "\n    Ends: " + i["end"]["dateTime"])

        pattern = pattern[1:] + pattern[0:1]
if __name__ == "__main__":
    main()
