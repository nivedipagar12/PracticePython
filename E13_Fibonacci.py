'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 13 : Fibonacci (https://www.practicepython.org/)
                      Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
                      Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
                      the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
                      numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
                      The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


# Ask the user for their desired length of the fibonacci series
length = int(input("Enter the number of elements you want in your fibonacci series : "))
sum = 0
last_sum = 1

# Initialize the list with the first element
series = [1]


'''Function to generate a fibonacci series with a given length'''


def fibonacci_series(length):
    '''generates a fibonacci series with the desired length

        Parameters
        -----------
        length: int
                length of the desired list

        Returns
        -----------
        None
        '''
    global sum, last_sum

    # length -1 because you already have one element in the list
    for i in range(length-1):

        # calculate the sum of the last two elements
        new_sum = sum + last_sum

        # increment the index
        sum = last_sum
        last_sum = new_sum

        # Add each element to the list
        series.append(new_sum)
    print(series)


fibonacci_series(length)
