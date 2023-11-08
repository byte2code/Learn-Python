# Create a sample input file with data
with open("input.txt", "w") as file:
    file.write("Hello, this is a sample input file.\n")
    file.write("Performing various operations on the data.\n")

# Read data from the input file
with open("input.txt", "r") as file:
    data = file.read()

print("Data read from input.txt:")
print(data)

# Append new data to the file
with open("input.txt", "a") as file:
    file.write("\nNew data appended to the file.")

# Read and display the updated data
with open("input.txt", "r") as file:
    updated_data = file.read()

print("\nUpdated data in input.txt:")
print(updated_data)

# List of lines by splitting the data
lines = updated_data.split("\n")

# Write the data to a new file
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

# Read and display the contents of file
with open("output.txt", "r") as file:
    output_data = file.read()

print("\nData in output.txt:")
print(output_data)
