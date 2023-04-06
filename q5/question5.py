def reverse_words(s):
    wds = []
    wds = s.split()
    wds.reverse()
    str = ""
    for i in wds:
        str += i + " "
    return str

def main():   
    a = "Two roads diverged in a yellow wood, And sorry I could not travel both "
    a += "And be one traveler, long I stood And looked down one as far as "
    a += "I could To where it bent in the undergrowth;"
    b = "Then took the other, as just as fair, And having perhaps the better claim, "
    b += "Because it was grassy and wanted wear; Though as for that the passing there "
    b += "Had worn them really about the same,"
    
    print("str1 :\n",a,"\n\nreverse :\n", reverse_words(a))
    print("\n")
    print("str2 :\n",b,"\n\nreverse :\n", reverse_words(b))
    
    
if __name__ == '__main__':
    main()
