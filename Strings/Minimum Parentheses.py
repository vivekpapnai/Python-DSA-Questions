"""Given a string "pattern", which contains only two types of characters ‘(’, ‘)’. Your task is to find the minimum
number of parentheses either ‘(’, ‘)’ we must add the parentheses in string ‘pattern’ and the resulted string is
valid. Condition for valid string- Every opening parenthesis ‘(’ must have a correct closing parenthesis ‘)’.
 Example - ‘(()(()))’, ‘()()()’, ‘((()))’ are valid string, and ‘(((’, ‘(()’, ‘)(())’ are invalid string.
 Note: 1. You are not required to print the output explicitly, it has already been taken care of. Just implement the
 function and return the minimum number of parentheses required to make a string valid.

"""

def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.

    count = 0
    s = []
    for i in range(len(pattern)):
        if pattern[i] == '(':
            s.append(pattern[i])
        elif pattern[i] == ')':
            if len(s) != 0:
                s.pop()
            else:
                count += 1

    return len(s) + count


