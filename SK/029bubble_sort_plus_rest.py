nums = [1, 5, 2, 3, 8, 4, 100, 7 ]

for i in range(len(nums)):
    y = 1
    for y in range(len(nums)):
        if nums[i] > nums[y]:
            pass
        else:
            z = nums[i]
            nums[i] = nums[y]
            nums[y] = z
#print(nums)

#30 list merginf

#31
PAIRS = {
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}
def is_valid(s):
    st = []
    for c in s:
        if c in PAIRS:
            st.append(PAIRS[c])
        else:
            if len(st) == 0:
                return False
            if c != st[-1]:
                return False
            st.pop()
    if len(st) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_valid("(") )