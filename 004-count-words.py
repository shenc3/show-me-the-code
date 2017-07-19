# -*- coding: utf-8 -*-

import re
import os
import tkinter as tk
from tkinter import filedialog
from collections import Counter

root = tk.Tk()
root.withdraw()
file2count = filedialog.askopenfilename()

wc = Counter()
with open(file2count, 'r', encoding='gbk') as f:
    lines = f.readlines()
    for row in lines:
        words = re.split('\W+', row)
        for word in words:
            wc[word] += 1

output = os.path.join(os.path.dirname(file2count), 'output.txt')
with open(output, 'w', encoding='utf-8') as f:
    for k, v in wc.items():
        f.write("{}\t{}".format(k, v))
        f.write('\n')
