from sys import stdin


# Test Cases definition

# Test framework with assertions

def test():
    # Test cases
    cases = [([], True),

             ([1, 2, 3, 4, 5], False),

             ([5, 4, 3, 2, 1], True),

             ([1, 2, 3, 10, 9, 8, 7, 20, 21, 22, 100, 99, 77, 65, 32], True),

             ]

    # Expected solutions
    solutions = [[],

                 [5, 4, 3, 2, 1],

                 [1, 2, 3, 4, 5],

                 [1, 2, 3, 7, 8, 9, 10, 20, 21, 22, 32, 65, 77, 99, 100]

                 ]

    # Test executions
    for case in range(len(cases)):
        assert insertionSort(cases[case][0], cases[case][1]) == solutions[case]

    return True


# Insertion sort algorithm implementation
def insertionSort(sequence, ordDirection):
    result = sequence

    # If the sequence is ordered, then result is the sequence itself
    for i in range(1, len(result)):
        # Order the sub-sequence A[0..i-1] inserting A[i]
        j, change = i - 1, i
        while j >= 0 and (result[change] < result[j] if (ordDirection) else result[change] > result[j]):
            result[change], result[j] = result[j], result[change]
            change -= 1
            j -= 1
    return result


def input():
    # Read the sequence separated by spaces
    sequence = [int(x) for x in stdin.readline().strip().split(' ')]

    if (sequence == ['']):
        return None

    # Read the direction of ordering
    direction = stdin.readline().strip()
    direction = True if (direction == 'ASC') else False

    # Return the tuple (A[i..N], Direction)
    return sequence, direction


# Format the output from a sequence as a space separated string
def output(sequence):
    return ' '.join([str(x) for x in sequence])


# main Entry
def main():
    userInput = input()

    while userInput != None:
        solution = insertionSort(userInput[0], userInput[1])

        userOutput = output(solution)

        print(userOutput)

        userInput = input()


if (test()):
    main()

"""Input examples

1 2 3 4 5 6 10 2 3 4 5 6 100 99 98 97 96 95 94 93

ASC

1 2 3 4 5

ASC

4 3 2 1

DESC

1 2 3 10 9 8 7 20 21 22 100 99 77 65 32

ASC

"""
