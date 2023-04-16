from PyPDF2 import PdfMerger
import os
from datetime import datetime

merge = PdfMerger()
dir = r"C:\Users\enoch\OneDrive - Nanyang Technological University\CS-NTU\EG0001\Presentation Slides"
pdf_files = os.listdir(dir) # insert dir here

for file in pdf_files:
    # append pdf file
    filepath = os.path.join(dir, file) 
    merge.append(filepath)
    # break

timenow = datetime.now().strftime("%d%m%Y_%H%M")

output_dir = "./merged_files"
merge.write(os.path.join(output_dir, f"Merged File_{timenow}.pdf"))
merge.close()