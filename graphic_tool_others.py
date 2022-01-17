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

labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
forwards_redundancy = [7.780991839, 7.117738888, 6.595845281, 7.380873181, 6.595845281, 7.380873181, 4.3950117, 7.117738888, 7.117738888, 4.3950117, 7.380873181, 6.595845281, 7.380873181, 6.595845281, 7.117738888,7.639650932]
backwards_redundancy = [8.082021834, 7.418768884, 6.896875276, 7.681903177, 6.896875276, 7.681903177, 4.696041695, 7.418768884, 7.418768884, 4.696041695, 7.681903177, 6.896875276, 7.681903177, 6.896875276, 7.418768884, 7.940680928]
traversal_redundancy = [8.082021834, 7.418768884, 6.896875276, 7.681903177, 6.896875276, 7.681903177, 4.696041695, 7.418768884, 7.418768884, 4.696041695, 7.681903177, 6.896875276, 7.681903177, 6.896875276, 7.418768884, 7.940680928]

x = np.arange(len(labels))
width = 0.4
fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/4, forwards_redundancy, width/2, label='conventional', color='k')
rects2 = ax.bar(x - width/4, backwards_redundancy, width/2, label='reversible', color='b')

rects3 = ax.bar(x + width/4, traversal_redundancy, width/2, label='multi-output', color='y')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('count(log)')
#ax.set_title('redundancies')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(bottom=4)
ax.legend()
plt.xticks(fontsize=23)
plt.yticks(fontsize=24)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_original = [2415749120, 524564480, 157726720, 961464320, 157726720, 961464320, 993280, 524564480, 524564480, 993280,
              961464320, 157726720, 961464320, 157726720, 524564480, 1744660480]
y_back = [4952285696, 1075357184, 323339776, 1971001856, 323339776, 1971001856, 2036224, 1075357184, 1075357184,
          2036224, 1971001856, 323339776, 1971001856, 323339776, 1075357184, 3576553984]
y_multi = [4952285696, 1075357184, 323339776, 1971001856, 323339776, 1971001856, 2036224, 1075357184, 1075357184,
           2036224, 1971001856, 323339776, 1971001856, 323339776, 1075357184, 3576553984]

plt.scatter(x, y_multi, label='multi-output', marker=",", color="y", s=60)
plt.scatter(x, y_back, label='reversible', marker="x", color="b", s=60)
plt.scatter(x, y_original, label='conventional', color="k", s=60)
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_conventional = [0.775458379, 0.656075897, 0.487932546, 0.691573919, 0.487932546, 0.691573919, 0.194201031,
                  0.664392313, 0.66233883, 0.194201031, 0.689147554, 0.487932546, 0.689147554, 0.487932546, 0.654022415,
                  0.711394804]
y_reversible = [0.770221528, 0.646686234, 0.476810425, 0.682897573, 0.476810425, 0.682897573, 0.189590143, 0.655389724,
                0.651906721, 0.189590143, 0.679649487, 0.476766681, 0.679649487, 0.476766681, 0.643769697, 0.703173661]
y_multi = [0.763031545, 0.643550919, 0.477652437, 0.678991174, 0.477652437, 0.678991174, 0.189841589, 0.651664495,
           0.648270943, 0.189841589, 0.675098445, 0.477652437, 0.675098445, 0.477652437, 0.640157368, 0.699410146]
plt.scatter(x, y_multi, label='multi-output', marker=",", color='y', s=45)
plt.scatter(x, y_reversible, label='reversible', marker="x", color='b', s=45)
plt.scatter(x, y_conventional, label='conventional', color='k', s=45)
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y_conventional = [0.280446022, 0.460330164, 0.50779867, 0.336580381, 0.50779867, 0.336580381, 0.75652921, 0.460935334,
                  0.470121713, 0.75652921, 0.344727609, 0.512886288, 0.344727609, 0.512886288, 0.483779855, 0.323726941]
y_reversible = [0.28750612, 0.471599917, 0.520805336, 0.349883358, 0.520805336, 0.349883358, 0.761512027, 0.474341127,
                0.485008252, 0.759579038, 0.35824324, 0.531270829, 0.35824324, 0.531270829, 0.498668447, 0.335517662]
y_multi = [0.283044491, 0.469055503, 0.52022712, 0.343363023, 0.52022712, 0.343363023, 0.756529209, 0.472229326,
           0.483674055, 0.756529209, 0.353727448, 0.527310697, 0.353727448, 0.527310697, 0.498661595, 0.327697058]
plt.scatter(x, y_multi, label='multi-output', marker=",", color='y', s=45)
plt.scatter(x, y_reversible, label='reversible', marker="x", color='b', s=45)
plt.scatter(x, y_conventional, label='conventional', color='k', s=45)
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
'''
data = pd.read_excel(r'C:\Users\eclipse\Desktop\master\edges(graph).xlsx')
df = pd.DataFrame(data, columns=['conventional', 'reversible', 'multi-output'])
x = np.linspace(0, 135, num=136)
plt.plot(x, df['conventional'], label='conventional', marker='s', color='k', markersize=3)
plt.plot(x, df['reversible'], label='reversible', marker='x', color='b', markersize=3)
plt.plot(x, df['multi-output'], label='multi-output', marker='o', color='y', markersize=3)
plt.xticks(fontsize=23)
plt.yticks(fontsize=24)
# plt.grid(True)

# df = pd.read_excel(r'neighbors.xlsx')
# x3 = pd.DataFrame(df, columns=['node'])
# y3 = pd.DataFrame(df, columns=['neighbors'])
# res = pd.DataFrame(df, columns=['connections'])
# sns.jointplot(x=x3, y=y3, data=res)
# sns.jointplot(x=x3, y=y3, data=res, kind="kde")


plt.xlabel('edge', fontsize=20)
plt.ylabel('edge weight(log)', fontsize=20)
plt.legend(prop={"size": 20})
# plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.95, wspace=0.92, hspace=0)

plt.show()