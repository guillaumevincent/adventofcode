def get_nb_connected_nodes(tree, key):
    nb_connected_nodes = 0
    itself = 1
    for node in tree.get(key, []):
        nb_connected_nodes += get_nb_connected_nodes(tree, node)
        nb_connected_nodes += itself
    return nb_connected_nodes


def get_direct_tree(inputs):
    tree = {}
    for input in inputs:
        center, orbit = input.split(")")
        if center not in tree:
            tree[center] = []
        tree[center].append(orbit)
    return tree


def indirect_and_direct_orbit(inputs):
    tree = get_direct_tree(inputs)
    count = 0
    for sub_tree in tree:
        count += get_nb_connected_nodes(tree, sub_tree)
    return count


assert (
    indirect_and_direct_orbit(
        ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L",]
    )
) == 42


data = [x.strip() for x in open("06.in").readlines()]

# print(indirect_and_direct_orbit(data))


def get_tree_in_both_directions(inputs):
    tree = get_direct_tree(inputs)
    for input in inputs:
        center, orbit = input.split(")")
        if orbit not in tree:
            tree[orbit] = []
        tree[orbit].append(center)
    return tree


def minimum_orbital_transfert(inputs):
    tree = get_tree_in_both_directions(inputs)
    distance_to_you = {}
    queue = [("YOU", 0)]
    while queue:
        node, d = queue.pop(0)
        if node in distance_to_you:
            continue
        distance_to_you[node] = d
        for n in tree[node]:
            queue.append((n, d + 1))
    return distance_to_you["SAN"] - 2


assert (
    minimum_orbital_transfert(
        [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN",
        ]
    )
) == 4

# print(minimum_orbital_transfert(data))

