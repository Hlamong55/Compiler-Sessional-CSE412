action = {
    (0, 'id'): ('s', 3),
    (1, '+'): ('s', 4),
    (1, '$'): ('acc',),
    (2, '+'): ('r', 2),
    (2, '$'): ('r', 2),
    (3, '+'): ('r', 3),
    (3, '$'): ('r', 3),
    (4, 'id'): ('s', 3),
    (5, '+'): ('r', 1),
    (5, '$'): ('r', 1),
}

goto = {
    (0, 'E'): 1,
    (0, 'T'): 2,
    (4, 'T'): 5,
}

productions = {
    1: ('E', ['E', '+', 'T']),
    2: ('E', ['T']),
    3: ('T', ['id'])
}


def format_stack(stack):
    return " ".join(map(str, stack))


def format_input(inp, i):
    return " ".join(inp[i:])


def slr_parser(input_string):
    stack = [0]
    input_string.append('$')
    i = 0

    print(f"{'STACK':<30}{'INPUT':<25}{'ACTION'}")
    print("-" * 70)

    while True:
        state = stack[-1]
        symbol = input_string[i]

        stack_str = format_stack(stack)
        input_str = format_input(input_string, i)

        if (state, symbol) not in action:
            print(f"{stack_str:<30}{input_str:<25}ERROR ❌")
            return

        act = action[(state, symbol)]

        if act[0] == 's':
            print(f"{stack_str:<30}{input_str:<25}Shift {symbol}")
            stack.append(symbol)
            stack.append(act[1])
            i += 1

        elif act[0] == 'r':
            prod_num = act[1]
            lhs, rhs = productions[prod_num]

            print(
                f"{stack_str:<30}{input_str:<25}Reduce {lhs} -> {' '.join(rhs)}"
            )

            for _ in range(len(rhs) * 2):
                stack.pop()

            state = stack[-1]

            if (state, lhs) not in goto:
                print("Goto Error ❌")
                return

            stack.append(lhs)
            stack.append(goto[(state, lhs)])

        elif act[0] == 'acc':
            print(f"{stack_str:<30}{input_str:<25}ACCEPTED ✅")
            return


# ===== Read Input File =====

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "input.txt")

try:
    with open(input_file, "r") as f:
        line = f.readline().strip()

    input_tokens = line.split()

    print("\nInput String:", line)
    print()

    slr_parser(input_tokens)

except FileNotFoundError:
    print("input.txt not found!")