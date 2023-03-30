print("Digite a altura de 5 girafas para saber qual a maior delas: ")
print("Digite a altura da girafa 1:")
g1=float(input())
print("Digite a altura d girafa 2:")
g2=float(input())
print("Digite a altura da girafa 3:")
g3=float(input())
print("Digite a altura da girafa 4:")
g4=float(input())
print("Digite a altura da girafa 5:")
g5=float(input())

if g1>g2 and g1>g3 and g1>g4 and g1>g5:
    print("A girafa 1 é a maior e tem: ",g1,"de altura")
elif g2>g1 and g2>g3 and g2>g4 and g2>g5:
    print("A girafa 2 é a maior e tem: ",g2,"de altura")
elif g3>g1 and g3>g2 and g3>g4 and g3>g5:
    print("A girafa 3 é a maior e tem: ",g3,"de altura")
elif g4>g1 and g4>g2 and g4>g3 and g4>g5:
    print("A girafa 4 é a maior e tem: ",g4,"de altura")
else: 
    print("A girafa 5 é a maior e tem: ",g5,"de altura")

