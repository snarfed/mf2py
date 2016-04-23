# coding: utf-8

from __future__ import unicode_literals, print_function

import iso8601
from icalendar import Calendar, Event, vDatetime

def parse_result_to_calendar(parsed):
    calendar = Calendar()
    for item in parsed['items']:
        if 'h-event' in item['type']:
            event = Event()
            if 'name' in item['properties'].keys() and len(item['properties']['name']) > 0:
                event['summary'] = item['properties']['name'][0]
            if 'start' in item['properties'].keys() and len(item['properties']['start']) > 0:
                event['dtstart'] = convert_dt(item['properties']['start'][0])
            if 'end' in item['properties'].keys() and len(item['properties']['end']) > 0:
                event['dtend'] = convert_dt(item['properties']['end'][0])
            calendar.add_component(event)
    return calendar

def convert_dt(dt):
    return vDatetime(iso8601.parse_date(dt, default_timezone=None))
