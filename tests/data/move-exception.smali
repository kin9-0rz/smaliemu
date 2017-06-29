# {'a': IndexError('string index out of range':), 'i': 100, 'ret': None, 's': 'hello'}
const-string s, "hello"
const/12 i, 100

:try_start_0

    invoke-virtual {s, i}, Ljava/lang/String;->charAt(I)C

:try_end_0
.catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

:catch_0
move-exception a