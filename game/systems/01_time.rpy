init python:
    from enum import Enum

    class Time(int, Enum):
        MORNING = 1, "Morning", "#fbff84"
        AFTERNOON = 2, "Afternoon", "#FFFFFF"
        EVENING = 3, "Evening", "#bc16a3"
        NIGHT = 4, "Late Night", "#690c5b"
        DREAMING = 5, "Dreaming", "#0099ff"

        def __new__(cls, value, label, color):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.label = label
            obj.color = color
            return obj

        @classmethod
        def from_str(cls, input_str):
            for cl in cls:
                if cl.label == input_str:
                    return cl
            raise ValueError(f"{cls.__name__} has no value matching {input_str}")

    TIME_BLOCKS = len(Time)
    