cpf = "29692002850" #cpf gerado aleatoriamente
novo_cpf = cpf[:-2] 

reverso = 10
total = 0
for i in range(19):
	if i > 8:
		i -= 9
	
	total += int(novo_cpf[i]) * reverso

	reverso -=1
	if reverso <2:
		reverso = 11
		d = 11 - (total % 11)
		if d > 9:
			d = 0
		total = 0
		novo_cpf += str(d)

if novo_cpf != cpf:
	print("cpf invalido")
else:
	print("cpf valido")
