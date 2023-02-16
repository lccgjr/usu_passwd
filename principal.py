# Rotina principal usuario/senha
# Feito por Luis Carlos Gonçalves
#
# primeiro solicita a digitação de um email válido
#
# ================================================
solicitaemail = str(input('Digite um email válido (formato nome@dominio)\n'))
print (solicitaemail)
#
# Chama o módulo que testa se o email é válido
#
import testaemail
testaemail.testa(solicitaemail)
#
