import re
from validate_docbr import CPF

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)
  

def nome_valido(nome):
    return  nome.isalpha()

def celular_valido(numero_celuar):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,numero_celuar)
    print(resposta)
    print(numero_celuar)
    return resposta
         
     

       
