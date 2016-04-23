from __future__ import unicode_literals, print_function

import nose
from mf2py.parser import Parser

def test_get_empty_icalendar_when_no_hevents():
    p = Parser(doc=open("test/examples/person_with_url.html"))
    cal = p.to_icalendar()
    assert len(cal.subcomponents) == 0

def test_get_icalendar():
    p = Parser(doc=open("test/examples/icalendar.html"))
    cal = p.to_icalendar()
    assert len(cal.subcomponents) == 1
    #assert cal.subcomponents[0]['SUMMARY'] == "Microformats meetup"
    with open("/Users/tom/tmp/test.ics", "w") as f:
        f.write(cal.to_ical())
