import icalendar

import json
import re

from datetime import datetime

# Group 1: Event name
# Group 2: Teacher
# Group 3: Something
# Group 4: Location
# Group 5: Event type
REGEX_TEXT = re.compile(r'<b>([A-Za-z0-9 ]+)<\/b><br>([A-Za-z ]+)<br>([A-Za-z0-9 -]+)<br><a href=\'.*\' >(\w+)<\/a><br>([A-Za-z0-9 /-]+)<br>')

events = json.loads(open('schedule.json').read()) # Load the JSON file

# Get text between starting and ending tags
def get_text_between_tags(text, start_tag, end_tag):
    start = text.find(start_tag) + len(start_tag)
    end = text.find(end_tag, start)
    return text[start:end]

calendar = icalendar.Calendar()

for event in events:
    matches = REGEX_TEXT.match(event['text'])

    name = matches.group(1)
    teacher = matches.group(2)
    location = matches.group(4)
    event_type = matches.group(5)

    # 2024-09-23T16:00:00
    start = event['start']
    end = event['end']

    start_date = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S')

    print(f'Name: {name}')
    print(f'Teacher: {teacher}')
    print(f'Location: Classroom {location}')
    print(f'Event type: {event_type}')

    # Add event to the calendar
    event = icalendar.Event()
    event.add('summary', name)
    event.add('dtstart', start_date)
    event.add('dtend', end_date)
    event.add('location', f'Classroom {location}')
    event.add('description', f'Teacher: {teacher}\nEvent type: {event_type}')

    # Set recurring event once every week
    event.add('rrule', {'freq': 'weekly'})

    calendar.add_component(event)

    print('---')

path_to_ics_file = 'schedule.ics'
with open(path_to_ics_file, 'wb') as f:
    f.write(calendar.to_ical())