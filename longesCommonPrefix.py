def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()

    prefix = strs[0]

    for i in range(len(prefix)):
        # print('i: '+str(i))
        for string in strs[1:]:
            # print('str: '+string)
            # print('string-I: '+string[i])
            # print('prefix-I: '+prefix[i])
            if string[i] != prefix[i]:
                return prefix[:i]
    return prefix


strs = ["abb", "abc"]

print("RES: "+longestCommonPrefix(strs))
