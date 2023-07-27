import os
def reverse_string(string):
    """Reverse a string."""
    return string[::-1]

def count_vowels(string):
    """Count the number of vowels in a string."""
    return sum(string.count(vowel) for vowel in 'aeiou')

def count_consonants(string):
    """Count the number of consonants in a string."""
    return sum(string.count(consonant) for consonant in 'bcdfghjklmnpqrstvwxyz')

def count_characters(string):
    """Count the number of characters in a string."""
    return len(string)

def count_specific_characters(string, chars):
    """Count the number of specific characters in a string."""
    return sum(string.count(char) for char in chars)

def count_word_occurrences(string, word):
    """Count the number of occurrences of a word in a string."""
    return string.count(word)

def count_letters(string):
    """Count the number of letters in a string."""
    return sum(c.isalpha() for c in string)

def count_numbers(string):
    """Count the number of numbers in a string."""
    return sum(c.isdigit() for c in string)

def count_capital_letters(string):
    """Count the number of capital letters in a string."""
    return sum(c.isupper() for c in string)

def count_noncapital_letters(string):
    """Count the number of non-capital letters in a string."""
    return sum(c.islower() for c in string)

def look_for_string(file_name, search_string, case_sensitive=False, return_lines=False, return_count=True, ignore_chars=""):
    # Open the file
    with open(file_name, "r") as file:
        # Read the file contents
        file_contents = file.read()
        
        # Ignore specific characters
        for char in ignore_chars:
            file_contents = file_contents.replace(char, "")
        
        # Set the search string to lowercase if case_sensitive is False
        if not case_sensitive:
            search_string = search_string.lower()
            file_contents = file_contents.lower()
        
        # Find all occurrences of the search string
        search_count = file_contents.count(search_string)
        
        # Return the count or lines where the search string was found based on input flags
        if return_count:
            return search_count
        elif return_lines:
            return [line for line in file_contents.split("\n") if search_string in line]
        else:
            return search_string
        
def look_for_string_in_string(input_string, search_string, return_count=True):
    # Find all occurrences of the search string
    search_count = input_string.count(search_string)
    
    # Return the count or the search string based on input flags
    if return_count:
        return search_count
    else:
        return search_string

def delete_string(file_name, delete_string, case_sensitive=False, ignore_chars=""):
    # Open the file
    with open(file_name, "r") as file:
        # Read the file contents
        file_contents = file.read()
        
        # Ignore specific characters
        for char in ignore_chars:
            file_contents = file_contents.replace(char, "")
        
        # Set the delete string to lowercase if case_sensitive is False
        if not case_sensitive:
            delete_string = delete_string.lower()
            file_contents = file_contents.lower()
        
        # Delete all occurrences of the delete string
        file_contents = file_contents.replace(delete_string, "")
        
    # Write the updated contents back to the file
    with open(file_name, "w") as file:
        file.write(file_contents)

def get_specific_file_content(filename, start_text, end_text, include_start=True, include_end=True, stop_at_empty_row=False, stop_at_character=None, output_format="list1"):
    """
    Returns the content of a file between two texts as a list of lines or a single merged string.
    
    :param filename: Name of the file to read.
    :param start_text: Text to start reading from.
    :param end_text: Text to stop reading at.
    :param include_start: Include the line containing start_text in the output.
    :param include_end: Include the line containing end_text in the output.
    :param stop_at_empty_row: Stop reading when an empty row is encountered.
    :param stop_at_character: Stop reading when a specific character is encountered.
    :param output_format: Format of the output. Valid values: "list1" (default), "list2", "string".
    :return: A list of lines or a single merged string containing the content between start_text and end_text.
    """
    # Initialize variables
    found_start_text = False
    stop_reading = False
    content = []

    # Open the file and read its contents line by line
    with open(filename, "r") as f:
        for line in f:
            # Check if the line contains the start text
            if start_text in line:
                found_start_text = True
                if include_start:
                    content.append(line.strip())
                continue

            # Check if the line contains the end text
            if end_text in line:
                if include_end:
                    content.append(line.strip())
                stop_reading = True
                break

            # Check if the line is empty and stop reading if required
            if stop_at_empty_row and not line.strip():
                break

            # Check if the line contains a specific character and stop reading if required
            if stop_at_character and stop_at_character in line:
                break

            # Add the line to the content if it'string between start and end texts
            if found_start_text and not stop_reading:
                content.append(line.strip())

    # Return the content in the desired output format
    if output_format == "list1":
        return "\n".join(content)
    elif output_format == "list2":
        return ", \n".join(content)
    elif output_format == "list3":
        return ", ".join(content)
    elif output_format == "list4":
        return " ".join(content)
    elif output_format == "list5":
        return content
    else:
        raise ValueError("Invalid output format: {}".format(output_format))
    
