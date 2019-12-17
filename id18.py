
f = open('./textFiles/id18.txt')

lines = f.readlines()

vertices = []

for line in lines:
    newVertices = line.split(' ')
    if len(vertices) == 0:
        for x in newVertices:
            vertices.append(int(x))
        continue
    
    for i in range(len(newVertices)):
        newVertices[i] = int(newVertices[i])
        if i == 0:
            newVertices[i] += vertices[i]
        elif i == len(vertices):
            newVertices[i] += vertices[i-1]
        else:
            if vertices[i] > vertices[i-1]:
                newVertices[i] += vertices[i]
            else:
                newVertices[i] += vertices[i-1]
    
    vertices = newVertices

max = 0
for vertex in vertices:
    if vertex > max:
        max = vertex

print(max)

    

