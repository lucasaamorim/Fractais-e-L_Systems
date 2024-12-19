import sys
from generate_string import generate_string, read_archive, axiom
from recognize_string import recognize_string
from turtle_main import draw_l_system

if __name__ == "__main__":
    file = sys.argv[1]
    ruledict = read_archive(file)

    if len(sys.argv) >= 3 and sys.argv[2] == "--verificar":
        if (len(sys.argv) < 5):
          print("Too Few Arguments for --verificar")
          exit(1)
        else:
            string = sys.argv[3]
            depth = int(sys.argv[4])
            if recognize_string(depth, axiom, ruledict["rules"], string):
                print("String pertence ao L-System")
                #Talvez seja interessante visualizar o L-System aqui
            else:
                print("String nao pertence ao L-System")
    else:
        string = generate_string(ruledict["length"], ruledict["rules"])[0]
        #print(string)
        if string == None:
            print("Invalid rules")
            exit(1)
        brad, screen = draw_l_system(ruledict["lineWidth"], ruledict["angle"], string)
        screen.mainloop()
        