from scipy.io import arff
import pandas as pd
import os

def load_arff_file(file_name = None):
    """
    Load an .arff file from the './data' directory and return the data as a NumPy array.
    """

    # Check if the './data' directory exists
    if not os.path.exists('./data'):
        raise FileNotFoundError("The './data' directory does not exist")

    # Find all files in the './data' directory that end with .arff
    files = [f for f in os.listdir('./data') if f.endswith('.arff')]


    # If there are no .arff files in the directory, throw an error
    if not files:
        raise FileNotFoundError("No .arff files found in the './data' directory")
    
    # If the file name is not provided, ask the user to choose a file
    if not file_name:
        # Print the list of files in the directory
        file_names_with_index = {i: f for i, f in enumerate(files)}
        print("Choose a file to load:")
        for i, f in file_names_with_index.items():
            print(f"{i}: {f}")

        # Ask the user to choose a file to load
        while True:
            try:
                file_index = int(input("Enter the index of the file to load: "))
                if file_index in file_names_with_index:
                    break
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get the file name from the index
        file_name = file_names_with_index[file_index]
    else:
        # Check if the file exists in the directory
        if file_name not in files:
            raise FileNotFoundError(f"The file '{file_name}' does not exist in the './data' directory")
        

    # Get the full path of the file
    file_path = os.path.join('./data', file_name)

    return load_arff_file_from_file_path(file_path)

# Create a utility function to take the full path of the file and 
def load_arff_file_from_file_path(file_path):
    """
    Load an .arff file from the specified file path and return the data as a NumPy array.
    """

    # Open the .arff file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as f:
        data, meta = arff.loadarff(f)
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Drop the last column if it is not required
    df = df.iloc[:, :-1]

    # Convert it to a NumPy array
    data = df.to_numpy()

    return data

if __name__ == '__main__':
    df = load_arff_file()
    print(df)  # Print the first few rows of the DataFrame