#!/usr/bin/env python3

from puresnmp import walk
import sys

# Variaveis
OID = '.1.3.6.1.4.1.3902.1012.3.13.1.1.1'
params = sys.argv

# Print inicio
print("[")

# Laço para cada index encontrado no snmpwalk
for row in walk(params[1],params[2], OID):
    # Oid completa
    oidfull = (row[0])
    # Pega o index
    index = (oidfull[13])
    # Converte o index para inteiro
    indexint = int(index)
    # Convert o index para binario
    binario = format(indexint, "b")
    # Separa por bits e converte para decimal
    tipo = int(binario[0:1], 2)
    slot = int(binario[1:13], 2)
    porta = int(binario[13:21], 2)

    # Print em formato json
    print("\t")
    print("\t{\n")
    print(f'\t\t"{"{#GPON_INDEX}"}": "{index}",')
    print(f'\t\t"{"{#GPON_NAME}"}": "{slot}/{porta}"')
    print("\t},\n")

print("\t{\n")
print(f'\t\t"{"{#TESTE}"}": "OK"')
print("\t}\n")

# Print fim
print("]")
