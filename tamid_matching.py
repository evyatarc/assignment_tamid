import sys
from munkres import Munkres, print_matrix, make_cost_matrix
import pandas as pd

df = pd.read_excel('small_excel_test.xls')
matrix = df.as_matrix().tolist()

cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxint - cost)
m = Munkres()
indexes = m.compute(cost_matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    column_name = df.columns[column]  #new addition Ev 4.30.16
    school_name = df.index[row]		#new addition Ev 4.30.16
    print "\n%s, %s" % (column_name, school_name)#new addition Ev 4.30.16
    print '(%d, %d) -> %d' % (row, column, value)
print 'total profit=%d' % total
