def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    d = 0
    l = 0
    di = {}
    for i in txt:
        print(i)
        if i.isdigit():
            d+=1
        
        elif i!=' ' and not i.isdigit():
            l += 1
    di['LETTERS'] = l
    di['DIGITS'] = d
    return di
print(count_all("Hello World"))