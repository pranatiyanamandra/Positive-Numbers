
print("Input: list1 =",end="")
input_1=input()
#Converting sting input to list
new_1=input_1[input_1.index("[")+1:input_1.index("]")]
news=new_1.split(",")
list_1=[]
for element in news:
    list_1.append(int(element))
#Printing Output    
output_1=[num for num in list_1 if num > 0]
print("Output: {}".format(output_1),end="\n\n")

print("Input: list2 =",end="")
new_2=input()
#Converting sting input to list
new=new_2[new_2.index("[")+1:new_2.index("]")]
news=new.split(",")
list_2=[]
for element in news:
    list_2.append(int(element))
#Printing Output     
output_2=[num for num in list_2 if num > 0]
print("Output:",output_2)
