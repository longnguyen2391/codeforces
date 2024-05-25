guest_name = input().strip().lower()
host_name = input().strip().lower()
mess = input().strip().lower()
 
merge = guest_name + host_name
merge = list(merge)
mess = list(mess)
 
merge.sort()
mess.sort()
 
if merge == mess:
    print('YES')
else: print('NO')
