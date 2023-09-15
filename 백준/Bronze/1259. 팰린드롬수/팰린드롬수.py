def is_palindrome(num_str):
    reversed_str = num_str[::-1]  # 문자열을 뒤집음
    return num_str == reversed_str

while True:
    num_str = input()
    if num_str == '0':
        break
    if is_palindrome(num_str):
        print('yes')
    else:
        print('no')