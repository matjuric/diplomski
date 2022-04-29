from cProfile import label
import enum
import matplotlib
import matplotlib.pyplot as plt, numpy as np
from datetime import date

dates = [
    date(2022, 3, 15),
    date(2022, 4, 1),
    date(2022, 4, 10),
    date(2022, 4, 20),
    date(2022, 4, 29),
]

labels = [
    'Intruder alert',
    'Phishing mails',
    'Ransomware',
    'DDoS',
    'DoS',
]

labels = ['{0:%d %b %Y}\n{1}'.format(d, l) for l, d in zip (labels, dates)]

fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
_ = ax.set_ylim(-2, 1.75)
_ = ax.set_xlim(date(2022, 3, 10), date(2022, 5, 5))
_ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)
_ = ax.scatter(dates, np.zeros(len(dates)), s=120, c='palevioletred', zorder=2)
_ = ax.scatter(dates, np.zeros(len(dates)), s=30, c='darkmagenta', zorder=3)

label_offsets = np.zeros(len(dates))
label_offsets[::2] = 0.35
label_offsets[1::2] = -0.7
for i, (l, d) in enumerate(zip(labels, dates)):
    _ = ax.text(d, label_offsets[i], l, ha='center', fontfamily='serif', fontweight='bold', color='royalblue',fontsize=12)

stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3
markerline, stemline, baseline = ax.stem(dates, stems, use_line_collection=True)
_ = plt.setp(markerline, marker=',', color='darkmagenta')
_ = plt.setp(stemline, color='darkmagenta')


for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)
 
_ = ax.set_xticks([])
_ = ax.set_yticks([])
 
_ = ax.set_title('Test timeline', fontweight="bold", fontfamily='serif', fontsize=16, 
                 color='royalblue')


plt.show()