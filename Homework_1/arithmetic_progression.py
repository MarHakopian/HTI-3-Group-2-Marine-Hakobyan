member1 = int(input('Enter the 1st member of progression: '))
member2 = int(input('Enter the 2nd member of progression: '))
N = int(input('Enter the N: '))

d = member2 - member1
progression: int = member1 + (N-1) * d

print(progression)
