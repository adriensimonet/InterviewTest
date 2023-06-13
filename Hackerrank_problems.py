###Arrays

#minimum Swap2
def minimumSwaps(arr):
    list_visit = [False for x in arr]
    res = 0
    for i in range(len(arr)):
        if not list_visit[i]:
            b=arr[i]-1
            lenght=1
            list_visit[i] = True
            while b!= i:
                list_visit[b]=True
                b=arr[b]-1
                lenght+=1
            res+=lenght-1
    return res

#works but do not pass all tests
def arrayManipulation_worst(n, queries):
    l = [0]*n
    for q in queries:
        for i in range(q[0], q[1]+1):
            l[i-1]+=q[2]
    return max(l)

#best one
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval

#dictionarys (ransom note)
def checkMagazine(magazine, note):
    for x in note:
        try:
            magazine.remove(x)
        except:
            print('No')
            return
    print('Yes')

#Sherlock and Anagrams

def getsubstring(s):
    res = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res.append(s[i:j])
    return res


def sherlockAndAnagrams(s):
    substrings = getsubstring(s)
    res = {}
    for x in substrings:
        temp = ''.join(sorted(x))
        if temp in res:
            res[temp]+=1
        else:
            res[temp] = 1
    return sum([sum(range(res[x])) for x in res if res[x]>1])

#If a substring appears k times, then the total possible anagrams of that substring will be 1+2+3+......+(k-1)
#Example in string "kkkk".
#Total possible anagrams of ["k","k"] will be 1+2+3 = 6, as there are 4 substrings of "k" in "kkkk".
#Total possible anagrams of "kk" will be 1+2 = 3, as there are 3 substrings of "kk" in "kkkk".
#Total possible anagrams of "kkk" will be 1 , as there are 2 substrings of "kkk" in "kkkk".
#Total anagrams of the string "kkkk" = 6+3+1 = 10.

