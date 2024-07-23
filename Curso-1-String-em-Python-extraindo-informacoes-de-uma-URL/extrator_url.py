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

extrator_url = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=Real&moedaDestino=dolar')
# Testes
# print('O tamanho da URL: ', len(extrator))
# print(extrator)
# valor_quantidade = extrator.get_valor_parametro('quantidade')
# print(valor_quantidade)

# Desafio do curso
valor_dolar = 5.58  # 1 dólar = 5.58 reais em 23.07.2024
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'Real' and moeda_destino == 'Dolar':
    valor_conversao = round(int(quantidade) / valor_dolar,2)
    print(f'O valor de R$ {quantidade} reais é igual a $ {str(valor_conversao)} dólares.')
elif moeda_origem == 'Dolar' and moeda_destino == 'Real':
    valor_conversao = round(int(quantidade) * valor_dolar,2)
    print(f'O valor de $ {quantidade} dólares é igual a R$ {str(valor_conversao)} reais.')
else:
    print(f'Câmbio de {moeda_origem} para {moeda_destino} não está disponível.')