def encrypt_filecontent(file_name, file_parent, method):
    file_path = os.path.join(file_parent, file_name)
    with open(file_path, "rb") as f:
        # read the file content
        file_content = f.read()
    with open(file_path, "ab") as f:
        # encode file name and content as bytes
        file_name_bytes = file_name.encode(method)
        file_content_bytes = file_content.encode(method)
        # write the length of file name and content as 4-byte integers
        f.write(len(file_name_bytes).to_bytes(4, byteorder="little"))
        f.write(len(file_content_bytes).to_bytes(4, byteorder="little"))
        # write the file name and content as bytes
        f.write(file_name_bytes)
        f.write(file_content_bytes)

def decrypt_filecontent(file_name, file_parent, method):
    file_path = os.path.join(file_parent, file_name)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            while True:
                # read the length of file name and content as 4-byte integers
                name_len_bytes = f.read(4)
                if not name_len_bytes:  # end of file
                    return "FILE_NOT_FOUND"
                content_len_bytes = f.read(4)
                # convert bytes to integers
                name_len = int.from_bytes(name_len_bytes, byteorder="little")
                content_len = int.from_bytes(content_len_bytes, byteorder="little")
                # read the file name and content as bytes
                name_bytes = f.read(name_len)
                content_bytes = f.read(content_len)
                # decode bytes as strings
                name = name_bytes.decode(method)
                content = content_bytes.decode(method)
                if name == file_name:
                    return content
                
def delete_encrypted_filecontent(file_name, file_parent, method):
    file_path = os.path.join(file_parent, file_name)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            lines = []
            while True:
                # read the length of file name and content as 4-byte integers
                name_len_bytes = f.read(4)
                if not name_len_bytes:  # end of file
                    break
                content_len_bytes = f.read(4)
                # convert bytes to integers
                name_len = int.from_bytes(name_len_bytes, byteorder="little")
                content_len = int.from_bytes(content_len_bytes, byteorder="little")
                # read the file name and content as bytes
                name_bytes = f.read(name_len)
                content_bytes = f.read(content_len)
                # decode bytes as strings
                name = name_bytes.decode(method)
                content = content_bytes.decode(method)
                if name != file_name:
                    lines.append((name_bytes, content_bytes))
        with open(file_path, "wb") as f:
            for name_bytes, content_bytes in lines:
                f.write(len(name_bytes).to_bytes(4, byteorder="big"))
                f.write(len(content_bytes).to_bytes(4, byteorder="big"))
                f.write(name_bytes)
                f.write(content_bytes)
                
def encrypt_string(string, method):
    encoded_string = string.encode(method)
    length_bytes = len(encoded_string).to_bytes(4, byteorder="little")
    return length_bytes + encoded_string

def decrypt_string(string, method):
    decoded_bytes = string.encode(method)
    decoded_string = decoded_bytes.decode(method)
    return decoded_string

def get_object_names(folder_path, object_type="both", exclude_subfolders=False, output_path=False, full_path=True, depth=0):
    if not os.path.isdir(folder_path):
        raise ValueError(f"{folder_path} is not a valid directory path.")
    folder_contents = []
    for object_name in os.listdir(folder_path):
        object_path = os.path.join(folder_path, object_name)
        
        if os.path.isdir(object_path):
            if object_type in ["folder", "both"]:
                folder_contents.append(object_path if output_path and full_path else object_name)
                
            if not exclude_subfolders:
                folder_contents.extend(get_object_names(object_path, object_type, exclude_subfolders, output_path, full_path, depth + 1))
        
        elif os.path.isfile(object_path) and (object_type in ["file", "both"]):
            folder_contents.append(object_path if output_path and full_path else object_name)
        
    if output_path and not full_path:
        folder_contents = [os.path.basename(path) for path in folder_contents]
    
    return folder_contents if depth > 0 else sorted(folder_contents)

__all__ = [
    'reverse_string',
    'count_vowels',
    'count_consonants',
    'count_characters',
    'count_specific_characters',
    'count_word_occurrences',
    'count_letters',
    'count_numbers',
    'count_capital_letters',
    'count_noncapital_letters',
    'look_for_string',
    'look_for_string_in_string',
    'delete_string',
    'get_specific_file_content',
    'get_object_names',
    'encrypt_string',
    'decrypt_string',
    'encrypt_filecontent',
    'decrypt_filecontent',
    'delete_encrypted_filecontent',
]