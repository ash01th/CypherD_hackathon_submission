import yaml

def update_state(key, new_value,filepath='state.yaml'):
    """
    Updates a value in a YAML file for a given key.

    Args:
        filepath (str): The path to the YAML file.
        key (str): The key of the value to update.
        new_value: The new value to set for the key.
    """
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        if key in data:
            print(f"Updating key '{key}' from '{data[key]}' to '{new_value}'...")
            data[key] = new_value
        else:
            print(f"Key '{key}' not found. Adding it to the file.")
            data[key] = new_value

        with open(filepath, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
        
        print("File updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def get_state(key, filepath='state.yaml'):
    """
    Retrieves a value from a YAML file for a given key.

    Args:
        filepath (str): The path to the YAML file.
        key (str): The key of the value to retrieve.

    Returns:
        The value associated with the key, or None if the key is not found.
    """
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            if key in data:
                return data[key]
            else:
                print(f"Error: Key '{key}' not found in '{filepath}'.")
                return None
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
if __name__ == "__main__":
    # yaml_file = 'state2.yaml'
    # print("--- Running Example 1: Update username ---")
    # update_state(yaml_file, 'username', 'user_9999')
    # print("\n")
    print(get_state('username'))

