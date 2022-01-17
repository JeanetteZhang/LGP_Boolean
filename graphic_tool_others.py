import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np
import pandas as pd

# ignore this part
'''
x1 = [1, 2, 3]
y1 = [5, 6, 7]

x2 = [1, 2, 3]
y2 = [7, 6, 5]

temperature = [12, 23, 31, 0, 5, 1, 22, 19, 15, 24, 20, 17, 18, -5, -2, 13, 28]
bins = [-5, 0, 5, 10, 15, 20, 25, 30, 35]

days = [1, 2, 3, 4, 5]
working = [7, 8, 10, 5, 6]
resting = [10, 8, 9, 7, 10]
sleeping = [7, 8, 5, 12, 8]

slices = [9, 20, 4, 19]
targets = ['games', 'books', 'transport', 'food']

# histogram
# plt.hist(temperature, bins, histtype='bar', rwidth=0.8)
# scatter
# plt.scatter(x1, y1, marker='o')
# stack plot (We cannot make labels, but we can make fake labels via using normal plot.)
# plt.stackplot(days, working, resting, sleeping)
# pie charts
# plt.pie(slices, labels=targets, startangle=90, shadow=True, explode=[0, 0.1, 0, 0], autopct='%1.1f%%')

# plt.bar(x1,y1,label='bar1')
# plt.bar(x2,y2,label='bar2')
# plt.plot(x1, y1, label='original connections')
# plt.plot(x2, y2, label='FB connections')
# plt.xlabel('original node')
# plt.ylabel('neighbors')
'''
'''
x = []
with open('pheno_edges_forwards.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\n')
    for row in plots:
        x.append(row[0])
sns.distplot(x, hist=False, rug=False)
'''
# y = np.loadtxt('neighbors.txt', delimiter='\n', unpack=True)

'''
a = []
b = []
with open('L4_func_4_genoRobEvolva_back.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\n')
    for row in plots:
        s = row[0].split('\t')
        a.append(int(s[0]))
        b.append(int(s[1]))
print(b)
bins1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
bins2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
plt.hist(a, bins1, histtype='bar', rwidth=0.8)
'''
'''
labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
forwards_redundancy = [7.780991839, 7.117738888, 6.595845281, 7.380873181, 6.595845281, 7.380873181, 4.3950117, 7.117738888, 7.117738888, 4.3950117, 7.380873181, 6.595845281, 7.380873181, 6.595845281, 7.117738888,7.639650932]
backwards_redundancy = [8.082021834, 7.418768884, 6.896875276, 7.681903177, 6.896875276, 7.681903177, 4.696041695, 7.418768884, 7.418768884, 4.696041695, 7.681903177, 6.896875276, 7.681903177, 6.896875276, 7.418768884, 7.940680928]
traversal_redundancy = [8.082021834, 7.418768884, 6.896875276, 7.681903177, 6.896875276, 7.681903177, 4.696041695, 7.418768884, 7.418768884, 4.696041695, 7.681903177, 6.896875276, 7.681903177, 6.896875276, 7.418768884, 7.940680928]

x = np.arange(len(labels))
width = 0.4
fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/4, forwards_redundancy, width/2, label='Conventional')
rects2 = ax.bar(x - width/4, backwards_redundancy, width/2, label='Reversible')
rects3 = ax.bar(x + width/4, traversal_redundancy, width/2, label='Traversal')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('count(log)')
ax.set_title('redundancies')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
'''
'''
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_original = [2415749120, 524564480, 157726720, 961464320, 157726720, 961464320, 993280, 524564480, 524564480, 993280,
              961464320, 157726720, 961464320, 157726720, 524564480, 1744660480]
y_back = [9662996480, 2098257920, 630906880, 3845857280, 630906880, 3845857280, 3973120, 2098257920, 2098257920,
          3973120, 3845857280, 630906880, 3845857280, 630906880, 2098257920, 6978641920]
y_multi = [9662996480, 2098257920, 630906880, 3845857280, 630906880, 3845857280, 3973120, 2098257920, 2098257920,
           3973120, 3845857280, 630906880, 3845857280, 630906880, 2098257920, 6978641920]

plt.scatter(x, y_multi, label='multi-output')
plt.scatter(x, y_back, label='reversal')
plt.scatter(x, y_original, label='original')
'''

'''
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_conventional = [0.775458379, 0.656075897, 0.487932546, 0.691573919, 0.487932546, 0.691573919, 0.194201031,
                  0.664392313, 0.66233883, 0.194201031, 0.689147554, 0.487932546, 0.689147554, 0.487932546, 0.654022415,
                  0.711394804]
y_reversible = [0.892393949, 0.865619865, 0.816478071, 0.86830844, 0.816478071, 0.86830844, 0.745352564, 0.867695348,
                0.864732037, 0.751682692, 0.867814772, 0.816543662, 0.867814772, 0.816543662, 0.860963845, 0.866535654]
y_multi = [0.892508977, 0.897699984, 0.750772266, 0.883362791, 0.750772266, 0.883362791, 0.648051948, 0.898595923,
           0.89568426, 0.648052455, 0.872693868, 0.752509863, 0.872693868, 0.752509863, 0.892803701, 0.826878625]
plt.scatter(x, y_multi, label='multi-output')
plt.scatter(x, y_reversible, label='reversal')
plt.scatter(x, y_conventional, label='conventional')
'''

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_conventional = [0.262918146, 0.431559529, 0.476061253, 0.315544107, 0.476061253, 0.315544107, 0.709246134,
                  0.432126876, 0.440739106, 0.709246134, 0.323182133, 0.480830895, 0.323182133, 0.480830895,
                  0.453543614, 0.303494007]
y_reversible = [0.323542754, 0.496652076, 0.576137394, 0.401974605, 0.576137394, 0.401974605, 0.722355769, 0.49615521,
                0.536663659, 0.705128205, 0.425935099, 0.578344757, 0.425935099, 0.578344757, 0.535669423, 0.397324947]
y_multi = [0.371841593, 0.50393862, 0.574299315, 0.410684962, 0.574299315, 0.410684962, 0.717248377, 0.508046481,
           0.525063172, 0.717533736, 0.425236748, 0.58179477, 0.425236748, 0.58179477, 0.532973655, 0.389002422]
plt.scatter(x, y_multi, label='multi-output')
plt.scatter(x, y_reversible, label='reversal')
plt.scatter(x, y_conventional, label='conventional')

# df = pd.read_excel(r'neighbors.xlsx')
# x3 = pd.DataFrame(df, columns=['node'])
# y3 = pd.DataFrame(df, columns=['neighbors'])
# res = pd.DataFrame(df, columns=['connections'])
# sns.jointplot(x=x3, y=y3, data=res)
# sns.jointplot(x=x3, y=y3, data=res, kind="kde")

# plt.grid(True)
plt.title('average genotypic evolvability')
plt.legend()
# plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.95, wspace=0.92, hspace=0)

plt.show()
