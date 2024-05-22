n = int(input())

while(n > 0): 
    n -= 1
    string = input() 
    if len(string) <= 10:
        print(string)
        continue
    print(string[0]+str(len(string)-2)+string[-1])
