import networkx as nx
import matplotlib.pyplot as mp
from union_find import UnionFind

"""
Kruskal's Algorithm for Minimum Spanning Tree
-----------------------------------------------------------

A minimum spanning tree (MST) can be derived 
from a connected undirected and weighted graph.
There can be multiple MST with the same total weight.
An MST includes all the vertices v  
and has v - 1 edges.

The Union Find (Disjoint Set) Data structure (UnionFind class) 
is used to implement the Kruskal algorithm.
The Union Find is a data structure that keeps
track of elements which are split into
one or more disjoint sets.
It has two primary operations: find and union.


The UnionFind class helps to avoid making cycles 
in the MST.

The main steps of the algorithm are:

    1.  Sort the edges of the graph by weight in ascending order.
    
    2.  Starting from the lowest weight, 
        edges are added to the MST while edges that create cycles are rejected. 
        
    3.  Stop when all the edges are processed or all vertices are connected.

"""

nodes = ['A','B','C','D','E','F','Z']
edges = [
            ('A','B',2),
            ('A','C',7),
            ('B','D',1),
            ('B','E',5),
            ('C','D',3),
            ('C','F',10),
            ('D','F',4),
            ('D','Z',6),
            ('E','Z',3),
            ('F','Z',3)
        ]


def draw_graph(G):
    """
    Draw the graph G elements (nodes, edges, labels)
    Uses a circular layout for the nodes.
    Returns the position object of the 
    elements of the graph 
    which is later used to draw the edges of the MST.
    """
    pos = nx.planar_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)
    nx.draw_networkx_edges(G,pos,edge_color='grey')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)},verticalalignment='baseline'
    )
    mp.title('Kruskal MST')
    mp.axis("off")
    return pos


def draw_mst_edge(T,pos):
    """
    Draw the network edges of the MST 
    and pause for 2 seconds.
    """
    nx.draw_networkx_edges(T, pos, edge_color="green", width=2)
    mp.waitforbuttonpress()
    
def kruskal_mst(G,pos):
    """
    Create the UF helper class.
    Sort the edges of the graph
    build the tree and add the nodes.
    Loop over the sorted edges and 
    if the  edges' nodes 
    are not unified, that is they do not 
    share the same root, add edge to MST and
    unify the nodes in the UnionFind class.

    """
    uf = UnionFind(nodes)
    sorted_edges=sorted(G.edges(data=True), key=lambda edge: edge[2].get('weight', 1))
    print('Sorted Edges')
    for e in sorted_edges:
        print(f'{e}')
    max_edges = len(nodes)-1
    T = nx.Graph()
    T.add_nodes_from(nodes)
    tree_edges = []
    i,e = 0,0
    total_weight = 0
    while i < len(sorted_edges) and len(tree_edges) < max_edges:
        u, v, w = sorted_edges[i]
        x = uf.find(u)
        y = uf.find(v)
        if x != y:
            # Unify edges 
            e = e + 1
            tree_edges.append([u, v, w])
            total_weight += w['weight']
            T.add_weighted_edges_from([(u,v,w)])
            uf.union(u, v)
            print(f'Edge added: {sorted_edges[i]}')
            draw_mst_edge(T,pos)
        else:
            print(f'Edge rejected: {sorted_edges[i]}')
        i += 1
    T.add_weighted_edges_from(tree_edges)
    mp.title('Kruskal MST - Total edge weight is ' + str(total_weight))
    print(f'Total edge weight is {total_weight}')
    return T

def main():
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    pos = draw_graph(G)
    mp.show(block=False)
    mp.waitforbuttonpress()
    T = kruskal_mst(G,pos)
    mp.show()

if __name__ == '__main__':
    main()
