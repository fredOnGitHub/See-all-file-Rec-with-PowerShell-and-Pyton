import os.path
import re
def go(src, regex):
    m=0
    o=0
    nf=0
    for root, dirs, files in os.walk(src):
        if len(files):
            for i in files:
                r = re.search(regex, i, re.IGNORECASE)#https://regex101.com/
                if r:
                    l=len(root)+len(i)
                    m=max(m, l)
                    nf+=1
                    print(nf, m , l, i)
                    # print(nf,m,l, root, i)

go("D:\SAUV_D_2\_OneDrive", ".*")# tout
# go("D:\SAUV_D_2\_OneDrive", "^\..*")# les .DS_Store par exemple
# ^ start
# \. le point
# .* n'importe quel caractère
