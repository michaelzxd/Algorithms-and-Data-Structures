
def reverse(s):
    new_s = ''
    for i in range(len(s)):
        new_s = s[i] + new_s
    return new_s
print(reverse('good'))