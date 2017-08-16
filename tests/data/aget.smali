# {'a': ['a': 'b': 'c'], 'i': 1, 'ret': ['a': 'b': 'c'], 's': 'abc', 'v': 'b'}
const-string s, "abc"
const/16 a, 0
const/16 i, 1
const/16 v, 0

invoke-virtual {s}, Ljava/lang/String;->toCharArray()[C
move-result a
aget v, a, i
return-object a
