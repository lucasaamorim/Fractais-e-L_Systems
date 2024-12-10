def recognize_string(length, rules, string) -> bool:
    stack = ['$']

    for char in string:
        topChar = stack[-1]
        if topChar not in terminals:

        elif topChar == char:
            stack.pop()
        else:
            return False

    return True

def recursive_call(rules,string):
    


def recognize_string_2(length, rules, string) -> bool:
    stacks = []
    for i in length(rules):
        stacks.append([rules[]])

    for char in string:
        topchar = stack[-1]
        if topchar not in terminals:

        elif topchar == char:
            stack.pop()
        else:
            return False

    return True