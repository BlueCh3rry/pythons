"""

"
Allowed functions: None. Use only permitted built-in functions
to avoid getting 0 on exam day.
"

Given a string `s`, find the minimum number of cuts needed to partition it
such that every resulting substring is a palindrome.

A cut divides the string between two characters. With `c` cuts, the string
is split into `c + 1` substrings. We want the minimum number of cuts `c`
such that all parts are palindromes.

Return this minimum number of cuts (an integer).

Constraints:
- An empty string or a string of length 1 is already a palindrome -> 0 cuts.
- If the entire string is already a palindrome -> 0 cuts.
- In the worst case (all characters are distinct),
the result is len(s) - 1 cuts.


palindrome_partitioner("aab")
-> 1

palindrome_partitioner("aba")
-> 0

palindrome_partitioner("abc")
-> 2

"""


def palindrome_partitioner(s: str) -> int:
    cuts = 0
    i = len(s)/2
    while i != 0:
        
        return len(s)-1

    return cuts


def main():
    print("1", palindrome_partitioner("aab"))
    print("2", palindrome_partitioner("aba"))
    print("3", palindrome_partitioner("abc"))

kayak
boppob

if __name__ == "__main__":
    main()
