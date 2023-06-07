#mocniny
"""def square_digits(num):
    z = str(num)
    strng = ""
    for y in z:
        done = int(y) * int(y)
        strng = strng + str(done)

    return int(strng)

nom = 9119
print(square_digits(nom))
"""
#pismeno zmení na index
"""def alphabet_position(text):
    letter_dic = {
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26",

    }
    strn = ""
    z = len(text)
    y = 0
    for x in text:
        if y != 0 and x.lower() in "abcdefghijklmnopqrstuvwxyz" and y != z:
            strn += " "
        y += 1
        if x.lower() in "abcdefghijklmnopqrstuvwxyz":
            strn += letter_dic[x.lower()]
    return strn



textt = "The sunset sets at twelve o' clock."

print(alphabet_position(textt))
"""
#roznásobky
"""
def persistence(n):
    x = len(str(n))
    if x > 1:
        help_result = 1
        for y in range(x):
            z = str(n)
            help_result = help_result * int(z[y])
        resultt = str(help_result)

    done = 1

    while True:
        zz = len(resultt)
        if zz > 1:
            result = 1
            for yy in range(zz):
                h = int(resultt[yy])
                if h != 0:
                    result = result * int(resultt[yy])

            resultt = str(result)
            done += 1
        else:
            break

    return done

num = 376556

print(persistence(num))"""
#pin z 4 a 6 iba čísla
"""
def validate_pin(pin):
    y = 0
    if len(pin) == 4 or len(pin) == 6:
        for x in pin:
            if x in "1234567890" and y == 0:
                x = x
            else:
                y = 1
        if y == 0:
            return True
        else:
            return False

    else:
        return False



puk = "12.0"
print(validate_pin(puk))
"""
#Stred slova
"""def get_middle(s):
    x = len(s)
    y = ""
    z = int(x / 2)
    print(z)
    if (x % 2) == 0:

        y += s[z-1] + s[z]
        return(y)

    else:
        y += s[z]
        return y


kata = "test"

print(get_middle(kata))"""
#Zmena znakov na #
"""def maskify(cc):
    x = len(cc)
    y = ""
    if x > 3:
        y += "#" * (x-4) + (cc[x-4:])
        return y
    else:
        return cc

c = ""
print(maskify(c))"""
#Vowel counter
"""def get_count(sentence):
    y = 0
    for x in sentence:
        if x in "aeiou":
            y += 1
    return y

c = "asodauisdui"
print(get_count(c))"""
#dna swap
"""def DNA_strand(dna):
    y = ""
    for x in dna:
        if x == "A":
            y += "T"
        elif x == "T":
            y += "A"
        elif x == "G":
            y += "C"
        else:
            y += "G"
    return(y)

dn = "ATTGC"
print(DNA_strand(dn))"""
#Same num x n o
"""def xo(s):
    xs = 0
    os = 0
    for x in s:
        if x.lower() == "x":
            xs += 1
        elif x.lower() == "o":
            os += 1
        else:
            pass
    if xs == os:
        return True
    else:
        return False

txt = "ooxx"
print(xo(txt))"""
#Smile counter
"""smiley = [';]', ':[', ';*', ':$', ';-D']

def count_smileys(arr):
    result = 0
    for x in arr:
        y = len(x)
        #print(y)
        #print(x[0] + "   " +x[1])
        if x[0] in ":;" and x[1] in ")D":
            result += 1
        if y == 3:
            #print("A")
            if x[1] in "-~" and x[2] in ")D":
                result += 1
    return result


print(count_smileys(smiley))"""
#First letter to end, adding ay -- ord na ascii chr naopak
"""text = 'Pig latin is cool !'
def pig_it(text):
    result = ""
    list = []
    list = text.split()
    #print(list)
    for z in list:
        x = len(z)
        y = 0
        for zz in range(x):
            if z[zz].lower() in "qwertzuioplkjhgfdsayxcvbnm":
                y += 1

        if y == x:
            string1 = z[0]
            string2 = z[1:]
            string3 = string2 + string1 + "ay"
            result += string3 + " "
        else: result += z
    xx = len(result) - 1
    if result[xx] == " ":
        resultt = result[:xx]
        return resultt
    else:
        return result


print(pig_it(text))"""
#5letter switch
"""text = "Hey fellow warriors"

def spin_words(sentence):
    list = sentence.split()
    result = ""
    for x in list:
        y = len(x)
        if y > 4:
            string1 = x[::-1]
            result += string1 + " "
        else:
            result += x + " "
    zz = len(result)
    if result[zz - 1] == " ":
        return result[:zz-1]
    else:
        return result

print(spin_words(text))"""
#Rozvetvenie čísla na 0lovité časti
"""int = 70304

def expanded_form(num):
    help_num = str(num)
    x = len(str(help_num))
    new_int = ""
    for y in range(x):
        z = str(help_num[y])
        if z != "0":
            new_int += help_num[y] + "0" * (x - y - 1) + " + "

    yy = len(new_int) - 1
    return(new_int[:yy - 2])


print(expanded_form(int))"""
#Camel case creator
"""text = "the-stealth-warrior"

def to_camel_case(text):
    result = ""
    yy = 0
    for x in text:
        if x in "-_":
            yy = 1
        else:
            if yy == 1:
                result += x.upper()
                yy = 0
            else:
                result += x
    return result

print(to_camel_case(text))"""
#String incrementer
"""text = "foo"

def increment_string(strng):
    xy = len(strng)
    new_string = "0"
    z = 0
    xx = 0
    for x in strng:
        if x in"0123456789":
            z += 1
            new_string += x
            xx = len(new_string)
    new_string2 = str(int(new_string) + 1)

    result = strng[:xy-xx + 1] + str(new_string2)
    return result

#print(text[:3])
print(increment_string(text))"""
#To seconds !!!
"""text = 6000001

def format_duration(seconds):
    x = seconds // 60
    result = ""
    end = "n"
    d = 0   #day
    y = 0   #hour
    z = 0   #mins
    t = 0   #secs
    if seconds > 0:
        if seconds == 3600:
            result += "1 hour"
            end = "y"
        elif seconds == 60:
            result += "1 minute"
            end = "y"
        elif seconds == 1:
            result += "1 second"
            end = "y"
        else:
            if x > 60:
                if x >= 1440:
                    d = x // 60 // 24
                y = x // 60 - (d * 24)
                z = x - (y * 60) - (d * 24 * 60)

            else:
                z = x
        t = seconds - (y * 60 * 60) - (z * 60) - (d * 24 * 60 * 60)
        if d == 1:
            result += "1 day, "
        elif d > 1:
            result += str(d) + " days, "
        if y != 0 and end != "y":
            result += str(y)
            if y == 1:
                result += " hour"
            else:
                result += " hours"
            if z == 0 or t == 0:
                result += " and "
            else:
                result += ", "

        if z != 0 and end != "y":
            result += str(z)
            if z == 1:
                result += " minute"
            else:
                result += " minutes"
            if t > 0:
                result += " and "


        if t != 0 and end != "y":
            result += str(t)
            if t == 1:
                result += " second"
            else:
                result += " seconds"
    else:
        result += "now"


    return result

print(format_duration(text))

#Dorobiť deň
"""
#string to int
"""
str_num = "twenty" #String to convert
def parse_int(string):
    y = "" #String for list
    list = [] # list of nums
    result = ""
    dresult = ""
    z = 0
    hunds = 0
    thous = 0
    teens = 0
    a = "n"
    num_dic = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "eleven": "11",
        "twelwe": "12",
        "thirteen": "13",
        "fourteen": "14",
        "fifteen": "15",
        "sixteen": "16",
        "seventeen": "17",
        "eighteen": "18",
        "nineteen": "19",
        "twenty": "2",
        "thirty": "3",
        "forty": "4",
        "fifty": "5",
        "sixty": "6",
        "seventy": "7",
        "eighty": "8",
        "ninety": "9",
        }
    if string in num_dic:
        result += num_dic[string]
        a = "y"
        z = 1
    elif string == "zero":
        return 0
    else:
        for x in string:
            if x in "qwertzuioplkjhgfdsayxcvbnm":
                y += x
            else:
                list.append(y)
                y = ""
        list.append(y)
        print(list)
        z = len(list)
        for z in list:
            if z in num_dic:
                result += num_dic[z]
            elif z == "hundred":
                hunds += 1
    zz = len(string)
    #print(z)
    #print(string[zz-2:])
    if hunds == 0 and thous == 0 and len(result) == 3 and a == "n":
        dresult = result[0] + result[2]
        #print("A")
    elif hunds == 1 and len(result) == 4 and a == "n":
        dresult = result[0] + result[1] + result[3]
        #print("B")
    elif z == 1 and string[zz-2:] == "ty":
        dresult += result + "0"
        #print("C")
    else:
        #print("D")
        if hunds != 0 and len(result) < 3:
            result += "00" * hunds
        elif thous != 0 and len(result) < 4:
            result += "000" * thous
        else:
            pass
    dresult.join(result)
    return int(dresult)

print(parse_int(str_num))"""
#Fibonacci perrimeter of recs
"""n_first = 5

def perimeter(n):
    list = [1, 1]
    #fib creation
    result = 0
    for i in range(n-1):
        list.append(list[i] + list[i+1])
    for y in list:
        result += y

    return result*4

print(perimeter(n_first))"""
#Dačo s učkom a n tým členom abo co
"""num = 10
def dbl_linear(n):
    list = [1]
    for x in range(n//2+1):
        y = 2*list[x] + 1
        z = 3*list[x] + 1
        list.append(y)
        list.append(z)
    zz = len(list)
    i = 0
    for i in range(zz):

        for j in range(zz - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return(list[n])

print(dbl_linear(num))"""
#Rot13 šifra
"""
txt = "EBG13 rknzcyr."
def rot13(s):
    result = ""
    chars = "abcdefghijklmnopqrstuvwxyz"
    a = 0
    for x in s:
        if x in chars or x in chars.upper():
            if ord(x) <= 122:
                if ord(x) <= 109:
                    a = ord(x) + 13
                    result += chr(a)
                else:
                    a = ord(x) - 13
                    result += chr(a)
            else:
                if ord(x) <= 77:
                    a = ord(x) + 13
                    result += chr(a)
                else:
                    a = ord(x) - 13
                    result += chr(a)
        else:
            result += x
    return result
print(rot13(txt))
"""
#N1 to n2 times
"""n_1 = 9
n_2 = 7

def last_digit(n1, n2):
    # y = 1
    # for x in range(n2):
    #     y = n1 * y
    # #return y
    # z = str(y)
    # z = z[len(z) - 1]
    # return int(z)

    return pow(n1, n2, 10)
print(last_digit(n_1, n_2))
"""
#Pyramidy kt. má dilino špatne
"""list = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
        ]
def longest_slide_down(pyramid):
    y = len(pyramid)
    result = 0
    index = 0
    xx = 0
    z = 0
    n_list = []
    n_list3 = []
    for x in range(y):
        n_list = pyramid[x]
        if x+1 <= y-1:
            n_list2 = pyramid[x + 1]
        if xx == 0:
            z = max(pyramid[x])
            xx += 1
        else:
            n_list3 = []
            n_list3.append(n_list[index])
            n_list3.append(n_list[index+1])
            if index + 1 <= y-1:
                 z = max(n_list3)
        print(z)

        index = n_list.index(z)

        result += z
    #return result

print(longest_slide_down(list))

#indexx = list[2].index(4)
#print(indexx)"""
#beeramid
"""
bnus = 9
prce= 2
def beeramid(bonus, price):
    result = 0
    price_result = 0
    x = 1
    while True:
        if price_result <= bonus:
            price_result = x*x * price + price_result
            x += 1
            #print(price_result)
            if price_result <= bonus:
                result += 1
        else:
            break
    return result


print(beeramid(bnus, prce))
"""
#StrngSum
"""
x= 1
y = 2
def sum_strings(x, y):
    list = []
    list.append(int(x))
    list.append(int(y))
    result = sum(list)

    return str(result)

print(sum_strings(x,y))"""
#(L33T+Grεεκ)Case
"""inp = "CodeWars"
def gr33k_l33t(string):
    letter_dic = {
        "a": "α",
        "b": "β",
        "d": "δ",
        "e": "ε",
        "i": "ι",
        "k": "κ",
        "n": "η",
        "o": "θ",
        "p": "ρ",
        "r": "π",
        "t": "τ",
        "u": "μ",
        "v": "υ",
        "w": "ω",
        "x": "χ",
        "y": "γ",

    }
    x= len(string)
    result = ""
    for i in string:
        if i.lower() in letter_dic:
            result += letter_dic[i.lower()]
        else:
            result += i.lower()

    return result

print(gr33k_l33t(inp))"""
#Merging 2s to 1s
"""s = "codewars"
part1 = "cdw"
part2 = "oears"

def is_merge(s, part1, part2):
    xx = len(part1)
    yy = len(part2)
    y = 0
    strng = ""
    result = 0
    step = 0
    q = 1
    z = len(s)
    for i in range(z):
        step += 1
        x = s[i]
        strng += x
        if x in part1 and q == 1:
            result += 1
        elif x in part2 and q == 2:
            result += 1
        else:
            pass
        if q == 1:
            if step <= yy+1:
                q = 2
        elif q == 2:
            if step <= xx+1:
                q = 1
        else:
            pass

    if s == strng:
        resultt = True
    else:
        result = False
    return resultt


print(is_merge(s, part1, part2))
"""
#domain from URL
"""
url = "codewars.com/kata"

def domain_name(url):
    x = url.find("/")
    y = url.find(".")
    url_help = url[y+1:]
    yy = url_help.find(".") + 4
    #print(x,y,yy)
    z = y - x - 2
    zz = yy - y - 1
    result = ""
    if x > 0 and y > 0 and x < y:
        for i in range(z):
            result += url[x + 2 + i]
    elif x > y:
        for i in range(y):
            result += url[i]
    else:
        for i in range(zz):
            result += url[y + 1 + i]
    return result


print(domain_name(url))
"""
#moving 0s
"""x = [1, 0, 1, 2, 0, 1, 3]
def move_zeros(lst):
    result = []
    x = 0
    for i in lst:
        if i != 0:
            result.append(i)
        else:
            x += 1
    for ii in range(x):
        result.append(0)
    return result

print(move_zeros(x))"""
#Upper case to _ case
"""x = "1"

def to_underscore(string):
    result = ""
    for i in string:
        if i in "qwertzuiopasdfghjklyxcvbnm0123456789":
            result += i
        else:
            result += "_"
            result += i.lower()
    if result[0] == "_":
        result = result[1:]

    return result

print(to_underscore(x))"""
#make looper func
"""def make_looper(string):
    x = 0
    result = ""
    if x == 3:
        x = 0
    result = string[x]
    x += 1
    return string[x]

abc = make_looper('abc')

print(abc)"""
#RomanToInt
"""
#1. menšie, väčšie
dic = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
s = "III"
class Solution:
    def romanToInt(self, s: str) -> int:
        ints_of_roman = []
        x = ""
        for i in s:
            x = dic[i]
            ints_of_roman.append(x)

        for i in range(len(ints_of_roman) - 1):
            if ints_of_roman[i + 1] <= ints_of_roman[i]:
                continue
            else:
                ints_of_roman[i] = ints_of_roman[i] * -1

        return sum(ints_of_roman)



print(Solution.romanToInt(Solution, s))
"""
# Two Sum - z listu sčítať čísla pre daný výsledok
"""
nums = [2, 5, 5, 11]
target = 10
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []

print(Solution.twoSum(Solution, nums, target))
"""
#Palindrome
"""
list = [1,2,2,1]
class Solution:
    def isPalindrome(self, head):
        if len(head) % 2 == 1:
            return False

        for i in range(1, int(len(head)/2) + 1):
            if head[i - 1] != head[-i]:
                return False
        return True

print(Solution.isPalindrome(Solution, list))

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
    """
