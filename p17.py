#one two three four five six seven eight nine ten eleven twelve thirteen fourteen fiveteen sixteen seventeen
#eighteen nineteen twenty

def letter_lenth(number):
    to_19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7
    thousand = 8
    ans = 0
    for x in range(1, number + 1):
        a = int(x%10)
        b = int((x%100 - a)/10)
        c = int((x - 10 * b - a)/100)
        if x < 20:
            ans += to_19[x]
        elif x > 999:
            ans += thousand + 3
        else:
            if x < 100:
                if a == 0:
                    ans += tens[b]
                else:
                    ans += tens[b] + to_19[a]
            else:
                if a == 0 and b == 0:
                    ans += to_19[c] + hundred
                elif x%(c*100) < 20:
                    ans += to_19[c] + hundred + 3 + to_19[x%(c*100)]
                elif a == 0:
                    ans += to_19[c] + hundred + 3 + tens[b]
                else:
                    ans += to_19[c] + hundred + 3 + tens[b] + to_19[a]
    return ans

print(letter_lenth(1000))