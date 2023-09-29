# Ex. 1

# price_list = [25, 19, 3, 22, 5, 3, 12, 7, 3, 2, 9, 5, 13, 1, 14]
# buying_price = min(price_list)
# b_index = price_list.index(buying_price)
# selling_price = max(price_list)
# s_index = price_list.index(selling_price)
# if b_index > s_index:
#     s_price1 = max(price_list[b_index:])
#     b_price1 = min(price_list[:s_index])
#     if s_price1 - buying_price > selling_price - b_price1:
#         print(f'Profit = {s_price1 - buying_price}, buying date = {b_index}, selling date = {(price_list[b_index:].index(s_price1) + len(price_list[:b_index]) + 1)}')
#     else: 
#         print(f'Profit = {selling_price - b_price1}, buying date = {price_list.index(b_price1)}, selling date = {s_index}')
# else:
#     print(f'Profit = {selling_price - buying_price}, buying date = {b_index}, selling date = {s_index}')


# Ex. 2

# def cache_decorator(function):
#     cache = {}
#     def inner(n):
#         if n not in cache:
#             cache[n] = function(n)
#         return cache[n]
#     return inner

# @cache_decorator
# def fib(n: int):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# def stairs(n: int):
#     return fib(n + 1)

# print(stairs(6))






