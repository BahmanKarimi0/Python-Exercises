def gcd_strings(s1,s2):
    if s1+s2 != s2+s1:
        return ""
    uniq_litter = set(s1)
    max_len = min(len(s1), len(s2))
    len_s1 = len(s1)
    len_s2 = len(s2)
    while len_s2:
        len_s1, len_s2 = len_s2, len_s1 % len_s2
    i =0
    condition =""
    while i < max_len:
        condition += s1[i]

        if set(condition) == uniq_litter and condition in s1 and condition in s2:
            loop = condition*len_s1
            if loop in s1*len_s1:
                return condition
        i +=1
    return ""


print(gcd_strings("ABCABC", "ABC"))       # "ABC"
print(gcd_strings("AB", "ABABABABAB"))    # "AB"
print(gcd_strings("ABAB", "ABABABAB"))    # "AB"
print(gcd_strings("ABAB", "ABABAB"))      # "AB"
print(gcd_strings("AACBBC", "AACBBCAACBBC"))   # "AABBC"
print(gcd_strings("LEET", "CODE"))        # ""




