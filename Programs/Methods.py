a
#{'dog': 'собака', 'cat': 'кошка', 'mouse': 'мышь',
#'bird': 'птица', 'elephant': 'слон'}
a.clear()
a
#{}



nums2 = nums.copy()
nums2[4] = 'four'
nums
#{1: 'one', 2: 'two', 3: 'three'}
nums2
#{1: 'one', 2: 'two', 3: 'three', 4: 'four'}



a = [1, 2, 3]
c = dict.fromkeys(a)
c
#{1: None, 2: None, 3: None}
d = dict.fromkeys(a, 10)
d
#{1: 10, 2: 10, 3: 10}
c
#{1: None, 2: None, 3: None}



nums.get(1)
#'one'



nums.pop(1)
#'one'
nums
#{2: 'two', 3: 'three'}
nums.popitem()
#(2, 'two')
nums
#{3: 'three'}



nums.setdefault(4, 'four')
#'four'
nums
#{3: 'three', 4: 'four'}



nums.update({6: 'six', 7: 'seven'})
#{3: 'three', 4: 'four', 6: 'six', 7: 'seven'}