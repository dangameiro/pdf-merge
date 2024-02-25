import pdf_merge
import sys
  
if (len(sys.argv) < 3):
    print("Usage: python pdf-merge.py front.pdf back.pdf [output.pdf]")
        
front = sys.argv[1]
back = sys.argv[2]

output='pdf_out.pdf'

if (len(sys.argv) == 4):
    output = sys.argv[3]

pdf_merge.pdf_merge(front, back, output)