import sys
from generate_string import generate_string, read_archive, axiom
from recognize_string import recognize_string
from turtle_main import create_screen, create_turtle

if __name__ == "__main__":
   file = sys.argv[1]
   ruledict = read_archive(file)

   if len(sys.argv) == 5 and sys.argv[2] == "--verificar":
      string = sys.argv[3]
      depth = sys.argv[4]
      print(recognize_string(depth, axiom, ruledict["rules"], string))
   else:
      string = generate_string(ruledict["length"], ruledict["rules"])[0]
      screen = create_screen()
      bob = create_turtle(ruledict["lineWidth"], ruledict["angle"], string)
      screen.mainloop()
      print(string)
      