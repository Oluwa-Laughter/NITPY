"""
Attendance taking script
"""

from typing import List

attendees: List[str] = ["Abike", "Bernard", "Christoper"]
waitlist: List[str] = ["Fuad", "Erika", "Frank"]


def take_attendance(name: str) -> bool:
    """
    This function takes the attendance of a person using thier name.
    Returns [True] if the person is registered.
    """
    if name in attendees:
        return True
    elif name in waitlist:
        # Add name to the attendees list
        attendees.append(name)
        waitlist.remove(name)
        return True
    else:
        return False


if __name__ == "__main__":
    name = ""
    while name != "stop":
        name = input("Enter name:")
        is_registered = take_attendance(name)
        print(is_registered)
