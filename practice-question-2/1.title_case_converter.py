def title_case_converter(sentence):
    result = ""
    for i in range(len(sentence)):
        if i == 0 or sentence[i - 1] == " ":
            result += sentence[i].upper()
        else:
            result += sentence[i].lower()
    return result


print(title_case_converter("hello world from python"))
