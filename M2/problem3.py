a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    positive_arr = []
    for i in range(len(arr)):
        x = arr[i]

        # If the element is a string, convert it to a number first
        if isinstance(x, str):
            try:
                x = int(x)
            except ValueError:
                x = float(x)

        # Convert negative numbers to positive using the abs() function
        abs_x = abs(x)

        # If the original element was a string, cast the absolute value to a string
        if isinstance(x, str):
            abs_x = str(abs_x)

        # Add the absolute value to the output array
        positive_arr.append(abs_x)

    # Print the positive output and the original data type of each element
    for i in range(len(positive_arr)):
        print(f"{positive_arr[i]} ({type(arr[i])})")

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
# Hrithikka UCID:hg345 Date:09/25 Showing the output of positive AND the same datatype as the input value