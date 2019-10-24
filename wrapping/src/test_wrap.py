import openmeeg as om
data_file = "/Users/jls/Development/athena/openmeeg/data/Head1/Head1.tri"
mesh = om.Mesh()
mesh.load(data_file)

V = mesh.vertices()
T = mesh

newmesh = om.Mesh()
#for i in range(len(V)):
#    print(newmesh.nb_vertices())
#    newmesh.add_vertex(V[i])
