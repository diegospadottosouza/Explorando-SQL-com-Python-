n = int(input())
funcionarios = []

for _ in range(n):
    id_func = int(input())
    nome = input()
    cargo = input()
    funcionarios.append({"id": id_func, "nome": nome, "cargo": cargo})

cargo_filtro = input()
resultado = [f["nome"] for f in funcionarios if f["cargo"] == cargo_filtro]
print(resultado)