##Count Triplets
def countTriplets(arr, r):
    count = 0
    before = {}
    after = {}
    for v in arr:
        if v in after:
            after[v]+=1
        else:
            after[v]=1
    for v in arr:
        after[v]-=1
        if v%r == 0 and v//r in before and v*r in after:
            count+=before[v//r]*after[v*r]
        if v in before:
            before[v]+=1
        else:
            before[v]=1
    return count

from collections import Counter
def freqQuery_notoptimized(queries):
    res_dic = Counter()
    res = []
    for x, y in queries:
        if x == 1:
            res_dic[y]+=1
        elif x == 2:
            if res_dic[y]>0:
                res_dic[y]-=1
        else:
            if y in res_dic.values():
                res.append(1)
            else:
                res.append(0)
    return res


def freqQuery(queries):
    res_dic = Counter()
    dic_val = Counter()
    res = []
    for x, y in queries:
        if x == 1:
            dic_val[res_dic[y]] -= 1
            res_dic[y] += 1
            dic_val[res_dic[y]] += 1
        elif x == 2:
            if res_dic[y] > 0:
                dic_val[res_dic[y]] -= 1
                res_dic[y] -= 1
                dic_val[res_dic[y]] += 1
        else:
            res.append(1 if dic_val[y] > 0 else 0)

    return res

#Mark and Toys
def maximumToys(prices, k):
    prices = sorted(prices)
    count=0
    res = 0
    i = 0
    while res <= k and i < len(prices):
        if res + prices[i] <= k:
            res+=prices[i]
            count+=1
        else:
            return count
        i+=1
    return count

#Fraudulent Activity Notifications

#not optimal solution
def median_func(l):
    if len(l) == 0:
        return None
    elif len(l)%2 == 0:
        return (l[len(l)//2-1]+l[len(l)//2])/2
    else:
        return l[len(l)//2]

def activityNotifications_notoptimal(expenditure, d):
    count=0
    if len(expenditure)<d+1:
        return 0
    else:
        for i in range(d, len(expenditure)):
            temp = sorted(expenditure[(i-d):i])
            median = median_func(temp)
            if median is not None and expenditure[i]>=median*2:
                count+=1
        return count

#semi-optimal solution

import statistics
from collections import deque
def activityNotifications2(ex, d):
    a=ex[:d]
    a=deque(a)
    c=0
    m=statistics.median(a)
    for i in range(d,len(ex)-1):
        if ex[i]>= 2*m:
            c+=1
        a.popleft()
        a.append(ex[i])
        m=statistics.median(a)
    return c

#optimal solution
import bisect

def med(arr, d, m):
    if d % 2 == 0:
        return sum(arr[m - 1:m + 1]) / 2
    else:
        return arr[int(m)]


def activityNotifications(exp, d):
    m = d // 2
    c = 0
    arr = sorted(sorted(exp[:d]))
    for i in range(d, len(exp)):
        if exp[i] >= 2 * med(arr, d, m):
            c += 1
        del arr[bisect.bisect_left(arr, exp[i - d])]
        bisect.insort(arr, exp[i])
    return c

#using counting sort, we can do that: https://www.youtube.com/watch?v=46V6tnxy_Vs

def countInversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    n1 = n//2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans =  countInversions(arr1) + countInversions(arr2)
    i1, i2 = 0, 0
    for i in range(n):
        if i1 < n1 and (i2>=n2 or arr1[i1]<= arr2[i2]):
            arr[i] = arr1[i1]
            ans+=i2
            i1+=1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2+=1
    return ans


from collections import Counter


def groupTransactions(transactions):
    res = {}
    for k in transactions:
        if k not in res:
            res[k] = 1
        else:
            res[k] += 1
    res = dict(sorted(res.items(), key=lambda item: item[0]))
    res = dict(sorted(res.items(), key=lambda item: item[1]))
    return res


def prison(n, m, h, v):
    horizontal_gap = 1
    vertcial_gap = 1

    vertical = [1 for x in range(m)]
    horizontal = [1 for x in range(n)]

    if len(h) == 0 and len(v) == 0:
        return vertcial_gap * horizontal_gap

    for i in v:
        vertical[i - 1] = 0
    for j in h:
        horizontal[j - 1] = 0

    temp= 1
    for k in range(len(vertical)):
        if vertical[k] == 1:
            temp = 1
        if vertical[k] == 0:
            temp += 1
            if temp > vertcial_gap:
                vertcial_gap = temp
    temp=1
    for k in range(len(horizontal)):
        if horizontal[k] == 1:
            temp = 1
        if horizontal[k] == 0:
            temp += 1
            if temp > horizontal_gap:
                horizontal_gap = temp
    return horizontal_gap * vertcial_gap

#
def makeAnagram(a, b):
    dic_a = Counter()
    dic_b = Counter()
    res=0
    for x in a:
        dic_a[x]+=1
    for y in b:
        dic_b[y]+=1

    for x in set(list(dic_a.keys())+list(dic_b.keys())):
        res+=abs(dic_a[x]-dic_b[x])
    return res

def isValid(s):
    char_dict={}
    for char in s:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    min_count = char_dict[char]
    max_count = char_dict[char]
    count_dict = {}
    for char, value in char_dict.items():
        if value in count_dict:
            count_dict[value]+=1
        else:
            count_dict[value] =1
        if value < min_count:
            min_count = value
        elif value > max_count:
            max_count = value
    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[max_count]==1 and max_count - min_count ==1:
            return 'YES'
        elif count_dict[min_count]==1 and min_count ==1:
            return 'YES'
    return 'NO'

def gameWinner(colors):
    dic={'w':0, 'b':0}
    dic_temp={'w':0, 'b':0}
    temp = colors[0]
    dic_temp[temp]+=1
    i=0
    for x in colors[1:]:
        i+=1
        dic_temp[x] += 1
        if x == temp:
            pass
        if (x != temp and dic_temp[temp]>=3) or (dic_temp[temp]>=3 and i==len(colors)-1):
            dic[temp]+=dic_temp[temp]-2
            dic_temp[temp]=0
        elif x!=temp:
            dic_temp[temp] = 0
        temp=x
    return 'bob' if dic['b'] >= dic['w'] else 'wendy'

if __name__ == '__main__':
    test=gameWinner('wwbbwww')
    #test = makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke')
    print()