
# b és 3 porque apunta a "a", y luego aunque cambie, sigue apuntando a "a"
a = 3
b = a
print("b es",b)

# b és 3 porque apunta a "a", y luego aunque cambie, sigue apuntando a "a", aunque A se modifique a posteriori
a = 3
b = a
a = "spam"
print("b es", b)

# b és 3 porque apunta a "a", y luego aunque cambie, sigue apuntando a "a", aunque A se modifique a posteriori
a = 3
b = a
a = a + 2
print("b es",b)

l = [2, 3, 4]
m = l 