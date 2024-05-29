# THEORY ONE
# assumption that the string is valid if the ascii 
# difference between the characters is 1
def isValid_ascii(s: str) -> bool:
    for c in range(1,len(s),2):
        if ord(s[c]) - ord(s[c - 1]) != 1:
            return False
    return True
# well it turns out that this is not the case
# ---


# THEORY TWO
# keep a record of corresponding pairs of parenthesis
# and compare string against this record
def isValid_record(s: str) -> bool:
    pairs = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    str_len = len(s)
    if str_len % 2 != 0:
        return False
    for i in range(1, str_len, 2):
        if pairs[s[i-1]] != s[i]:
            return False
    return True
# it turns out that this does not work for all cases
# eg: "{[]}". I guess I did not understand the problem well enough
# ---


# THEORY THREE
# - keep track of opened prth.
# - remove from record when corresponding closing prth is found
# - repeat until all opened prth are closed and return True
# - if at the end, you still have unpaired prth, return False
def isValid(self, s: str) -> bool:
    pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    str_len = len(s)
    if str_len % 2 != 0:
        return False

    open_prths = pairs.values()
    if s[0] not in open_prths:
        return False
    
    yet_to_close_prths = [s[0]] 
    for i in range(1, str_len):
        unk_prth = s[i]
        print(unk_prth, yet_to_close_prths)

        if unk_prth in open_prths:
            #check is open prth
            yet_to_close_prths.append(unk_prth)
        else:
            #then it's close prth; check can close
            if len(yet_to_close_prths) == 0:
                return False

            corresponding_open_prth = pairs[unk_prth]
            if corresponding_open_prth in yet_to_close_prths[-2:]:
                index_of_open_prth = yet_to_close_prths.index(corresponding_open_prth)
                if yet_to_close_prths.count(corresponding_open_prth) == 1:
                    yet_to_close_prths = yet_to_close_prths[:index_of_open_prth]
                else:
                    yet_to_close_prths = yet_to_close_prths[:-2]
            else:
                return False
    return len(yet_to_close_prths) == 0

# THEORY FOUR
# same theory but better with understanding of the problem
# the rules were not made clear:
# test cases:
# "({[)" -> False
# "({[]})" -> True
# "([)" -> False
# "([)]" -> False
# "[[[]" -> False
# "{[]}" -> True
def isValid(s: str) -> bool:
    pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    open_prths = pairs.values()
    if s[0] not in open_prths:
        return False
    
    stack = []
    for c in s:
        if c in open_prths:
            stack.append(c)
        else:
            corr_open_prth = pairs[c]
            if len(stack) == 0:
                return False
            if corr_open_prth in stack[-1]:
                stack = stack[:-1]
            else:
                return False
    return len(stack) == 0

# NOW WE OPTIMIZE
# optimization with Python
def isValid(s: str) -> bool:
    pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    if len(s) % 2 != 0:
        return False

    if s[0] not in pairs.values():
        return False
    
    stack = []
    for c in s:
        if c not in pairs:
            stack.append(c)
        elif stack and pairs[c] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


# ------------ LESSONS LEARNT ------------
# - understand the problem well
# - know different cases and test with different cases
# - do not assume
