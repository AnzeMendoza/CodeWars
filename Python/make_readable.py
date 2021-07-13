# Write a function, which takes a non-negative integer (seconds)
# as input and returns the time in a human-readable format (HH:MM:SS)

#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59

# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.


def make_readable(seconds):
    # Do something
    sec = (seconds % 60)
    seconds -= sec
    minute = int(int(seconds % 3600) / 60)
    seconds -= 60*minute
    hour = int(seconds/3600)

    return(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}")

def make_readable2(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)

def main():
    make_readable(0)

if __name__ == "__main__":
    main()