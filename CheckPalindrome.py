def checkPalindrome(string, start, end):
    if start < end:
        if string[start] != string[end]:
            return 0

        return checkPalindrome(string, start + 1, end - 1)
    else:
        return 1


if __name__ == "__main__":
    A = input()
    startIndex = 0
    endIndex = len(A) - 1

    print(checkPalindrome(A, startIndex, endIndex))
