'''统计一句话中，某个字符的出现次数，忽略大小写'''

def get_count(sentence,word):
    count=0
    for item in sentence:
        if word.upper()==item or word.lower()==item:
            count +=1
    return count

print(get_count('sssaddddsaass','a'))
