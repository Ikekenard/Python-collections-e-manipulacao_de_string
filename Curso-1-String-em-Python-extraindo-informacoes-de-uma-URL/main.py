# Url abse
# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = ''
print(f'\nUrl: {url}\n')

# Limpeza URL usando strip()
url = url.strip()

# Válidação da URL
if url == '':
     raise ValueError(f'A url está vázia')


# Separa base e parametros 
interrogacao = url.find('?')
url_base = url[:interrogacao]
url_parametros = url[interrogacao + 1:]
print(f'Parametros da url: {url_parametros}')

# Busca o valor de um parametro por meio da separção '?' '&'
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)

# Condicional para ele separar ou não com o '&'
if indice_e_comercial == -1:
     valor = url_parametros[indice_valor:]
else:
     valor = url_parametros[indice_valor:indice_e_comercial]

print(f'Valor da moeda Origem: {(valor).title()}')

