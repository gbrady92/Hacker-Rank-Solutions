alpha_list = [

             ['a','b','c','d'],
             ['e','f','g','h'],
             ['i','j','k','l'],
             ['m','n','o','p']

             ]

def rotate(alpha_list):
    output_matrix = []
    num_of_rows = len(alpha_list) - 1
    num_of_columns = len(alpha_list[0])

    for x in range(num_of_columns):
        output_matrix.append([])
    for x in range(num_of_rows , -1, -1):
        for y in range(0,num_of_columns, 1):
            output_matrix[y].extend(alpha_list[x][y])
    print output_matrix

rotate(alpha_list)

    



