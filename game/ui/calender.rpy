screen calendar():
    text "%s %s | %s\n%s"%(calendar.get_month(), calendar.get_ordinal_day(), calendar.get_weekday(3), calendar.get_time())

init python:
    class Calendar(object):
        def __init__(self, start_time: int = 1, start_day: int = 1, start_month: int = 1, start_year: int = 2000):
            self.game_day = 1
            self.time_block = start_time

            self.start_day = start_day
            self.start_month = start_month
            self.start_year = start_year

            self.day = start_day
            self.month = start_month
            self.year = start_year
            
            self.time_block_names = ["Morning", "Afternoon", "Evening", "Late Night"]
            
            self.day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            self.month_day_counts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def set_day(self, game_day: int = 1, start_time: int = 1):
            self.game_day = game_day
            self.day = self.start_day
            self.month = self.start_month
            self.year = self.start_year
            self.next_day(days=game_day - 1, start_time=start_time)

        def next_day(self, days: int = 1, start_time: int = 1):
            self.time_block = start_time
            self.game_day += days
            self.day += days
            day_count = self.month_day_counts[self.month - 1]
            if self.day > day_count:
                self.month += self.day // day_count
                if self.month > 12:
                    self.month = 1
                    self.year += 1
                self.day = self.day % day_count

        def advance(self, time_blocks: int = 1):
            self.time_block += time_blocks
            if self.time_block > 4:
                days = self.time_block // 4
                remainder = self.time_block % 4
                self.next_day(days=days, start_time=remainder)

        def get_time(self):
            return self.time_block_names[self.time_block - 1]

        def get_weekday(self, max_characters: int):
            day_list_index = self.game_day % 7
            day_name = self.day_names[day_list_index]
            if max_characters is not None:
                day_name = day_name[:max_characters]
            return day_name 

        def get_month(self):
            return self.month_names[self.month - 1]

        def get_ordinal_day(self):
            return to_ordinal(self.day)
    
    def to_ordinal(number: int):
        if 11 <= (number % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(number % 10, 4)]

        return str(number) + suffix