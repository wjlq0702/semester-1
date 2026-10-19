
# set.intersection() method

Look up documentation on the 'intersection()' method
- how is the method described?  
The intersection method for sets in python returns new set containing elements of the set that are also in another set.
- what are the inputs?
The inputs would be what is in both sets for example "setA.intersection(setB)". Here we are checking what intersects with setB and setA.
- what is the output?
The output would be the elements that are in both setA and setB
- think about the description of the data and also the type
The data would always be defined using {}. A set is unorder collection of unique items

Write a small program to test the method
setA = {"apple", "orange", "banana"}
setB ={"orange", "banana"}
test = setA.intersection(setB)
print(test)
##This would return {"orange","banana"}, as these are the two elements contained in both. 
