screen calendar_overlay():
    tag calendar
    style_prefix "calendar_overlay"
    zorder 2
    frame:
        has vbox
        text calendar.date.strftime(f"%B {calendar.get_ordinal()} | %a")
        text calendar.get_time() at transform:
            xalign 1.0

style calendar_overlay_frame:
    background "#00000090"
    align (0.995, 0.008)
    padding (14, 12)


screen day_change():
    tag calendar
    text "Day [calendar.day]" at transform:
        align (0.5, 0.38)
    text calendar.date.strftime(f"%A, %B {calendar.get_ordinal()}, 2XX{calendar.date.year % 10}") at transform:
        align (0.5, 0.45)

init python:
    import datetime

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

        def pass_time(self, blocks: Time = Time.MORNING) -> None:
            self.time = Time(self.time + blocks)
            if self.time > TIME_BLOCKS:
                days = self.time // TIME_BLOCKS
                remaining_time = Time(self.time % TIME_BLOCKS)
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
