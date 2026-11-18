import re as reg

#funções
#re.sercch() --> procura padrao em qualquer parte do texto
#re.match() --> procura desde o inicio da string
#re.findall() --> devolve todas as occorrenciass
#re.split() --> divide a string em partes por padrao

padraoemail=r"^[\w\.]+@[\w]+\.\w+$"
# ^ --> inicio da string
# [\w\.]+ --> letras, numeros, undersccore, pontos ou hifens
# @ --> arroba
# \.\w+ --> ponto seguido de letras (ex:.com .pt)
#$ --> fim da string

padrao="python"
texto="Eu gosto das manhas de python elas sao muito boas e adoro programar em python é uma locura"
email="atec@atec.pt"

print(reg.search(padrao,texto))

print(reg.match(padrao,texto))

print(reg.search(padraoemail,texto))
print(reg.match(padraoemail,texto))

print(reg.search(padraoemail,email))
print(reg.match(padraoemail,email))

print(reg.findall(padrao,texto))
print(reg.split(padrao,texto))