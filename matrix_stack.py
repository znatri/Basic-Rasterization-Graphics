class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
        
    def pop(self, index=-1):
        if self.size() == 1:
            print("can't remove last matrix")
        else:
            self.data.pop(index)
    
    def clear(self):
        self.data = []        
        
    def peek(self):
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def updateCtm(self, item):
        self.data[-1] = item

stack = Stack()
dim = 4

def create(size):
    matrix = []
    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            matrix[i].append(0)
    return matrix

def gtInitialize():
    stack.clear()
    matrix = create(dim)
    matrix[0][0] = 1
    matrix[1][1] = 1
    matrix[2][2] = 1
    matrix[3][3] = 1
    stack.push(matrix)

def gtPopMatrix():
    stack.pop()

def gtPushMatrix():
    oldCtm = stack.peek()
    newCtm = duplMatrix(oldCtm)
    stack.push(newCtm)

def gtScale(x,y,z):
    scale_matrix = create(dim)
    scale_matrix[0][0] = x
    scale_matrix[1][1] = y
    scale_matrix[2][2] = z
    scale_matrix[3][3] = 1
    
    oldCtm = stack.peek()
    newCtm = multMatrix(oldCtm, scale_matrix)
    stack.updateCtm(newCtm)
    
def gtTranslate(x,y,z):
    translation_matrix = create(dim)
    translation_matrix[0][0] = 1
    translation_matrix[1][1] = 1
    translation_matrix[2][2] = 1
    translation_matrix[3][3] = 1
    translation_matrix[0][3] = x
    translation_matrix[1][3] = y
    translation_matrix[2][3] = z
    
    oldCtm = stack.peek()
    newCtm = multMatrix(oldCtm, translation_matrix)
    stack.updateCtm(newCtm)
    
def gtRotateX(theta):
    rotation_matrix = create(dim)
    theta = radians(theta)
    rotation_matrix[0][0] = 1
    rotation_matrix[1][1] = cos(theta)
    rotation_matrix[1][2] = -sin(theta)
    rotation_matrix[2][1] = sin(theta)
    rotation_matrix[2][2] = cos(theta)
    rotation_matrix[3][3] = 1
    
    oldCtm = stack.peek()
    newCtm = multMatrix(oldCtm, rotation_matrix)
    stack.updateCtm(newCtm)
    

def gtRotateY(theta):
    rotation_matrix = create(dim)
    theta = radians(theta)
    rotation_matrix[0][0] = cos(theta)
    rotation_matrix[0][2] = sin(theta)
    rotation_matrix[1][1] = 1
    rotation_matrix[2][0] = -sin(theta)
    rotation_matrix[2][2] = cos(theta)
    rotation_matrix[3][3] = 1
    
    oldCtm = stack.peek()
    newCtm = multMatrix(oldCtm, rotation_matrix)
    stack.updateCtm(newCtm)

def gtRotateZ(theta):
    rotation_matrix = create(dim)
    theta = radians(theta)
    rotation_matrix[0][0] = cos(theta)
    rotation_matrix[0][1] = -sin(theta)
    rotation_matrix[1][0] = sin(theta)
    rotation_matrix[1][1] = cos(theta)
    rotation_matrix[2][2] = 1
    rotation_matrix[3][3] = 1
    
    oldCtm = stack.peek()
    newCtm = multMatrix(oldCtm, rotation_matrix)
    stack.updateCtm(newCtm)

def print_ctm():
    ctm = stack.peek()
    for row in ctm:
        val = ' '.join(map(str, row))
        print(val)
    println("")
    
def multMatrix(matA, matB):
    result = create(len(matA))
    for i in range(0, len(matA)):
        for j in range(0, len(matA[i])):
            for k in range(0, len(matB)):
                result[i][j] += matA[i][k] * matB[k][j]
    return result

def duplMatrix(matA):
    matB = create(len(matA))
    for i in range(0, len(matA)):
        for j in range(0, len(matA[i])):
            matB[i][j] = matA[i][j]
    return matB
            
