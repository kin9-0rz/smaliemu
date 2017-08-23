#{'ret': None, 'v2': 'hello world', 'v3': 'hello', 'v4': ' world'}

new-instance v2, Ljava/lang/StringBuilder;
const-string v3, "hello"
invoke-direct {v2, v3}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
const-string v4, " world"
invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
