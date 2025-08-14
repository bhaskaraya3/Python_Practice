def my_generator(n):
    for i in range(n):
        yield i
        

gen = my_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))

# for g in gen:
#     print(next(g))