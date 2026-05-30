import re
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "input.txt")

with open(input_file, "r") as f:
    n = int(f.readline().strip())

    patterns = []
    for _ in range(n):
        patterns.append(f.readline().strip())

    m = int(f.readline().strip())

    inputs = []
    for _ in range(m):
        inputs.append(f.readline().strip())

for text in inputs:
    matched = False

    for index, pattern in enumerate(patterns):
        if re.fullmatch(pattern, text):
            print(f"YES, {index + 1}")
            matched = True
            break

    if not matched:
        print("NO, 0")