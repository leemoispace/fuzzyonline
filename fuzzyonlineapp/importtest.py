from fuzzycompare import compare2list
from fuzzywuzzy import process, fuzz


tlist=[]
with open("test") as tt:
    tlist=tt.readlines()

leftl=[i.split("\t")[0] for i in tlist]
rightl=[i.split("\t")[1] for i in tlist]


print(compare2list(leftl, rightl))