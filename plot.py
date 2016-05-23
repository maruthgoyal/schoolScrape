import matplotlib.pyplot as plt

def pl(filename, t):

    dic = {}
    marks_axis = []
    freq_axis = []

    with open(filename) as f:

        for number in f:

            if int(number) in dic:
                dic[int(number)] += 1

            else:
                dic[int(number)] = 1

    for key in dic:

        marks_axis.append(key)
        freq_axis.append(dic[key])

    plt.bar(marks_axis, freq_axis, width=(1/1.5), color="red")
    plt.title(t)
    plt.show()





# MATH
pl('math', 'MATH 2016')

# PHYSICS
pl('phy', 'PHYSICS 2016')

#CHEMISTRY
pl('chem', 'CHEMISTRY 2016')

#ENGLISH
pl('english', 'ENGLISH 2016')
