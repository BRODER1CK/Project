def is_palindrome(string):
    chars = str()
    if str(string).isdigit():
        if str(string)[:] == str(string)[::-1]:
            return True
        else:
            return False
    else:
        for i in str(string).casefold():
            if i.isalpha():
                chars += i
        if chars[:] == chars[::-1]:
            return True
        else:
            return False