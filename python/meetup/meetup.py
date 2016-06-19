import datetime
import calendar

_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_abbr, madeup_word):
    day = None
    matrix = calendar.monthcalendar(year, month)

    # Get day index in week (Ex: Monday = 0, Tuesday = 1, ..., Sunday = 6)
    day_index = _days.index(day_abbr)

    # Get date between 10 and 20 days of the month
    if madeup_word == 'teenth':
        for week in matrix:
            if week[day_index] > 10 and week[day_index] < 20:
                day = week[day_index]
                break

    # Get date for last specified weekday in the month
    elif madeup_word == 'last':
        for week in matrix:
            if week[day_index] > 0:
                day = week[day_index]

    # 1st, 2nd, 3rd, 4th, 5th weekday
    else:
        day_pos = int(filter(str.isdigit, str(madeup_word)) or 0) or None
        if not day_pos:
            raise MeetupDayException()

        for week in matrix:
            if week[day_index] > 0:
                if day_pos == 1:
                    day = week[day_index]
                    break
                else:
                    day_pos = day_pos - 1

    if not day:
        raise MeetupDayException()

    try:
        meetup_date = datetime.date(year, month, day)
    except ValueError:
        raise MeetupDayException()

    return meetup_date
