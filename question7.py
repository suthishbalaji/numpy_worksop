# create a list as below

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 5, 3, 2, 3]
d = [2]
e = [3]
output = []
output.append(a) 
output.append(b)  
nested_list = c.copy()
deep_nested_list = d.copy() 
deep_nested_list.append(e)   
nested_list.append(deep_nested_list) 
output.append(nested_list)
print(output)
