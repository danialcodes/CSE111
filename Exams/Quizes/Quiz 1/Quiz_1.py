#Quiz 1
#Md Danial Islam
#20101534
#Sec: 01

#3,1,5,4,6,7,8

user_input = input().split(",")
range_to_print = input().split(" ")
user_inputed_list = [ int(x) for x in user_input ]
list_dict = {}
for i in range(len(user_inputed_list)):
  temp = 1
  for j in range(i+1):
    temp*= user_inputed_list[j]
  list_dict[i] = temp
product = list_dict[int(range_to_print[1])] // list_dict[int(range_to_print[0])-1]

print(list_dict)
print(product)