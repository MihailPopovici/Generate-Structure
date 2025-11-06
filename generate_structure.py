import os 
import sys
import json

def load_structure_from_json(json_file_path):
    """Load structure from JSON file"""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found!")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

def create_structure(root_path, structure_dict):
    """
    Creates dictionary and file structure from JSON.

    Args:
        root_path: Path to the root directory
        structure_dict: Dictionary containing the structure
    """

    if not os.path.exists(root_path):
        os.makedirs(root_path)
        print(f"Created directory {root_path}")

    def process_item(current_path, item_dict):
        """Recursively process each item in the dictionary"""
        for key, value in item_dict.items():
            item_path = os.path.join(current_path, key)

            if isinstance(value, dict):
                #It's a directory, create it and process its contents
                if not os.path.exists(item_path):
                    os.makedirs(item_path)
                    print(f"Created directory {item_path}")
                process_item(item_path, value)

            elif isinstance(value, str):
                #It's a file, create it with the specified content
                with open(item_path, 'w', encoding='utf-8') as f:
                    f.write(value)
                print(f"Created file {item_path}, content: {value}")

    #Start processing from the root path
    process_item(root_path, structure_dict)
    print(f"\nStructure created successfully in: {os.path.abspath(root_path)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_structure.py <root_folder_path> <structure_json_file_path>")
        print("\nExample:")
        print('  python create_structure.py root_folder structure.json')
        print('\nJSON file content should be:')
        print('  {"dir1": {"dir2": {"file1": "content1", "file2": "content2"}, "file3": "content3"}, "file4": "content4"}')
        sys.exit(1)
    
    root_folder_path = sys.argv[1]
    structure_json_file_path = sys.argv[2]

    structure = load_structure_from_json(structure_json_file_path)

    create_structure(root_folder_path, structure)
    