# Project :- Days Calculator

from datetime import date

start_date = input("Enter Start Date: ")
end_date = input("Enter End Date: ")


def totalDays(start_date, end_date):

    if "-" not in start_date and end_date:
        return -1
    else:
        start = [int(day) for day in start_date.split("-")]
        end = [int(day) for day in end_date.split("-")]

        date1 = date(start[2], start[1], start[0])
        date2 = date(end[2], end[1], end[0])

        return date2-date1


if __name__ == '__main__':
    print(totalDays(start_date, end_date))

