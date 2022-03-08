"""Time utils."""
import datetime
import time

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
FORMAT_DATE = '%Y-%m-%d'
FORMAT_DATE_ID = '%Y%m%d'


class SECONDS_IN:
    """Units of time."""

    MINUTE = 60
    HOUR = 3600
    DAY = 86400
    WEEK = 7 * 86400
    FORTNIGHT = 14 * 86400
    MONTH = 365.25 * 4 * 86400 / 12
    QTR = 365.25 * 86400 / 4
    YEAR = 365.25 * 86400


def get_timezone():
    """Get timezone."""
    return str(datetime.datetime.now().astimezone().tzinfo)


def get_unixtime():
    """Get current unixtime."""
    return (int)(time.time())


def parse_time(
    time_str,
    time_format=DEFAULT_TIME_FORMAT,
):
    """Parse time string, and return unixtime."""
    _datetime = datetime.datetime.strptime(time_str, time_format)
    return (int)(time.mktime(_datetime.timetuple()))


def format_time(
    unixtime,
    time_format=DEFAULT_TIME_FORMAT,
):
    """Format unixtime as time string."""
    _datetime = datetime.datetime.fromtimestamp(unixtime)
    return _datetime.strftime(time_format)


def format_current_date_with_timezone():
    """Format date with timezone."""
    date = format_time(get_unixtime(), '%B %d, %Y %H:%M%p')
    timezone = get_timezone()
    return '{date} {timezone}'.format(date=date, timezone=timezone)


def get_date_id(unixtime=None):
    """Get date id."""
    if unixtime is None:
        unixtime = get_unixtime()
    return format_time(unixtime, FORMAT_DATE_ID)


def parse_date_id(date_id):
    return parse_time(date_id, FORMAT_DATE_ID)


def get_date(unixtime=None):
    """Get date id."""
    if unixtime is None:
        unixtime = get_unixtime()
    return format_time(unixtime, FORMAT_DATE)


