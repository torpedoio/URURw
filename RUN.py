file = open("PATH", "r").read()

import os
os.system(f"cd {file} && bash startup")
