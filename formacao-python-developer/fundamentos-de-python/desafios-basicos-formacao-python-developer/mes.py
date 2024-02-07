month = int(input());

months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if 1 <= month <= 12:
    print(months_dict[month]);
else:
    print("Invalid input. Please enter a number between 1 and 12.");