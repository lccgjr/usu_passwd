# Rotina principal usuario/senha
# Feito por Luis Carlos Gonçalves
#
# primeiro solicita a digitação de um email válido
#
# ================================================
#
#
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
# Modulo para testar se email é válido
#
#
def testa(email):
    if(re.search(regex,email)):
        return True
    else:
        return False
#
# 
#
email = str(input('Digite um email válido (formato nome@dominio)\n'))
print (email)
#
# Chama o módulo que testa se o email é válido
#
testa(email)
if testa(email):
    print('valido')
else:
    print('invalido')
#
# Acessa banco de dados e verifica se email está cadastrado
