if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    

arr=set(list(arr))
arr=sorted(arr)
print(arr[-2])
