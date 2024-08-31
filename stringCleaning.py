# 3. You are given a
# string.  If the string has some “  # ”, in
# it you have to move all the hashes to the front of the string and return the
# whole string back

# Input - Move  # From#Here#ToStart
# output  -  # MoveFromHereToStart

def move_hashes_to_front(s):
    hash_count = s.count('#')
    hashes = '#' * hash_count

    result = hashes + ''.join(c for c in s if c != '#')

    return result

input_str = "Move#From#Here#ToStart"
output_str = move_hashes_to_front(input_str)
print(output_str)  
