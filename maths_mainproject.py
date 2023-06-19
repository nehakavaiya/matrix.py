from math import pow

# =========================Function=============================

def get_matrix_input(row,column):
    matrix = []
    for i in range(row):
        while True:
            row = input(f"Enter row {i+1} elements separated by \',\' ")
            row_elements = row.split(',')
            if len(row_elements) >= column:
                matrix.append([int(row_elements[i]) for i in range(column)])

                break 
            else :
                print('please enter all elements as per matrix order')

    return matrix

def adjointof2x2(matrix):
    adj_a = matrix[1][1]
    adj_a1 = -matrix[0][1]
    adj_b = -matrix[1][0]
    adj_b1 = matrix[0][0]
    adjointof2x2 = [[adj_a, adj_a1], [adj_b, adj_b1]]
    return adjointof2x2

def determinant2x2(matrix):
    return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])

def determinant_3x3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

def multiplication_matrix(matrix1,matrix2,matrix3):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                matrix3[i][j] += matrix1[i][k]*matrix2[k][j]
    return matrix3

def transpose(matrix):
    matrix_ = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        matrix_.append(row)
    return matrix_

def cofactor_3x3(matrix ,row ,column):
    matrix_row_remove = []
    final_matrix = []
    for i in range(len(matrix)):
        if i == row:
            pass
        else:
            matrix_row_remove.append(matrix[i])
    for i in range(len(matrix_row_remove)):
        row_ = []
        for j in range(len(matrix_row_remove[0])):
            if j == column:
                pass
            else:
                row_.append(matrix_row_remove[i][j])
        final_matrix.append(row_)
   

    cofactor = pow(-1,row+column)*determinant2x2(final_matrix)
    return cofactor

def cofactor_4x4(matrix,row ,column):
    matrix_row_remove = []
    final_matrix = []
    for i in range(len(matrix)):
        if i == row:
            pass
        else:
            matrix_row_remove.append(matrix[i])
    for i in range(len(matrix_row_remove)):
        row_ = []
        for j in range(len(matrix_row_remove[0])):
            if j == column:
                pass
            else:
                row_.append(matrix_row_remove[i][j])
        final_matrix.append(row_)
   

    cofactor = pow(-1,row+column)*determinant_3x3(final_matrix)
    cofactor2=int(cofactor)
    return cofactor2

# ================================Main code=========================================

print("\t\t\tMaths project")
ordermatrix=input("Enter order of matrix as NxN formate ex 3x3 = ").split('x')
if ordermatrix==["2","2"]:
    row1= int(ordermatrix[0])
    column1 = int(ordermatrix[1])
    matrix2x2=get_matrix_input(row1,column1)
    print(matrix2x2)
    print("Matrix is:")
    for i in matrix2x2:
        print(i)
    adjoint2x2=adjointof2x2(matrix2x2)
    print("Adjoint of matrix is:")
    for i in adjoint2x2:
        print(i)
    matrix3=[[0,0],[0,0]]
    multiplication2x2=multiplication_matrix(matrix2x2,adjoint2x2,matrix3)
    print("Matrix multiplied with Adjoint matrix:")
    for i in multiplication2x2:
        print(i)

elif ordermatrix==["3","3"]:
    row1= int(ordermatrix[0])
    column1 = int(ordermatrix[1])
    matrix3x3=get_matrix_input(row1,column1)

    print("Matrix is:")
    for i in matrix3x3:
        print(i)
    adjoint3x3=[]
    for row in range(len(matrix3x3)):
        row_=[]
        for column in range(len(matrix3x3[0])):
            row3=cofactor_3x3(matrix3x3,row,column)
            row_.append(row3)
        adjoint3x3.append(row_)
    print("Adjoint of matrix is:")
    trans3x3=transpose(adjoint3x3)
    for i in trans3x3:
        print(i)
        
    
    matrix3=[[0,0,0],[0,0,0],[0,0,0]]
    multiplication3x3=multiplication_matrix(matrix3x3,trans3x3,matrix3)
    print("Matrix multiplied with Adjoint matrix:")
    for i in multiplication3x3:
        print(i)

elif ordermatrix==["4","4"]:
    row1= int(ordermatrix[0])
    column1 = int(ordermatrix[1])
    matrix4x4=get_matrix_input(row1,column1)
    print("Matrix is:")
    for i in matrix4x4:
        print(i)
    adjoint4x4=[]
    for row in range(len(matrix4x4)):
        row_1=[]
        for column in range(len(matrix4x4[0])):
            row3=cofactor_4x4(matrix4x4,row,column)
            row_1.append(row3)
        adjoint4x4.append(row_1)
    print("Adjoint of matrix is:")
    trans4x4=transpose(adjoint4x4)
    for i in trans4x4:
        print(i)
    matrix3=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    multiplication4x4=multiplication_matrix(matrix4x4,trans4x4,matrix3)
    print("Matrix multiplied with Adjoint matrix:")
    for i in multiplication4x4:
        print(i)


else:
    print("Please Enter 2x2 matrix,3x3 matrix,4x4 matrix")


