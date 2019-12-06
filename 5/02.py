def get_opcode(code):
    digits = [int(x) for x in str(code)]
    return (0 if len(digits) == 1 else digits[-2]) * 10 + digits[-1]


def getNextSequence(sequence, index=0):
    command = get_opcode(sequence[index])
    if command == 99:
        return sequence
    first_position = sequence[index + 1]
    second_position = sequence[index + 2]
    next_position = sequence[index + 3]
    if command == 1:
        sequence[next_position] = sequence[first_position] + sequence[second_position]
    elif command == 2:
        sequence[next_position] = sequence[first_position] * sequence[second_position]
    index += 4
    return getNextSequence(sequence, index)


assert getNextSequence([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert getNextSequence([1002,4,3,4,33]) == 


assert get_opcode(1100) == 0
assert get_opcode(1002) == 2
assert get_opcode(1003) == 3
