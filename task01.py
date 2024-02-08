import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (людей) до графа
people = ['Hanna', 'Serhii', 'Ivan', 'Dariya', 'Olena', 'Franko']
G.add_nodes_from(people)

# Додавання зв'язків (дружби) між деякими людьми
friendships = [('Hanna', 'Serhii'), ('Serhii', 'Ivan'), ('Serhii', 'Olena'), ('Olena', 'Ivan'), ('Ivan', 'Dariya'), ('Dariya', 'Olena'), ('Olena', 'Franko'), ('Franko', 'Hanna')]
G.add_edges_from(friendships)

# Аналіз основних характеристик графа
print("Кількість вершин у графі:", G.number_of_nodes())
print("Кількість ребер у графі:", G.number_of_edges())
print("Ступінь кожної вершини у графі:", dict(G.degree()))

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', pos=nx.spring_layout(G))
plt.title("Соціальна мережа друзів")
plt.show()