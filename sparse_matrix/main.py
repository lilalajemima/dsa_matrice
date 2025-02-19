from collections import defaultdict

# this initialises the sparse matrix class, a dictionary stores the matrix values. 
class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        self.matrix = defaultdict(int)  
        self.num_rows = num_rows
        self.num_cols = num_cols
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # extracts number of rows and columns of the matrice that by taking the first two lines of the file
            #checks/reads the matrix values from the file
            self.num_rows = int(lines[0].split('=')[1].strip())
            self.num_cols = int(lines[1].split('=')[1].strip())

            for line in lines[2:]: 
                parts = line.strip("()\n").split(", ")
                if len(parts) == 3:
                    row, col, value = map(int, parts)
                    self.matrix[(row, col)] = value

    def save_to_file(self, file_path):
        """Save the matrix to a file in the same format."""
        with open(file_path, 'w') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (row, col), value in sorted(self.matrix.items()):
                file.write(f"({row}, {col}, {value})\n")

    def add(self, other):
        """Does addition"""
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for key, value in self.matrix.items():
            result.matrix[key] = value + other.matrix.get(key, 0)
        for key, value in other.matrix.items():
            if key not in self.matrix:
                result.matrix[key] = value
        return result

    def subtract(self, other):
        """Does subtracting of matrices"""
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for key, value in self.matrix.items():
            result.matrix[key] = value - other.matrix.get(key, 0)
        for key, value in other.matrix.items():
            if key not in self.matrix:
                result.matrix[key] = -value
        return result

    def multiply(self, other):
        """Does the multiplying of matrices"""
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not allow multiplication. Go to README for more info on why.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (row, col), value in self.matrix.items():
            for k in range(other.num_cols):
                if (col, k) in other.matrix:
                    result.matrix[(row, k)] += value * other.matrix[(col, k)]
        return result

# File paths of the matrices
file1 = r'C:\Users\lilal\Intranet\dsa_matrice\sparse_matrix\sample_files\matrixfile1.txt'
file2 = r'C:\Users\lilal\Intranet\dsa_matrice\sparse_matrix\sample_files\matrixfile3.txt'

# Load matrices
matrix1 = SparseMatrix(file1)
matrix2 = SparseMatrix(file2)

# Display Menu 
print("Pick an operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
choice = input("Enter your choice (1/2/3): ").strip()

if choice == '1':
    result = matrix1.add(matrix2)
    output_file = 'sum.txt'
elif choice == '2':
    result = matrix1.subtract(matrix2)
    output_file = 'difference.txt'
elif choice == '3':
    result = matrix1.multiply(matrix2)
    output_file = 'product.txt'
else:
    print("Invalid choice.now closing the application.")
    exit()

result.save_to_file(output_file)
print(f"Results are saved. Go check it out at {output_file}")
