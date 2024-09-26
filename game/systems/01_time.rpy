init python:
    from enum import Enum

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

    TIME_BLOCKS = len(Time)
    