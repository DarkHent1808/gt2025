def build_adj_matrix(edge_list, num_nodes):
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for src, dest in edge_list:
        matrix[src - 1][dest - 1] = 1
    return matrix


def traverse_inorder(graph, current_node):
    if current_node not in graph:
        return []

    left_subtree = traverse_inorder(graph, graph[current_node][0]) if graph[current_node] else []
    right_subtree = traverse_inorder(graph, graph[current_node][1]) if len(graph[current_node]) > 1 else []

    return [*left_subtree, current_node, *right_subtree]


graph_edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
total_nodes = 8

adjacency = build_adj_matrix(graph_edges, total_nodes)
print("Ma trận kề:")
for line in adjacency:
    print(line)

tree_structure = {
    1: [2, 3],
    2: [5, 6],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

target_node = int(input("Nhập nhãn nút để duyệt cây con theo thứ tự giữa: "))

result = traverse_inorder(tree_structure, target_node)
print(f"Kết quả duyệt cây con từ nút {target_node} theo thứ tự giữa: {result}")