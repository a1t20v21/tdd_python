def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 != 0:
            return True
    return False

if __name__ == '__main__':
    year = input('Enter an year: ')
    if leap_year(int(year)):
        print('{0} is a leap year'.format(year))
    else:
        print('{0} is not a leap year'.format(year))