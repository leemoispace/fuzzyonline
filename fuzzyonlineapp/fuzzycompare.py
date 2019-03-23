from fuzzywuzzy import process,fuzz

def compare2list(leftl,rightl,resultdict):
    '''
    2 list, using right one to match left one 
    '''
    for item in leftl:
        resultdict[item]=process.extractOne(item, rightl,scorer=fuzz.token_sort_ratio)