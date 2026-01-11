n = int(input())
funcionarios = []

for _ in range(n):
    nome = input()
    horas_trabalhadas = int(input())
    valor_hora = float(input())
    funcionarios.append({"nome": nome, "horas_trabalhadas": horas_trabalhadas, "valor_hora": valor_hora})

for f in funcionarios:
    salario = f["horas_trabalhadas"] * f["valor_hora"]
print(f"{f['nome']}: {salario:.1f}")