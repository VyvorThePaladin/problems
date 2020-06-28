from pwnlib.util.fiddling import unhex

nums = unhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))

list_strings = list(strings)

for i in range(len(list_strings)):
    if "crypto" in list_strings[i]:
        print(i, ":", list_strings[i])