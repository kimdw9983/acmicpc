l =[1, "b", "c"]
print(''.join(map(str, l))) 
print(*l, sep="")
#붙여서 출력
print('\n'.join(map(str, l)))
print(*l, sep="\n")
#한줄씩 출력

print = sys.stdout.write

#소수 셋째까지 반올림
round(3.14159265358, 3) #3.142

#소수 셋째까지 출력
format(1.23, ".3f") #1.230 