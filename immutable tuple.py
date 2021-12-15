'''code to verrify that tuple is immutable means we cannot change data 
change data object in particular with another data in that particular index postion'''

tuple=(0,1,3.5,True,False,50+54j,"aditya")
tuple[0]=4 # as tuple object does not suppport item assignment. this line will create error message.
print(tuple)

# unlike list tuple do not support remove(),pop(),append(,inseert(),reverse(),and sort() due to immutability nature.

