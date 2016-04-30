
"""
Download Munkres from http://software.clapper.org/munkres/#installing_via_easyinstall
Download Anaconda PYTHON version 2.7 from https://www.continuum.io/downloads
	- large package with all awesome stuff
"""
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
    print column_name	#new addition Ev 4.30.16
    print school_name	#new addition Ev 4.30.16
    print '(%d, %d) -> %d' % (row, column, value)
print 'total profit=%d' % total

"""
Sources
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/linear_assignment_.py
https://github.com/scipy/scipy/blob/v0.17.0/scipy/optimize/_hungarian.py#L13-L107
http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.optimize.linear_sum_assignment.html
"""