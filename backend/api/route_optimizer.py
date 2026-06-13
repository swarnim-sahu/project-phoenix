import networkx as nx

def find_best_route():

    G = nx.Graph()

    G.add_edge("Base", "Checkpoint-A", weight=2)
    G.add_edge("Checkpoint-A", "Checkpoint-B", weight=1)
    G.add_edge("Checkpoint-B", "Victim-Zone", weight=2)
    G.add_edge("Base", "Victim-Zone", weight=8)

    route = nx.shortest_path(
        G,
        source="Base",
        target="Victim-Zone",
        weight="weight"
    )

    distance = nx.shortest_path_length(
        G,
        source="Base",
        target="Victim-Zone",
        weight="weight"
    )

    return {
        "best_route": route,
        "distance_km": distance
    }
