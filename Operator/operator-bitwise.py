# 63  // bila menjadi biner adalah 0011 1100
# 13  // bila menjadi biner adalah 0000 1101
#
# # AND
# 0011 1100
# 0000 1101
# ---------
# 0000 1100
#
# #OR
# 0011 1100
# 0000 1101
# ---------
# 0011 1101
#
# #XOR
# 0011 1100
# 0000 1101
# ---------
# 0011 0001
#
# #Negasi
#
# 0011 1100
# ---------
# 1100 0011
#
# # >> 2
#
# 0011 1100
# ---------
# 0000 1111
#
# # 2 <<
#
# 0011 1100
# ---------
# 1111 0000

x = 63
y = 13

print ("x & y", x & y)
print ("x | y", x | y)
print ("x ^ y", x ^ y)
print ("~x ", x)
print ("~y ", y)
print ("x >> 2 ", x >> 2)
print ("x << 2 ", x << 2)

# Operator bitwise yang harus kamu ingat antara lain:
#
# &, melakukan operasi AND terhadap dua bilangan biner
# |, melakukan operasi OR terhadap dua bilangan biner
# ~, melakukan operasi negasi terhadap bilangan biner
# ^, melakukan operasi XOR terhadap dua bilangan biner
# >>, melakukan operasi penggeseran bit ke kanan terhadap bilangan biner
# <<, melakukan operasi penggeseran bit ke kiri terhadap bilangan biner
