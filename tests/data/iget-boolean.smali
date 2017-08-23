#{'field': 0, 'ret': 0, 'v0': 0, 'vx': 0}
const/4 vx, 0x0
iput-boolean vx, vy, field
# Puts the boolean value located in vx into an instance field. The instance is referenced by vy.
iget-boolean v0, vy, field
return-object v0
