import json

# read in file and parse into dictionary of dictionaries
def readData(filename):
    data = []
    for cat in range(0,10):
        data.append([[[],[]],[[],[]]])
        for i in range(0,2):
            for j in range(0,2):
                for k in range(0,13):
                    data[cat][i][j].append([0] * 12)
    # reads in a file line by line
    with open(filename, encoding='utf-8') as a_file:

        for x in a_file:
            tweetCat = x.strip().split(',')
            cat = int(tweetCat.pop())
            for i in range(0, 12):
                j = i + 1
                while j < 12:
                    data[cat][int(tweetCat[i])][int(tweetCat[j])][i][j] = data[cat][int(tweetCat[i])][int(tweetCat[j])][i][j] + 1
                    j = j + 1
    return data
# start doing stuff here
k = readData('line_counts.csv')
with open('data.txt', 'w') as outfile:
    json.dump(k, outfile)
