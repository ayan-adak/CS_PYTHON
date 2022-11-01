import matplotlib.pyplot as plt
import numpy as np
 
fruits=['Apple','Banana','Kiwi','Orange']
pos = np.arange(len(fruits))
counts=[50,40,30,20]
c = ['red', 'yellow', 'green', 'orange']
plt.bar(pos,counts,color=c,edgecolor='black')
plt.xticks(pos, fruits)
plt.xlabel('FRUITS', fontsize=16, color='purple')
plt.ylabel('COUNTS', fontsize=16, color='blue')
plt.legend(fruits,loc=1)
plt.show()
