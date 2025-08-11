"""
set() é utilizada para criar um conjunto ,
que é uma coleção não ordenada e
não indexada de elementos únicos

set e conjunto é a mesma merda!

add() - adiciona;
update() - atualiza;

"""
# EXENPLO 1

# s1 = set() 
# # isso tbm é um set
# s1 = {1,2,3,4,5}

# s1.add(1)
# print(s1)

# s1.update('a')
# print(s1)

# s1.update('python')# update acaba iterando cada letra até mesmo espaços
# print(s1)


# l1 = [1,2,1,1,3,4,5,6,6,7,8,8, 'luiz', 'luiz']
# l1 = set(l1)#resolveu as repetições e virou conjunto
# l1 = list(l1)# virou lista novamente
# print(l1)




# EXEMPLO 2

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 # Esse | quer dizer União
print(s3)

# EXEMPLO 3
s3 = s1 & s2 # Uma interseção o os dois tem em comum
print(s3)

# EXEMPLO 4
s3 = s1 - s2 #diferença
print(s3)

# EXEMPLO 5
s3 = s1 ^ s2 # symmertric_diferença ^(element que estão nos dois sets,
             # mas não nos dois)
print(s3)