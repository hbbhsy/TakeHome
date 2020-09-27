# Agnes He
# agneshesf@gmail.com

# Using Python, construct a class without importing any modules (such as numpy) given the following guidelines:
# -Given 2 inputs, data and shape, construct a tensor using nested lists.
# -A tensor is a general term for n-dimension matrix. (order goes scalar, vector, matrix, tensor)
# -Data and shape inputs are given as lists of numbers. Data can be any number (float, int, etc.),
#  but shape needs to be a list of positive integers.
# -Data and shape inputs can be lists of any length.
# -The constructed tensor can be saved as an instance variable, printed in standard output, or both.
# -If too many data numbers, cut it off after the tensor fills up. If not enough, pad the tensor w/ zeroes.


class Tensor(object):
    """
    The Tensor class will construct a tensor using nested lists, given the data and shape of the tensor.
    """

    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = []
        self.transform()

    def transform(self):
        """

        :return: None
        """

        def product(shape):
            """
            Helper function to compute the product of the positive integers in a list
            :param shape: List of positive integers
            :return: Product of the list
            :rtype: Int
            """
            prod = 1
            for i in shape:
                prod *= i
            return prod

        temp_data = [d for d in self.data]  # Create a copy of the data, in case of losing the original data

        # Check the shape of the tensor and the data size
        # -If too many data numbers, cut it off after the tensor fills up. If not enough, pad the tensor w/ zeroes.
        if len(self.data) > product(self.shape):
            temp_data = self.data[0:product(self.shape) + 1]
        elif len(self.data) < product(self.shape):
            temp_data += [0] * (product(self.shape) - len(self.data))

        # Iterating backwards through the shape list
        for s in self.shape[::-1]:
            current = 0
            temp_l = []

            # reshape the list to the current shape
            while current < len(temp_data):
                temp = temp_data[current:current + s]
                temp_l.append(temp)
                current += s
            temp_data = temp_l
        self.tensor = temp_data[0]
        print(self.tensor)


if __name__ == "__main__":
    data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
    shape0 = [2, 3, 2]
    tensor0 = Tensor(data0, shape0)

    data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2]
    shape1 = [5, 2]
    tensor1 = Tensor(data1, shape1)






