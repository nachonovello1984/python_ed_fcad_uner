from data_structures import Vertex, Edge, Graph

# Creo el grafo.
graph = Graph(is_directed=False)

# Creo los vértices.
chajari = graph.insert_vertex('Chajarí')
concordia = graph.insert_vertex('Concordia')
federal = graph.insert_vertex('Federal')
san_salvador = graph.insert_vertex('San Salvador')
colon = graph.insert_vertex('Colón')

# Defino los arcos que conectan cada vértice.
graph.insert_edge(chajari, concordia, 81)
graph.insert_edge(chajari, federal, 94)
graph.insert_edge(federal, concordia, 108)
graph.insert_edge(concordia, san_salvador, 61)
graph.insert_edge(concordia, colon, 125)
graph.insert_edge(san_salvador, colon, 93)

# Imprimo el grafo.
print (f"{'':*^60}")
print (f"{'Grafo completo':*^60}")
print (f"{'':*^60}")
print(graph)

# Métodos de consulta.
print (f"{'':_^60}")
print("Cantidad de vértices del grafo: ", graph.vertex_count())
print("Cantidad de arcos del grafo: ", graph.edge_count())
print("Grado de Concordia: ", graph.degree(concordia))

print (f"{'':_^60}")

# Muestro los arcos que entran y/o salen de Concordia
print("Arcos que entra/salen a/desde Concordia")
for e in graph.incident_edges(concordia, outgoing= True):
    print(f"-> origen: {e._origin} - destino: {e._destination} - distancia: {e._element}")

# Algoritmo de búsqueda primero en profundidad.
print()
print (f"{'':*^60}")
print (f"{' Búsqueda primero en profundidad (DFS) para Concordia ':*^60}")
print (f"{'':*^60}")

# Indico que inicio desde el nodo u (Concordia).
dfs_resultado = graph.dfs(concordia)
print([str(key) for key in dfs_resultado.keys()])

# Algoritmo de reconstrucción del camino.
print()
print (f"{'':*^60}")
print (f"{' Búsqueda primero en profundidad (DFS) para Chajarí ':*^60}")
print (f"{'':*^60}")

# Indico que inicio desde el nodo u (Chajarí).
dfs_resultado = graph.dfs(chajari)
print("DFS:", [str(key) for key in dfs_resultado.keys()])
print("Camino Chajarí - San Salvador:", graph.construct_path(chajari, san_salvador, dfs_resultado)) # type: ignore

print (f"{' Búsqueda primero en profundidad completo (dfs_complete)':*^60}")

# Creamos dos vértices más y los insertamos en el grafo.
salto = graph.insert_vertex('Salto (R.O.U.')
paysandu = graph.insert_vertex('Paysandú (R.O.U.)')

# Los vértices están conectados entre sí pero no con con el resto de las ciudades de Entre Ríos.
graph.insert_edge(salto, paysandu, 120)

print('DFS desde concordia:', graph.dfs(concordia))
print()
print('DFS desde salto:', graph.dfs(salto))
print()
print("DFS complete:", graph.dfs_complete())