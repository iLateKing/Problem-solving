def remove_char(text):
    #your code here
    length_of_text = len(text)
    result = ""
    
    for i in range(1, length_of_text - 1):
        result += text[i]

    return result