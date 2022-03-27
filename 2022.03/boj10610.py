N = input()
char_list = list(map(int,list(N)))

if not 0 in char_list or sum(char_list)%3 != 0:
    print("-1")
else:
    char_list= list(map(str,sorted(char_list,reverse=True)))
    print(''.join(char_list))
