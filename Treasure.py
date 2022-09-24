# I/we declare that this file represents our own work, and that we
# have not seen any work on this assignment done by others, and that
# we have not shown our work to any others.

# Student name(s): James McDermott
# Student ID(s): 00001234

# Do not change the formatting above. For multiple names/IDs, use
# commas to separate.


from collections import Counter

def dict_sort(d):
    result = {}
    for k in sorted(d.keys()):
        # in modern Python, dicts remember the order in which their keys
        # were added, and use that order when being printed
        result[k] = d[k]
    return result

def recursive_func(the_input, result):
    
    if isinstance(the_input,dict):       #checking if the given input is dict and iterate until the keys are int       
        for key, value in the_input.items():            
            if isinstance(value,int):
                if key not in result:
                    result[key] = value
                else:
                    result[key] += value
            
            else: #if the values are not int then find the total length of the iterable and add to the result dict
                if key not in result:
                    result[key] = len(value)
                else:
                    result[key] += len(value)
                recursive_func(value, result)
                
    elif isinstance(the_input,(list, tuple)): #if the input is not dict parse each item in the iterable and recursively call the function
        for item in the_input:
            if not isinstance(item, dict):
                raise TypeError("'int' object is not iterable")
            recursive_func(item, result)
    return

def count_treasure(box):
    '''
    While wandering in the fortress of the goblin king, we've discovered a
    box of treasure!

    Count all the treasure and other items in the box and return the
    result as a `dict`, with keys sorted alphabetically.
    
    `box` is a `dict` specifying the number of each item, eg:
    >>> count_treasure({'coins': 10, 'diamonds': 10})
    {'coins': 10, 'diamonds': 10}

    The above is a box containing 10 coins and 10 diamonds, so the output
    is as shown.

    A container (the box itself, or a bag, pouch, etc.) can contain other
    containers. Instead of a number, the containers are specified as a 
    list, tuple, or similar. We should include the containers in the count:
    >>> count_treasure({'coins': 10,  
    ...                 'bags': [{'coins': 2}, {'coins': 5}]})
    {'bags': 2, 'coins': 17}

    Notice the above is a multi-line doctest, using ...

    Containers can be recursive:
    >>> count_treasure({'bags': [{'bags': [{'coins': 10}]}]})
    {'bags': 2, 'coins': 10}

    Here is a bigger example:
    >>> count_treasure({
    ...   'coins': 10,
    ...   'rubies': 10,
    ...   'enchanted pouches': [{
    ...      'coins': 10,
    ...      'rubies': 10,
    ...      'treasure chests': (
    ...         {'coins': 1000},
    ...         {'coins': 1000},
    ...         {'coins': 1000}
    ...      ) # this was a tuple of 3 treasure chests
    ...    }] # this was a list of 1 enchanted pouches
    ... })
    {'coins': 3020, 'enchanted pouches': 1, 'rubies': 20, 'treasure chests': 3}

    If the input is mis-specified, we expect to see an error:
    >>> count_treasure({'bags': (10, 20, 30)})
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
    '''
    
    
    

    # HINT: use a `Counter` to store your results while working
    
    result = Counter()
    

    ## YOUR CODE HERE
    recursive_func(box,result)
    # HINT: use `dict_sort(result)` at the end to sort and
    # convert to an ordinary `dict`
    return dict_sort(result)
