import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (людей) до графа
people = ['Hanna', 'Serhii', 'Ivan', 'Dariya', 'Olena', 'Franko']
G.add_nodes_from(people)

# Додавання ваг до ребер у графі
edges_with_weights = [('Hanna', 'Serhii', 1), ('Serhii', 'Ivan', 3), ('Serhii', 'Olena', 2),
                      ('Olena', 'Ivan', 4), ('Ivan', 'Dariya', 5), ('Dariya', 'Olena', 2),
                      ('Olena', 'Franko', 3), ('Franko', 'Hanna', 4)]
G.add_weighted_edges_from(edges_with_weights)

# Функція для знаходження найкоротших шляхів за допомогою алгоритму Дейкстри
def dijkstra_shortest_paths(graph, start):
    # Ініціалізація списку для зберігання найкоротших відстаней
    shortest_paths = {node: float('inf') for node in graph.nodes}
    # Початкова вершина має відстань 0
    shortest_paths[start] = 0
    # Ініціалізація списку відвіданих вершин
    visited = set()
    # Цикл для обробки всіх вершин графа
    while len(visited) < len(graph.nodes):
        # Знаходження вершини з найменшою відстанню
        current_node = min((node for node in graph.nodes if node not in visited), key=lambda x: shortest_paths[x])
        # Додавання поточної вершини до списку відвіданих
        visited.add(current_node)
        # Отримання сусідів поточної вершини
        neighbors = graph[current_node]
        for neighbor, weight in neighbors.items():
            # Розрахунок нової відстані до сусіда
            new_distance = shortest_paths[current_node] + weight['weight']
            # Оновлення найкоротшого шляху, якщо знайдено коротший
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
    return shortest_paths


# Знаходження та виведення найкоротших шляхів
for node in people:
    shortest_paths = dijkstra_shortest_paths(G, node)
    print(f"Найкоротші шляхи від вершини {node}: {shortest_paths}")


# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Соціальна мережа друзів")
plt.show()