def romanToInt(s):
    romain = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i in range(len(s)):        
        temp = romain[s[i]]
        if (i != 0 and romain[s[i-1]] < romain[s[i]]):
            temp = temp - (romain[s[i-1]])*2
        total = total + temp
    #return total
    print(total)

def main():
    romanToInt("III")
    romanToInt("IV")
    romanToInt("IX")
    romanToInt("LVIII")
    romanToInt("MCMXCIV")

if __name__ == '__main__':
    main()
 
