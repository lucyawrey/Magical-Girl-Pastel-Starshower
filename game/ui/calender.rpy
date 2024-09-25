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
    import datetime

    class Calendar(object):
        def __init__(self, start_year: int = 2000, start_month: int = 1, start_day: int = 1, start_time: int = 1, day_skips_dict: dict = None):
            self.day = 1
            self.time_block = start_time

            self.day_skips_dict = day_skips_dict
            self.start_date = datetime.datetime(year=start_year, month=start_month, day=start_day)
            self.date = self.start_date
            
            self.time_block_names = ["Morning", "Afternoon", "Evening", "Late Night"]

        def set_day(self, day: int = 1, start_time: int = 1) -> None:
            self.day = day
            self.date = self.start_date
            if day > 1:
                self.next_day(day - 1, start_time)

        def set_time(self, time_block: int = 1) -> None:
            self.time_block = time_block

        def next_day(self, days: int = 1, start_time: int = 1) -> None:
            skip_sum = 0
            if self.day_skips_dict is not None:
                for i in range(self.day + 1, self.day + days + 1):
                    if i in self.day_skips_dict:
                        skip_sum += self.day_skips_dict[i] - 1
            self.date = self.date + datetime.timedelta(days=days + skip_sum)
            self.day += days
            self.time_block = start_time

        def advance(self, time_blocks: int = 1) -> None:
            self.time_block += time_blocks
            if self.time_block > 4:
                days = self.time_block // 4
                remainder = self.time_block % 4
                self.next_day(days=days, start_time=remainder)

        def get_time(self) -> str:
            return self.time_block_names[self.time_block - 1]

        def get_ordinal(self) -> str:
            number = self.date.day
            if 11 <= (number % 100) <= 13:
                suffix = 'th'
            else:
                suffix = ['th', 'st', 'nd', 'rd', 'th'][min(number % 10, 4)]
            return str(number) + suffix
