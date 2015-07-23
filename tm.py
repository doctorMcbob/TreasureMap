def run(code):
    lines = code.split("\n")
    for i, line in enumerate(lines):
        if "O" in line:
            x = line.index("O") + 1
            y = i

    i, s = 0, [0 for n in range(50)]
    val = 0
    direction = (0, 0)
    treasure = ""
    cmd = ""
    while cmd != "X":
        cmd = lines[y][x]
        if cmd == ">":
            direction = (1, 0)
        elif cmd == "<":
            direction = (-1, 0)
        elif cmd == "v":
            direction = (0, 1)
        elif cmd == "^":
            direction = (0, -1)

        elif cmd == "w":
            s[i] = val

        elif cmd == "g":
            val = s[i]

        elif cmd == "f":
            i += 1
        elif cmd == "b":
            i -= 1

        elif cmd == "?":
            if val == 0:
                x += direction[0]
                y += direction[1]

        elif cmd == "+":
            val = val + 1 if val < 255 else 0
        elif cmd == "-":
            val = val - 1 if val > 0 else 255
        elif cmd == ".":
            treasure += chr(val)
        elif cmd == ",":
            val = ord(raw_input()[0])

        x += direction[0]
        y += direction[1]
        # ----DEBUG----
        # print cmd, val, (x, y), i, s[0:10]
        # raw_input()
    return treasure


if __name__ == "__main__":
    import sys
    if sys.argv[-1] != "tm.py":
        with open(sys.argv[-1], "r") as code:
            print run(code.read())
    else:
        raise IOError("Expected system argument")
