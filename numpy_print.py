import numpy

sampleArray = numpy.array([[11, 22, 33],[44, 55, 66],[77, 88, 99]])
print("Printing Input Array")
print(sampleArray)
print("\n printing array of items in the third column from all rows")
newArray = sampleArray[...,2]
print(newArray)
