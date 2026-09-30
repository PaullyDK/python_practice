nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if num % 10 == 1:
        print(f"{num}st")
    elif num % 10 == 2:
        print(f"{num}nd")
    elif num % 10 == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

    # I was thinking I'd make a metrics reporter application
    # maybe also some sort of ball game
    # well see