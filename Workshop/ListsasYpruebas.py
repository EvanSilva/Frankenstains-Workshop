stooges = ["Moe","Larry","Curly"]

print(stooges)

def how_many_days(num):

    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[num -1]


print(how_many_days(9))

countries =  [["china", "Beijing", 1350],["India","Delhi", 1210],["Romania","Bucharest",21],["United States","Washington",307]]

india_capital = countries[1][1]
romania_times_china = countries[0][2] / countries[2][2]

print(india_capital)
print(romania_times_china)

stooges_two = ["Moe","Larry","Curly"]
stooges_two[2] = "Shemp"
print(stooges_two)

def replace_spy(list):
    list[2] = list[2] + 1

spy = [0,0,7]

replace_spy(spy)

print(spy)
