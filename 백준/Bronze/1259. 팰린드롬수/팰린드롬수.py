while True:
    Palindrome = list(map(int, input().strip()))
    if Palindrome[0] == 0 and len(Palindrome) == 1:
        break
    if Palindrome[0:len(Palindrome)] == Palindrome[::-1]:
        print('yes')
    else:
        print('no')