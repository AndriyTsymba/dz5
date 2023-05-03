# dz
#1
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print("Сума елементів списку list1: ", sum_list(list1))
print("Сума елементів списку list2: ", sum_list(list2))
#2
a = ""
def palindroma():
    slovo = str(input("ведіть слово"))
    a = slovo[::-1]
    if slovo == a:
        print("True")
    else:
        print("false")
        return slovo
palindroma()
#3
dict_1 = ["aaa","a","aabb","ab","b"]
def lens(srt):
    return sorted(srt,key=len)
print(lens(dict_1))