def list_to_text(lst):
    output = ''
    for i in range (0, len(lst)):
        if i < len(lst) - 2:
            output += (lst[i] + ' ')
        elif i == len(lst) -2 :
            output += (lst[i] + ', ')
        else:
            output += lst[i]
    return output


spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_text(spam))



