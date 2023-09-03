"""
File: weather_master.py
Name: Eydie Cheng
-----------------------
This program should implement a console program
that asks whether data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
    """
    TODO: based on the degrees user input, the program will analyze the highest,
    lowest number, the average and cold days (less than 16 degree)
    among them. it ends when -100 is entered
    """

    print("stanCode \"Weather Master 4.0\"!")
    degree = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
    if degree == EXIT:
        print('No temperatures were entered.')
    else:

        high = degree
        low = degree
        sum_degree = degree
        count_degree = 1  # count the first step above
        cold = 0
        if degree < 16:  # whether the first time could be counted
            cold += 1
        while True:
            degree = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))

            if degree == EXIT:
                break
            if degree < 16:
                cold += 1
            if high < degree:
                high = degree
            if low > degree:
                low = degree

            sum_degree = sum_degree + degree
            count_degree += 1
        print('Highest temperature = ' + str(high))
        print('Lowest temperature = ' + str(low))
        print('Average = ' + str(float(sum_degree / count_degree)))
        print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
