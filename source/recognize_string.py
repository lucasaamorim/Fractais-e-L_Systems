from generate_string_multi import read_archive, generate_string, axiom

def recognize_string_2(length, axiom, rules, string):
    stack = [('$',0),(axiom, 0)]
    charPosition = 0
    
    while charPosition < len(string):
        char = string[charPosition]
        topChar, gen = stack.pop()
        
        if topChar == '$': 
            return False
        if topChar in rules and gen != length:
            stack.extend((newChar,gen+1) for newChar in rules[topChar][0][::-1])
        elif topChar == char:
            charPosition += 1
        else:
            return False
        
    return stack.pop() == ('$', 0)        

def recognize_string(length, axiom, rules, string) -> bool:
    stack = [('$',0),(axiom, 0)]
    charPosition = 0
    tmpString = ''
    #TODO: Remover isso, so p debug
    returnValue = True
    
    while charPosition < len(string):
        char = string[charPosition]
        topChar, gen = stack.pop()
        
        tmpString += topChar if length == gen else ''
           
        if topChar == '$': 
            returnValue = False
            break
        elif topChar == char and length == gen:
            charPosition += 1
        elif topChar in rules and gen != length:
            stack.extend((newchar,gen+1) for newchar in rules[topChar][0][::-1])
        elif gen == length:
            returnValue = False
    
    print(tmpString)
    return stack.pop() == ('$', 0) and returnValue


#def recursive_call(rules,string):
    
if __name__ == "__main__":
    file = read_archive("rules.json")
    string = generate_string(file["length"], file["rules"])[0]
    string = string[:15] + 'X' + string[15:]
    print(recognize_string_2(file["length"], axiom, file["rules"], string))