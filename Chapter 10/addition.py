while True:
    print("Enter two numbers to add. Enter 'q' to stop.")
    first_input = input("First number: ")
    if first_input == 'q':
        break

    second_input = input("Second number: ")
    if second_input == 'q':
        break

    try:
        first_number = int(first_input)
        second_number = int(second_input)

        print(first_number + second_number)
    except ValueError:
        print("Please enter only valid integers.")