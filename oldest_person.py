def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    m = 0
    n = ''
    t = ()
    while people:
        t = people.popitem()
        if t[-1]>m:
            m = t[-1]
            n = t[0]
        # print(people.popitem())
        
    return n
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))