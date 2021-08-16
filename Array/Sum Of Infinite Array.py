"""Given an array “A” of N integers and you have also defined the new array “B” as a concatenation of array “A” for
an infinite number of times. For example, if the given array “A” is [1,2,3] then, infinite array “B” is [1,2,3,1,2,3,
1,2,3,.......]. Now you are given Q queries, each query consists of two integers “L“ and “R”. Your task is to find
the sum of the subarray from index “L” to “R” (both inclusive) in the infinite array “B” for each query. Note : The
value of the sum can be very large, return the answer as modulus 10^9+7. Input Format : The first line of input
contains a single integer T, representing the number of test cases or queries to be run.

Then the T test cases follow.

The first line of each test case contains a single integer N, denoting the size of the array “A”.

The second line of each test case contains N single space-separated integers, elements of the array “A”.

The third line of each test case contains a single integer Q, denoting the number of queries.

Then each of the Q lines of each test case contains two single space-separated integers L, and R denoting the left and the  right index of the infinite array “B” whose sum is to be returned.
Output Format :
For each test case, print Q space-separated integers that denote the answers of the given Q queries. Print the answer to each test case in a separate line.
Note :
You do not need to print anything, it has already been taken care of. Just implement the given function.
Constraints :
1 <= T <= 100
1 <= N <= 10^4
1 <= A[i] <= 10^9
1 <= Q <= 10^4
1 <= L <= R <= 10^18

Time Limit: 1sec Sample Input 1 : 1 3 1 2 3 2 1 3 1 5 Sample Output 1 : 6 9 Explanation To Sample Input 1 : For the
first test case, the given array A is [1,2,3] therefore the infinite array “B” will be [1,2,3,1,2,3,1,2,3,
.......]. So the answer for the given first query is 6 because the sum of the subarray from index 1 to 3 of infinite
array “B” i.e. (B[1]+B[2]+B[3]) is 6.

For the given second query is 9 because the sum of the subarray from index 1 to 5 of array “B” .ie (B[1]+B[2]+B[3]+B[4]+B[5])
is 9.
Sample Input 2 :
1
4
5 2 6 9
3
1 5
10 13
7 11
Sample Output 2 :
27 22 28


https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381865

"""


def sum_range(x, n, pre_sum):
    mod = (10 ** 9) + 7
    count = (n // x) % mod  # it will count number of times the whole array is repeating
    result = (count * pre_sum[n]) % mod  # then count is multiplied with total sum of an array
    result += pre_sum[n % x]  # then we added the remaining sum in the result and return the array
    return result


def sumInRanges(arr, n, queries, q):
    pre_sum = [0 for i in range(n + 1)]  # initialising an array with 0 for pre_sum
    mod = (10 ** 9) + 7  # initialising mod value
    rslt = []
    # calculating pre sum
    for i in range(1, n + 1):
        sum = pre_sum[i - 1] + arr[i - 1]
        pre_sum[i] = sum
    for i in queries:
        l = i[0]
        r = i[1]
        l_sum = sum_range(l-1, n, pre_sum)
        r_sum = sum_range(r, n, pre_sum)
        final_sum = (r_sum - l_sum) % mod
        rslt.append(final_sum)
    return rslt
