def isPalindrome(s):
    # Initialize two pointers
    L, R = 0, len(s) - 1

    while L < R:
        # Keep advancing L until it hits an alphanumeric character. Note that also while L is still on the left side of R
        while L < R and not s[L].isalnum():
            L += 1
        # Keep advancing R until it hits an alphanumeric character. Note that also while R is still on the right side of L
        while L < R and not s[R].isalnum():
            R -= 1

        # Compare the lowercase version. If they don't match, return False.
        if s[L].lower() != s[R].lower():
            return False

        # Otherwise advance both pointers
        L += 1
        R -= 1

    # At the end, return true
    return True

        