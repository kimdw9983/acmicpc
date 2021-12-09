l =[1, "b", "c"]
print(''.join(map(str, l))) 
print(*l, sep="")
#붙여서 출력
print('\n'.join(map(str, l)))
print(*l, sep="\n")
#한줄씩 출력