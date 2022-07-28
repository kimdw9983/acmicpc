i = 97
c = 'a'

#int -> char (97 -> a)
chr(i)
#char -> int (z -> 97)
ord(c)


#0 = 48, 9 = 57	(48+9)
ord(c) - 48
#a = 97, z = 122 (97+25)
ord(c) - 97
#A = 65, Z = 90
ord(c) - 65

#A -> a(대문자-> 소문자)
chr(ord(c) + 32)

#a -> A(소문자 -> 대문자)
chr(ord(c) - 32)