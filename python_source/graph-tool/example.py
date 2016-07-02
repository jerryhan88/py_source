from graph_tool.all import *

# g = Graph()
# v1 = g.add_vertex()
# v2 = g.add_vertex()
# e = g.add_edge(v1, v2)
# 
# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")
# 
# from itertools import izip
# for v in g.vertices():
#    for e in v.out_edges():
#        print(e)
#    for w in v.out_neighbours():
#        print(w)
# 
#    # the edge and neighbours order always match
#    for e,w in izip(v.out_edges(), v.out_neighbours()):
#        assert(e.target() == w)

from itertools import izip
from numpy.random import randint as np_randint
from random import seed, randint

seed(2)

g = Graph()
num_vertex = 10
g.add_vertex(num_vertex)
g.edge_properties["weight"] = g.new_edge_property("int")
# insert some random links
# for s, t in izip(np_randint(0, num_vertex, num_vertex), np_randint(0, num_vertex, num_vertex)):
#     e = g.add_edge(g.vertex(s), g.vertex(t))
#     g.ep.weight[e] = randint(0, num_vertex)

# g.add_vertex(10)
# 
e = g.add_edge(g.vertex(1), g.vertex(2))
g.ep.weight[e] = 12
e = g.add_edge(g.vertex(0), g.vertex(2))
g.ep.weight[e] = 9
e = g.add_edge(g.vertex(2), g.vertex(3))
g.ep.weight[e] = 11
e = g.add_edge(g.vertex(2), g.vertex(6))
g.ep.weight[e] = 3
e = g.add_edge(g.vertex(5), g.vertex(6))
g.ep.weight[e] = 5

# for e in g.edges():
#     print e, g.ep.weight[e] 
g.vertex_properties["size"] = g.new_vertex_property("int")

for v in g.vertices():
    g.vp.size[v] = v.out_degree()
#     print g.vp.size[v]
# pos = sfdp_layout(g)
# pos = arf_layout(g, max_iter=0)
# pos = radial_tree_layout(g, g.vertex(0))
pos = fruchterman_reingold_layout(g, n_iter=1000)
graph_draw(g, pos=pos, vertex_text=g.vertex_index, vertex_pen_width = g.vertex_properties["size"], edge_text=g.ep.weight, vertex_font_size=18,
#            edge_pen_width=g.edge_properties["weight"], 
           output_size=(200, 200), output="temp1.pdf")
# graph_draw(g, efilt=lambda e: g.ep.weight[e] > 5, vertex_text=g.vertex_index, edge_text=g.ep.weight, vertex_font_size=18, output_size=(200, 200), output="temp2.pdf")
# for x in g.ep.weight.get_array():
#     print x

u = GraphView(g, efilt=lambda e: g.ep.weight[e] > 5)
graph_draw(u, vertex_text=g.vertex_index, edge_text=g.ep.weight, vertex_font_size=18, output_size=(200, 200), output="temp2.pdf")
