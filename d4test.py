from vpython import *
#Web VPython 3.2

verts = [
    vector(1, 1, 1),
    vector(-1, -1, 1),
    vector(-1, 1, -1),
    vector(1, -1, -1)
]

faces_idx = [
    [0, 1, 2],
    [0, 3, 1],
    [0, 2, 3],
    [1, 3, 2]
]

tri_faces = []
for idxs in faces_idx:
    tri_faces.append(
        triangle(
            v0=vertex(pos=verts[idxs[0]], color=color.red),
            v1=vertex(pos=verts[idxs[1]], color=color.red),
            v2=vertex(pos=verts[idxs[2]], color=color.red)
        )
    )
    
tetra = compound(tri_faces)