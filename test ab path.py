import os
from pathlib import Path
print(Path("post_pc_green_1.png").parent)
print("output: "+os.path.realpath("post_pc_green_1.png"))
out =os.path.dirname("post_pc_green_1.png")


for root, directories, filenames in os.walk(out):
    for name in filenames:
        print(root,directories,name)
