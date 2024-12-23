''''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio
==================================
Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''

# https://www.bytebank.com.br/cambio
import re 

url = 'https://www.bytebank.com.br/cambio'
padrão_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrão_url.match(url)

# .search é quando se quer buscar um padrão em uma string
# .match é para ver se uma string inteira bate com o padrão estabelecido

if not match:
     raise ValueError(f'A url não é válida.')

print(f'A url é válida')