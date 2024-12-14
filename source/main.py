import sys
from generate_string import generate_string, read_archive
from recognize_string import recognize_string
from turtle_main import create_screen, create_turtle

if __name__ == "__main__":
  file = sys.argv[1]
  ruledict = read_archive(file)
  
  if len(sys.argv) == 5 and sys.argv[2] == "--verificar":
    string = sys.argv[3]
    #Axiom = X always??
    depth = sys.argv[4]
    print(recognize_string(depth, ruledict["rules"]['X'], ruledict["rules"], string))
  else:
    screen = create_screen()
    bob = create_turtle()
    screen.mainloop()
    print(generate_string(ruledict["length"], ruledict["rules"]))
    