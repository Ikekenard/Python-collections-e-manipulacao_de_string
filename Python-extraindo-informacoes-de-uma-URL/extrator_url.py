import re



class ExtratorURL:
     def __init__(self,url):
          self.url = self.limpa_url(url)
          self.valida_url()
          
     def limpa_url(self,url):
          if type(url) == str:
               return url.strip()
          else:
               return ''
     
     def valida_url(self):
          if not self.url:
               raise ValueError(f'A url está vázia')
          
          padrão_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
          match = padrão_url.match(self.url)
          if not match:
               raise ValueError(f'A url não é válida.')

     
     def get_url_base(self):
          interrogacao = self.url.find('?')
          url_base = self.url[:interrogacao]
          return url_base
     
     def get_url_parametros(self):
          interrogacao = self.url.find('?')     
          url_parametros = self.url[interrogacao + 1:]
          return url_parametros
     
     def get_valor_parametro(self, parametro_busca):
          indice_parametro = self.get_url_parametros().find(parametro_busca)
          indice_valor = indice_parametro + len(parametro_busca) + 1
          indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
          # Condicional para ele separar ou não com o '&'
          if indice_e_comercial == -1:
               valor = self.get_url_parametros()[indice_valor:]
          else:
               valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
          return valor.title()
     
     def __len__(self):
          return len(self.url)
     
     def __str__(self):
          return f'URL: {self.url} \nParâmetros: {self.get_url_parametros()} \nURL Base: {self.get_url_base()}'

     def __eq__(self, other):
          return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=Real&moedaDestino=dolar'

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)

# Verifica que duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

# Busca o valor do parâmetro quantidade
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)