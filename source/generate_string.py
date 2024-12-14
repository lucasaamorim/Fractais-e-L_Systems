axiom = 'X'
alphabet = ['r', 'g', 'b', 'n', '1', '2', '+', '-', '/', '\\', 'F', 'G', 'A', 'B', 'X', '[', ']']

def read_archive(path) -> dict:
   with open(path, 'r') as file:
      return eval(file.read())
   
   return {}

def validate_rules(rules) -> bool:
   for key, value in rules.items():
      if key not in alphabet:
         return False
      else:
         for rule in value:
            for char in rule:
               if char not in alphabet:
                  return False
   return True

def apply_rules(str, rules) -> list:   
   newStrings = []
   
   for rule in rules:
      newStrings.append(str + rule)
   
   return newStrings

def apply_rules_multi(strs, rules) -> list:
   newStrings = []
   
   for str in strs:
      newStrings.extend(apply_rules(str, rules))
   
   return newStrings

def generate_string(length, rules) -> list:
   if not validate_rules(rules):
      return None
   
   strings = [axiom]
   
   for _ in range(length):
      newStrings = []
      
      for string in strings:
         newForks = ['']
         
         for char in string:
            if char in rules:
               newForks = apply_rules_multi(newForks, rules[char])
            else:
               newForks = [fork + char for fork in newForks]
         newStrings.extend(newForks)
      strings = newStrings
   
   return strings

if (__name__ == "__main__"):
   file = read_archive("rules.json")
   string = generate_string(file["length"], file["rules"])
   
   if (string == None):
      print("Invalid rules")
   else:
      for (i, string) in enumerate(string):
         print(f"{i}: {string}")