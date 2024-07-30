import pandas as pd
import matplotlib.pyplot as plt

x1 = ['CSK','DC','KKR','MI','RCB','SRH','RR','KXIP']
y1 = [76,111,98,88,106,66,86,109]

plt.bar(x1, y1)
  
plt.xlabel("Teams")
plt.ylabel("Lost")
plt.title('Matches Lost')
plt.show()