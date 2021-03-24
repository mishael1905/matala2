
def revword(word:str):
    newword=word.lower()
    fixword=(newword[::-1])
    return(fixword)

def countword():
    fname=input("Enter a file name:")
    handle=open(fname)
    counter=0
    for line in handle:
        if counter==0:
            word=line.lower()
            word=word.rstrip()
            counter=counter+1
        lineword=line.split()
        for sword in lineword:
            x=revword(sword)
            if x==word:
                counter=counter+1
    return counter+1
    

   


