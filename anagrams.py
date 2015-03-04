class LetterInventory():

    def __init__(self, word):
        word = word.lower()
        self.inv = {}
        for i in range(97,123):
            self.inv[chr(i)] = word.count(chr(i))

    def __sub__(self, li2):
        new_li = LetterInventory("")
        for i in range(97,123):
            count_self = self.inv[chr(i)]
            count_li2 = li2.inv[chr(i)]
            new_li.inv[chr(i)] = count_self - count_li2 if count_self > count_li2 else count_li2 - count_self
        return new_li

    def __contains__(self, li2):
        new_dict = {}
        for i in range(97,123):
            count_self = self.inv[chr(i)]
            count_li2 = li2.inv[chr(i)]
            new_dict[chr(i)] = count_self - count_li2
        for i in new_dict.values():
            if i < 0:
                return False
        return True

    def __str__(self):
        letters = ""
        for i in range(97,123):
            count = self.inv[chr(i)]
            if count > 0:
                letters += chr(i)*count
        return letters

def anagrams(filename, s):
    word_list = parse(filename)
    word_list = prune_by_length(word_list, 10)
    word_dicts = compute_invs(word_list)
    li_s = LetterInventory(s)
    word_dicts = prune_by_inv(word_dicts, li_s)

    return anagram_helper(word_dicts, li_s, [])

def anagram_helper(my_dict, li_s, matches):
    if len(str(li_s)) == 0:
        return [matches] if len(matches) > 0 else []

    combinations = []
    for i in my_dict.keys():
        if my_dict[i] in li_s:
            new_list = li_s - my_dict[i]
            combinations += anagram_helper(my_dict, new_list, matches + [i])
    return combinations

def parse(filename):
    return [x.strip("\n").lower() for x in open(filename).readlines()]

def compile_list(list_pos):
    return ["".join(words) for words in list_pos]

def compute_invs(words):
    return {j : LetterInventory(j) for j in words}

def prune_by_inv(my_dict, li):
    keys = my_dict.keys()
    for i in keys:
        if my_dict[i] not in li:
            del my_dict[i]
    return my_dict

def prune_by_length(word_list, n):
    return [x for x in word_list if len(x) >= 10]

def main():
    list_pos = anagrams("w_words.txt", "aabdddeeeeeeggggiiiiiikllnnprrsssttwwwww")
    print compile_list(list_pos)

main()
