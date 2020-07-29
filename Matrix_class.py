def inputint(text):
    while True:
        number = str(input(text))
        if number.strip() == '' or number.isalpha():
            print('Invalid integer number, try again.')
        else:
            return int(number)
            break


class Matrix():
    def definer(self):
        """
        Defines a 3x3 matrix by nine inputs of integer numbers.
        :return: A callable list containing the 9 digits of the matrix
        """
        matrix = [[], [], []]
        for line in range(0, 3):
            for column in range(0, 3):
                element = int(inputint(f'Type the [ {line + 1}, {column + 1} ] element: '))
                matrix[line].append(element)
        return matrix

    def printmatrix(matrix):
        """
        Prints the matrix properly in a better looking view.
        """
        for line in range(0, 3):
            if line != 0:
                print()
            for column in range(0, 3):
                print(f'[ {matrix[line][column]} ]', end='')


matrix_a = Matrix().definer()
Matrix.printmatrix(matrix_a)









