import networkx as nx
import matplotlib.pyplot as plt

from paths import dfs_paths, bfs_paths

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (людей) до графа
people = ['Hanna', 'Serhii', 'Ivan', 'Dariya', 'Olena', 'Franko']
G.add_nodes_from(people)

# Додавання зв'язків (дружби) між деякими людьми
friendships = [('Hanna', 'Serhii'), ('Serhii', 'Ivan'), ('Serhii', 'Olena'), ('Olena', 'Ivan'), ('Ivan', 'Dariya'), ('Dariya', 'Olena'), ('Olena', 'Franko'), ('Franko', 'Hanna')]
G.add_edges_from(friendships)

# Знаходження шляхів за допомогою DFS і BFS
start_node = 'Serhii'
end_node = 'Franko'
dfs_result = list(dfs_paths(G, start_node, end_node))
bfs_result = list(bfs_paths(G, start_node, end_node))

# Виведення результатів
print("Шляхи за допомогою DFS:", dfs_result)
print("Шляхи за допомогою BFS:", bfs_result)