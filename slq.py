sql = '''SELECT * FROM LEITURAS'''
leituras = query(sql)
for leitura in leituras:
  print(leitura)