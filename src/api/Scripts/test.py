# popuf = open('Puerto Rico_population.txt', 'w')
name = "Power County"
with open('co_est2020.txt') as file:
    lines = file.readlines()
    # print(lines)

    for line in range(len(lines)):
        line_  =lines[line].split(',')
        # print(line_[6])
        if line_[6] == name:
            print(line_[6], line_[-1])
        # if (lines[line][:-1]) == name:
        #     print(lines[line][:-1]+' County')
#     print(lines)
#     count =0
#     # for line in range(len(lines)):
#         # count += 1
#         # print(lines[line])
#         if lines[line][:-3].isalpha():
#             county = lines[line]
#             # print(county)

#         if lines[line].endswith('%\n'):
#             popu = lines[line-2]

#         try:
#             popuf.write(county+' '+popu)
#         except:
#             continue
# popuf.close()