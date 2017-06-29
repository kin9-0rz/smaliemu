# {'a': ['a': 'b': 'c'], 'l': 3, 'ret': ['a': 'b': 'c'], 's': 'abc'}
const-string s, "abc"
const/16 a, 0
const/16 l, 0

invoke-virtual {s}, Ljava/lang/String;->toCharArray()[C
move-result a
array-length l, a
