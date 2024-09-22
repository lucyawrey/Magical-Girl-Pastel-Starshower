screen calendar():
    text "%s %s | %s\n%s"%(calendar.get_month(), calendar.get_ordinal_day(), calendar.get_weekday(3), calendar.get_time())

init python:
    class Calendar(object):
        def __init__(self, start_time_block=0, start_day=1, start_month=1, start_year=2000):
            self.game_day = 1

            self.time_block = start_time_block
            self.day = start_day
            self.month = start_month
            self.year = start_year
            
            self.time_block_names = ["Night", "Morning", "Afternoon", "Evening"]
            self.day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            self.days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
        def next_day(self):
            self.game_day += 1
            self.day += 1
            if self.day > self.days_count[self.month]:
                self.month += 1
                if self.month > 12: 
                    self.month = 1
                    self.year += 1
                self.day = 1

        def get_time(self):
            return self.time_block_names[self.time_block]

        def get_weekday(self, max_characters):
            day_list_index = self.day % 7
            day_name = self.day_names[day_list_index]
            if max_characters is not None:
                day_name = day_name[:max_characters]
            return day_name 

        def get_month(self):
            return self.month_names[self.month - 1]

        def get_ordinal_day(self):
            return to_ordinal(self.day)
    
    def to_ordinal(number):
        if 11 <= (number % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(number % 10, 4)]

        return str(number) + suffix