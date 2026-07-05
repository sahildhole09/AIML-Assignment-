import sys

print("Enter the number: ")
Value = int(input())

print("Datatype is: ",type(Value))
print("Memory Address is: ",id(Value))
print("Size of Variable in bytes: ",sys.getsizeof(Value))