#Longest Substring Without Repeating Characters
"""
n = "pwwkew"
class Solution:
    def lengthOfLongestSubstring(self, s):
        n_del = nn = s
        n_new = ""
        result = ""

        for i in nn:
            n_new = n_new + i
            n_del = n_del.replace(i,"",1)
            if n_new in n_del:
                result = n_new

            else:
                print(result)
                return len(result)

print(Solution.lengthOfLongestSubstring(Solution, n))
"""
#Remove duplicate list values
"""
n = [1,1,2]
class Solution:
    def removeDuplicates(self, nums):
        k = 0
        hash = {}
        list = nums
        for i in list:
            if i in hash:
                hash[i] += 1
                k += 1
                list.append("_")
                list.remove(list[i])
            else:
                hash[i] = 1
        return k, list

print(Solution.removeDuplicates(Solution, n))
"""
#searchInsert
"""
n = [1,3,5,6]
t = 7
class Solution:
    def searchInsert(self, nums, target):
        l = []
        k = 0
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i < target or k == 1:
                l.append(i)
            else:
                k = 1
                l.append(target)
                l.append(i)
        if target not in nums:
            l.append(target)
        return l.index(target)

print(Solution.searchInsert(Solution,n,t))
"""
#lengthoflastword
"""
n = "   fly me   to   the moon  "

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return (len(word[-1]))

        x = s[::-1]
       result = 0
       spaces = 0
       while True:
           for i in x:
               if i != " ":
                   result += 1
               elif result == 0 and i == " ":
                   pass
               else:
                   return result
           


print(Solution.lengthOfLastWord(Solution, n))
"""
#PascalTriangle
"""
class Solution(object):
    def generate(self, numRows):
        # Create an array list to store the output result...
        output = []
        for i in range(numRows):
            if(i == 0):
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                # Calculate for each of the next values...
                while(j < i):
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j-1] + prev[j])
                    j+=1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output    
"""
#Valid palindrome
"""
s = "0P"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s:
            if i.lower().isalpha() or i.isdigit():
                x += i.lower()
        print(x)
        if x == x[::-1]:
            return True
        else:
            return False

print(Solution.isPalindrome(Solution, s))
"""
#1Digitfromlist
"""
s = [1]
class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        l = list(dic.values())
        y = l.index(min(l))
        x = list(dic.keys())
        return x[y]
"""
#LinkedListCycle
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}

        while (head):
            if head.next not in nodes:
                nodes[head.next] = 1
            else:
                return True
            head = head.next

        return False
"""
#2 list intersection
"""
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
class Solution:
    def getIntersectionNode(self, headA, headB):
        x, y = len(headA), len(headB)
        if x < y:
            k = 1
        else:
            x = y
            k = 2
        for i in range(x):
            if k == 1:
                if headA[i] in headB:
                    return str(headA[i])
            elif k == 2:
                if headB[i] in headA:
                    return str(headB[i])
            else:
                return None
"""




print(Solution.getIntersectionNode(Solution, listA, listB))
