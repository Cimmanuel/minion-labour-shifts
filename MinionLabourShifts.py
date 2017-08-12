"""Write a function called answer(data, n) that takes a list of less than 100
integers and a number n, and returns that same list but with all the numbers
that occur more than n times removed entirely. The returned list should return
the same ordering as the original list. For instance, if data was [5, 10, 15,
10, 7] and n was 1, answer(data, n) should return the list [5, 15, 7] because
10 occurs twice, and thus was removed from the list entirely."""
# Written by Immanuel Kolapo Friday, 17th Feb 2017

# The function
def answer(data, n):
    copied_data = data.copy()
    for each_id in data:
        if data.count(each_id) > n:
            for each_copied_id in copied_data:
                if each_copied_id == each_id:
                    copied_data.remove(each_copied_id)
                else:
                    pass
        else:
            pass
    return copied_data
# The list of IDs
id_list = [53, 85, 29, 23, 29, 26, 88, 78, 5, 75, 74, 44, 33, 62, 98, 50, 89, 93,
           24, 14, 74, 49, 83, 45, 41, 14, 68, 76, 68, 8, 77, 85, 17, 3, 9, 30, 71,
           48, 18, 25, 86, 55, 55, 20, 74, 76, 99, 87, 59, 87, 36, 29, 29, 8, 22,
           65, 1, 18, 23, 5, 13, 60, 7, 5, 98, 61, 78, 64, 36, 60, 49, 57, 31, 32,
           41, 86, 52, 90, 9, 55, 35, 35, 2, 44, 8, 19, 96, 81, 68, 7, 8, 51, 9, 76,
           12, 96, 61, 99, 74]
# Call to answer() function
print(answer(id_list, 1))


# The test before writing the answer() function
# id_list = [1, 2, 3]
# n = 0
# id_list_copied = id_list.copy()
# for each_id in id_list:
#     if id_list.count(each_id) > n:
#         for each_id_copied in id_list_copied:
#             if each_id_copied == each_id:
#                 id_list_copied.remove(each_id_copied)
# print(id_list_copied)
