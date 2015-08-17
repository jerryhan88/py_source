import numpy

A = numpy.array([1, 2, 3, 4])
print numpy.sum(A)
print '---------------------------------'
#
A = numpy.array([[1, 2], [3, 4]])
print(A + 2)
print(A - 3)
print(A * 2)
print(A / 5)
print '---------------------------------'
#
A = numpy.array([1, 2, 4, 5, 5, 7, 10, 13, 18, 21])
print(numpy.mean(A))
print(numpy.median(A))
print(numpy.std(A))
print(numpy.var(A))
print '---------------------------------'
#
A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])
B = A.reshape((6, 2))
B = numpy.concatenate((B, numpy.array([[2, 2], [5, 3]])), axis = 0)
(C, D) = numpy.split(B, 2, axis = 0)
E = numpy.concatenate((C, D), axis = 1)
total = numpy.sum(E)
E = E / float(total)
print E
print '---------------------------------'
#
