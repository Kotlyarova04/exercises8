def filter_out(word):
    if word.isupper():
        return True


sentence = list(input())
begin = int(input())
end = int(input())
output = list(filter(filter_out, sentence[begin-1: end]))
print(len(output))
