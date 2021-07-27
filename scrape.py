import requests as _requests
import bs4 as _bs4
from typing import List
def _generate_url(month: str, day : int) -> str:
    url = f"https://www.onthisday.com/events/{month}/{day}"
    return url

def _get_page(url : str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    url = _generate_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all(class_ ="event")
    events = [event.text for event in raw_events]
    print(events)
    return events

events_of_the_day("december", 2)