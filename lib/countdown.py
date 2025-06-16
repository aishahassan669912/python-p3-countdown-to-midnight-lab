# your code goes here!
# lib/countdown.py

def countdown(start=10):
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -= 1
    print("HAPPY NEW YEAR!")
    return "HAPPY NEW YEAR!"


def countdown_with_sleep(start=10):
    import time
    while start > 0:
        print(f"{start} SECOND(S)!")
        time.sleep(1)
        start -= 1
    print("HAPPY NEW YEAR!")
    return "HAPPY NEW YEAR!"
