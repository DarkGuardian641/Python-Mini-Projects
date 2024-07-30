import pandas as pd
import matplotlib.pyplot as plt

x1 =['CSK','DC','KKR','MI','RCB','SRH','RR','KXIP']
y1 = [117,93,107,125,98,64,84,91]

plt.bar(x1, y1)
  
plt.xlabel("Teams")
plt.ylabel("Won")
plt.title('Matches Won')
plt.show()