#Adjacency List
graph = {
    1: [2],
    2: [1, 5],
    3: [6],
    4: [6, 7],
    5: [2],
    6: [3, 4, 7],
    7: [4, 6]
}

#DFS: Depth First Search
def is_path_exist(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    # Nếu đỉnh bắt đầu bằng đỉnh kết thúc
    if start == end:
        return True

    # Đánh dấu đỉnh hiện tại là đã thăm
    visited.add(start)

    # Duyệt qua các đỉnh kề
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if is_path_exist(graph, neighbor, end, visited):
                return True
    return False


# Chương trình chính
if __name__ == "__main__":
    start_node = int(input("Start node: "))
    end_node = int(input("End node: "))

    if start_node not in graph or end_node not in graph:
        print("Either start node or end node not exist")
    else:
        if is_path_exist(graph, start_node, end_node):
            print("True")
        else:
            print("False")
