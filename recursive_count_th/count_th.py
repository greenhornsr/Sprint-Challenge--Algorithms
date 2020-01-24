'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    my_list = list(word)
    count = 0
    if not my_list:
        return 0
    if len(my_list)-1 == 0:
        return count
    elif my_list[0] == "t":
        if my_list[1] == "h":
            count += 1
    new_word = ''.join(my_list[1:])
    count += count_th(new_word)
    return count

print(count_th("THtHThth"))