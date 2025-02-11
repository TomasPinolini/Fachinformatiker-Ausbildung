# 1. Even or Odd Check
# Bitwise AND (&) with 1 checks if the last bit is 1 (odd) or 0 (even)
num = 6  # Try changing this number!
if num & 1:
    print(f"{num} is ODD!")
else:
    print(f"{num} is EVEN!")

# 2. Make a Number Always Odd
# Bitwise OR (|) with 1 ensures the last bit is always 1, making the number odd
num = 8  # Try changing this!
new_num = num | 1  
print(f"Original: {num}, Now always odd: {new_num}")

# 3. Double a Number with Bit Shift
# Left shift (<<) moves bits left, multiplying by 2
num = 4  # Try different numbers!
double = num << 1  
print(f"Original: {num}, Doubled: {double}")

# 4. Cut a Number in Half with Bit Shift
# Right shift (>>) moves bits right, dividing by 2
num = 10  # Try different numbers!
half = num >> 1  
print(f"Original: {num}, Halved: {half}")

# 5. Turn ON a Specific Bit
# Bitwise OR (|) with (1 << position) sets a specific bit to 1
num = 2  # Binary: 10
pos = 1  # 2nd bit (0-based)
new_num = num | (1 << pos)  
print(f"Before: {bin(num)}, After setting bit {pos}: {bin(new_num)}")

# 6. Turn OFF a Specific Bit
# Bitwise AND (&) with ~(1 << position) clears a specific bit to 0
num = 7  # Binary: 111
pos = 1  # Clearing 2nd bit
new_num = num & ~(1 << pos)  
print(f"Before: {bin(num)}, After clearing bit {pos}: {bin(new_num)}")

# 7. Flip All Bits (Make Negative)
# Bitwise NOT (~) inverts all bits, effectively making the number negative - (num + 1)
num = 5  # Try different numbers!
flipped = ~num  
print(f"Original: {num}, Flipped: {flipped}")
