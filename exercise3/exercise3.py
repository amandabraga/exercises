def last_char_is_a_space(name, index):
    return (index - 1 >= 0) and (name[index-1] == " ")

def reverse_and_format(name):
    if not isinstance(name, str):
        raise TypeError("Name should be a string")

    name = name.strip()
    result = ""
    index = len(name) - 1

    while(index >= 0):
        if (index == 0) or last_char_is_a_space(name, index):
            result += name[index].upper()
        else:
            result += name[index].lower()
        
        index -= 1
    
    return result

if __name__ == "__main__":
    name = input("Please type your first and last name separated by a space: ")

    print(f"{name} -> {reverse_and_format(name)}")