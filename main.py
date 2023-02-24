#IMPORTS
import re
import requests

#FROM
from cpf_cnpj import Documento
from validate_docbr import CNPJ
from telefones_br import TelefonesBr
from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

#PRINT CPF
exemplo_cpf = "15316264754"
documento_cpf = Documento.cria_documento(exemplo_cpf)
print("Número do CPF:", documento_cpf)

#PRINT CNPJ
exemplo_cnpj = "35379838000112"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print("Número do CNPJ:", documento_cnpj)

#PRINT TELEFONE
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print("Número de telefone:", telefone_objeto)

#PRINT DATA
hoje = DatasBr()
print("Data de Hoje:", hoje.format_data())
print("Data de Cadastro:", hoje.tempo_cadastro())

#PRINT ENDEREÇO
cep = "21061590"
objeto_cep = BuscaEndereco(cep)
cep, logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()
print("Endereço:", cep, logradouro, bairro, cidade, uf)