def ehLetra(c):
	return True if (ord(c) >= 65 and ord(c)<=90) or (ord(c) >= 97 and ord(c)<=122) else False
def ehMaiuscula(c):
	return True if (ord(c) >= 65 and ord(c)<=90) else False
def converteMaiuscula(s,i=0,ns=""):
	if i<len(s):
		if ehLetra(s[i]):
			if ehMaiuscula(s[i]) or s[i] == " ":
				return converteMaiuscula(s,i+1,ns+s[i])
			else:
				return converteMaiuscula(s,i+1,ns+chr(ord(s[i])-32))
		else:
			return converteMaiuscula(s,i+1,ns+s[i])
	else:
		return ns

print(converteMaiuscula("teste 123"))