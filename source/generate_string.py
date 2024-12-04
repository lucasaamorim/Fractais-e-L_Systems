axiom = 'X'
alphabet = ['r', 'g', 'b', 'n', '1', '2', '+', '-', '/', '\\', 'F', 'X', '[', ']']

def read_archive(path) -> dict:
   with open(path, 'r') as file:
      return eval(file.read())
   
   return {}

def validate_rules(rules) -> bool:
   for key, value in rules.items():
      if key not in alphabet:
         return False
      else:
         for char in value:
            if char not in alphabet:
               return False
   return True

def generate_string(length, rules) -> str:
   if not validate_rules(rules):
      return None

   string = axiom

   for _ in range(length):
      newString = ""
      for char in string:
         if char in rules:
            newString += rules[char]
         else:
            newString += char
      string = newString

   return string

if (__name__ == "__main__"):
   rules = read_archive("rules.json")
   string = generate_string(2, rules)
   
   if (string == None):
      print("Invalid rules")
   else:
      print(string)
