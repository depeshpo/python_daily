# the number of times that the substring occurs in the given string.

if __name__ == '__main__':
    string = 'ABCDCDC'
    substring = 'CDC'
    count = 0
    for i in range(0, len(string)-len(substring)+1):
        if string[i] == substring[0]:
            for j in range (0, len(substring)):
                flag = 1
                if string[i+j] != substring[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    print(count)
