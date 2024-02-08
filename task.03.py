import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (людей) до графа
people = ['Hanna', 'Serhii', 'Ivan', 'Dariya', 'Olena', 'Franko']
G.add_nodes_from(people)

# Додавання зв'язків (дружби) між деякими людьми
#friendships = [('Hanna', 'Serhii'), ('Serhii', 'Ivan'), ('Serhii', 'Olena'), ('Olena', 'Ivan'), ('Ivan', 'Dariya'), ('Dariya', 'Olena'), ('Olena', 'Franko'), ('Franko', 'Hanna')]
#G.add_edges_from(friendships)

# Додавання ваг до ребер у графі
edges_with_weights = [('Hanna', 'Serhii', 1), ('Serhii', 'Ivan', 3), ('Serhii', 'Olena', 2),
                      ('Olena', 'Ivan', 4), ('Ivan', 'Dariya', 5), ('Dariya', 'Olena', 2),
                      ('Olena', 'Franko', 3), ('Franko', 'Hanna', 4)]
G.add_weighted_edges_from(edges_with_weights)

# Функція для знаходження найкоротших шляхів за допомогою алгоритму Дейкстри
def dijkstra_shortest_paths(graph):
    shortest_paths = {}
    for node in graph.nodes:
        shortest_paths[node] = nx.single_source_dijkstra_path_length(graph, node)
    return shortest_paths

# Знаходження найкоротших шляхів
shortest_paths = dijkstra_shortest_paths(G)

# Виведення найкоротших шляхів
for node in shortest_paths:
    print(f"Найкоротші шляхи від вершини {node}: {shortest_paths[node]}")


# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Соціальна мережа друзів")
plt.show()