import numpy

A = numpy.array([[1, 2, 3],
                 [4, 5, 6]])
print A.shape
print '---------------------------------'
#
B = A.reshape((3, 2))
print B
print '---------------------------------'
#
A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[5, 6], [7, 8]])

C_Y = numpy.concatenate((A, B), axis = 0)
print C_Y
print '---------------------------------'
C_X = numpy.concatenate((A, B), axis = 1)
print C_X
print '---------------------------------'
#
A = numpy.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13 ,14 ,15, 16]])
print A
print '---------------------------------'
slice_Y_equal_size = numpy.split(A, 4, axis = 0)
print slice_Y_equal_size[0]
print '---------------------------------'
print slice_Y_equal_size[1]
print '---------------------------------'
slice_X_different_sizes = numpy.split(A, [2, 3], axis = 1)
print(slice_X_different_sizes[0])
print '---------------------------------'
print(slice_X_different_sizes[1])
print '---------------------------------'
print(slice_X_different_sizes[2])
print '---------------------------------'
#
A = numpy.array([[1,4,5,8], 
                    [2,1,7,3], 
                    [5,4,5,9]])
B = A.reshape((6, 2))
print B
print '---------------------------------'
temp_array = numpy.array([[2,2],
                            [5,3]])
B = numpy.concatenate((B, temp_array), axis = 0)                        
print B
print '---------------------------------'
# 3
C, D = numpy.split(B, 2, axis = 0)
print C
print '---------------------------------'
print D
print '---------------------------------'
# 4
E = numpy.concatenate((C, D), axis = 1)
print E
