r_list = range(1,299)
print(len(r_list))
list = list(r_list)

q_list=[]
for i in list:
    i=i**2
    q_list.append(i)
print(q_list)

if 57 in q_list:
    print("57 is there")
else:
    print("57 is not included")