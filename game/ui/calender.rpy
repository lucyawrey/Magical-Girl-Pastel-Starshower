screen calendar_overlay():
    tag calendar
    text calendar.date.strftime(f"%B {calendar.get_ordinal()} | %a\n{calendar.get_time()}")

screen day_change():
    tag calendar
    text "Day [calendar.day]" at transform:
        align (0.5, 0.38)
    text calendar.date.strftime(f"%A, %B {calendar.get_ordinal()}, 2XX{calendar.date.year % 10}") at transform:
        align (0.5, 0.45)

init python:
    from enum import Enum
    import datetime

    class Time(int, Enum):
        MORNING = 1, "Morning"
        AFTERNOON = 2, "Afternoon"
        EVENING = 3, "Evening"
        NIGHT = 4, "Late Night"

        def __new__(cls, value, label):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.label = label
            return obj

        @classmethod
        def from_str(cls, input_str):
            for finger in cls:
                if finger.label == input_str:
                    return finger
            raise ValueError(f"{cls.__name__} has no value matching {input_str}")

    time_blocks = len(Time)

    class Calendar(object):
        def __init__(self, start_year: int = 2000, start_month: int = 1, start_day: int = 1, start_time: Time = Time.MORNING, day_skips_dict: dict = None):
            # In-game days elapsed since start of game
            self.day = 1
            # Current time, must be between 1-4
            self.time = start_time

            self.day_skips_dict = day_skips_dict
            self.start_date = datetime.datetime(year=start_year, month=start_month, day=start_day)
            self.date = self.start_date

        def set_day(self, day: int = 1, start_time: Time = Time.MORNING) -> None:
            self.day = day
            self.date = self.start_date
            if day > 1:
                self.next_day(day - 1, start_time)


        def next_day(self, days: int = 1, start_time: Time = Time.MORNING) -> None:
            skip_sum = 0
            if self.day_skips_dict is not None:
                for i in range(self.day + 1, self.day + days + 1):
                    if i in self.day_skips_dict:
                        skip_sum += self.day_skips_dict[i] - 1
            self.date = self.date + datetime.timedelta(days=days + skip_sum)
            self.day += days
            self.time = start_time

        def advance(self, blocks: Time = Time.MORNING) -> None:
            self.time = Time(self.time + blocks)
            if self.time > time_blocks:
                days = self.time // time_blocks
                remaining_time = Time(self.time % time_blocks)
                self.next_day(days=days, start_time=remaining_time)

        def get_time(self) -> str:
            return self.time.label

        def get_ordinal(self) -> str:
            number = self.date.day
            if 11 <= (number % 100) <= 13:
                suffix = 'th'
            else:
                suffix = ['th', 'st', 'nd', 'rd', 'th'][min(number % 10, 4)]
            return str(number) + suffix
