from operator import add, mul

operations = {1: add, 2: mul}

def int_code(sequence, input):
    resultat = None
    i = 0
    while True:
        opcode = sequence[i]
        if opcode == 99:
            break
        p1 = p2 = p3 = 0
        if opcode > 100:
            opcode, params = opcode % 100, opcode // 100
            p3 = params % 10
            params //= 10
            p2 = params % 10
            params //= 10
            p1 = params % 10
            params //= 10
        if opcode in operations:
            value1 = sequence[i + 1] if p3 else sequence[sequence[i + 1]]
            value2 = sequence[i + 2] if p2 else sequence[sequence[i + 2]]
            index = sequence[i + 3]
            sequence[index] = operations[opcode](value1, value2)
            i += 4
        else:
            index = i if p3 else sequence[i + 1]
            if opcode == 3:
                sequence[sequence[i + 1]] = input
            elif opcode == 4:
                resultat = sequence[index]
            i += 2
    return resultat

input = 1
data = [int(x) for x in open("05.in").read().split(',')]
print(int_code(data, input))