
from rest_framework import serializers
from  clientes.models  import Cliente
from  clientes.valitadors import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'
    
    def validate(self, data):
            if not cpf_valido(data['cpf']):
               raise  serializers.ValidationError({'cpf':"O cpf inválido"})
            if   nome_valido(data['nome']):
                raise   serializers.ValidationError({ 'nome':'Não inclua número neste campo'})
            if  not celular_valido(data['celular']):
                raise  serializers.ValidationError({ 'celular':"celular teve seguir este modelo: 11 99999-9999"})
            return data