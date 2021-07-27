from typing import Dict
import json as _json
import datetime as dt
def get_all_events() -> Dict:
    with open("events.json", encoding='utf-8') as events_file:
        data = _json.load(events_file)

    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "Month does not exist"

def get_day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        day_events = events[month][str(day)]
        return day_events
    except KeyError:
        return "Day does not exist"
    
def get_today_events():
    today = dt.date.today()
    month = today.strftime("%B")
    return get_day_events(month, today.day)