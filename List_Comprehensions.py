if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    result=[];
    abc=[];
    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                if x+y+z!=n:
                    abc=[x,y,z];
                    result.append(abc);
                
    print(result)
                
                
