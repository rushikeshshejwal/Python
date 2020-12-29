
n = int(raw_input())
marks = [[raw_input(), float(raw_input())] for i in  xrange(n)]           
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print '\n'.join(result)
   

# second code
N = int(input())
mini = 101
mini2 = 102
a = []
for i in range(N):
    name = raw_input()
    mark = float(input())
    if mark<mini:
        mini2 = mini
        mini = mark
    elif mark<>mini and mark<mini2:
        mini2 = mark
    a.append([name, mark])
b = [x[0] for x in a if x[1]==mini2]
b.sort()
for y in b:
    print y
