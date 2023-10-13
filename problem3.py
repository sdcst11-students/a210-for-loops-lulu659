#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
x = int(input("Enter a number smaller than 10: "))
sum1 = 0
series = 0
for i in range(1, x + 1):
    series = series + pow(10, i-1)
    sum1 = sum1 + series
print("The sum of series is ",sum1)