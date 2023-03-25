def longest_substring(s):
  
    max_len = 0
    i = 0
    j = 0
    seen = set()

    while j < len(s):
        # check if character has been seen before
        if s[j] not in seen:
            seen.add(s[j])
            j += 1
            # see if substring length is greater or the main string and set the greater one to max_len
            max_len = max(max_len, len(seen))
        else:
            seen.remove(s[i])
            i += 1

    return max_len 

print(longest_substring("abcabcbb"))