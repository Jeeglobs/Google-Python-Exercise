words = ['apple', 'board', 'chess', 'dog', 'zipline']

# print(words[::0])
# --> ValueError: slice step cannot be zero

# ===============================

# print(words[::1])
# --> ['apple', 'board', 'chess', 'dog', 'zipline'] --- prints list "as-is"? --- Same as print(words)??

# print(words[::-1])
# --> ['zipline', 'dog', 'chess', 'board', 'apple'] --- prints list in reverse order

# ===============================

# print(words[::2])
# --> ['apple, 'chess', 'zipline'] --- removes every other string??? --- WTF

# print(words[::-2])
# --> ['zipline', 'chess', 'apple'] --- reverses it and removes every other string???

# ===============================

# print(words[::3])
# --> ['apple', 'dog'] --- prints index 0 and index 3??

# print(words[::-3])
# --> ['zipline', 'board'] --- reverses the order and then prints index 0 and index 3?

# print(words[::4])
# --> ['apple', 'zipline'] --- prints index 0 and index 4

# print(words[::-4])
# --> ['zipline', 'apple'] --- reverses the order and then prints index 0 and index 4

# ===============================

# print(words[::5])
# --> ['apple'] --- no index 5, so does it wrap around so 0 is 5???

# print(words[::-5])
# --> ['zipline'] --- reverse wrap???

# ===============================

# print(words[0::4])
# --> ['apple', 'zipline']

# print(words[2::4])
# --> ['chess'] --- WTF why does't it print ['chess', 'zipline']

# print(words[::5])
