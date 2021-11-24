{x: x * x for x in (1, 2, 3, 4)}
#{1: 1, 2: 4, 3: 9, 4: 16}



dict((x, x * x) for x in (1, 2, 3, 4))
#{1: 1, 2: 4, 3: 9, 4: 16}



{name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name > 6)}
#{'exchange': 8, 'overflow': 8}




dict((name, len(name)) for name in ('stack', 'overflow', 'exchange') if len(name) > 6)
#{'exchange': 8, 'overflow': 8}



initial_dict = {'x': 1, 'y': 2}
{key: value for key, value in initial_dict.items() if key == 'x'}
#{'x': 1}



my_dict = {1: 'a', 2: 'b', 3: 'c'}
swapped = {v: k for k, v in my_dict.items()}
swapped = dict(v, k) for k, v in my_dict.items()
swapped = dict(zip(my_dict.values(), my_dict))
swapped = dict(zip(my_dict.values(), my_dict.keys()))
swapped = dict(map(reversed, my_dict.items()))

print(swapped)
#{a: 1, b: 2, c: 3}