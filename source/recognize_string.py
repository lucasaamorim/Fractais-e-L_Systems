from generate_string import read_archive, generate_string, axiom

def recognize_string(length, axiom, rules, string):
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

if __name__ == "__main__":
    file = read_archive("rules.json")
    string = generate_string(file["length"], file["rules"])[0]
    string = string[:15] + 'X' + string[15:]
    print(recognize_string(file["length"], axiom, file["rules"], string))