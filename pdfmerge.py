import PyPDF2
import pathlib
from os import remove as rm
from datetime import datetime
from tkinter import Tcl
merger = PyPDF2.PdfMerger()
output_file = "./output/"+str(datetime.now().timestamp())+".pdf"
files = [f for f in pathlib.Path('input').iterdir() if f.is_file()]
files = Tcl().call('lsort', '-dict', files)
for i in files:
    print(i)
    input_file = i
    merger.append(input_file)

merger.write(output_file)

for i in files:
    rm(i)
