#Atividade 2, Calcular enésimo termo de uma pg

n = float(input("Digite o n:"))
a1 = float(input("Digite o a1:"))
q = float(input("Digite o q:"))

an = a1*q**(n-1)

print("O enésimo termo é",an)