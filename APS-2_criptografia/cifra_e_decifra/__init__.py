from time import sleep

lista1 = ['a','?','c','(','T','P','g',':','i',')','k','/','m','+','o','}','q','!','s','~','u','$','w','¢','y','£','ç',',',
          ' ','é','á','à','ã','ê','õ','ô','ó','í','.','!','b','è','A','B','C','D','E','Ç','F','G','H','I','J','K','L','M','-','N',
          'O','_','Q','R','S','e','U','V','W','X','Y','Z','l','|',';','.','h',',','r','@','%','&','§','t','º','Á','À','ú',
          'É','Ã','Ô','Ó','Ê','È','"','d','j','`','f','=','n','x','<','>',']','[','p','{','ª','z','¬','*','¨','v','°',
          'Ú','ù','Ù','ò','Ò','Í','ì','Ì','ý','Ý','Õ','Â','â','î','Î','ñ','Ñ','^','´']
# lista1, para caracteres gerais, com exceção de números.

lista2 = ['91','298','1357','5302','31','104','306','17','8017','7110','165','72','467','15','6094','77','901','1298','52',
          '597','43','794','8001','11','5771','119','781','4897','923','73','113','3333','9001','999','88','78906','90347','12378','56789','34098',
          '89742','23778','77790','55570','90999','43599','70865','12345','67890','76899','12303','99999','88888','77777','33333','11111','00000','00999',
          '15243','22222','89120','66666','21987','71721','81828','39355','63738','45678','45017','90023','00789','55785','90034','45009','44409','17003',
          '19009','95001','09677','33003','70707','03030','65001','678954','777777','333333','456902','999083','675877','234789','111011','569999',
          '666017','098345','440443','121289','789964','998356','070070','242930','45908','999999','77817','817','98710','93222','713','090965','370123',
          '8714','903478','444091','9207','56555','48990','99073','689594','15789','819','9731','09712']
# lista2, só possui números.
# porém, ambas são usadas na cifragem e na decifragem, devido a chave randômica.

lista3 = lista1 + lista2
# lista3, concatena as duas listas, para poder ter uma maior variedade de carácteres, na hora da cifragem.

# bloco da cifra.
def cifra(mensagem, lista3):
    from random import randrange
    global lista4
    global chave # Torna a chave pública, para funcionar tanto na cifragem, quanto na decifragem.
    chave = randrange(200, 800) # Chave Randômica.
     # usada como chave, para avançar os caracteres na cifragem.
     # E também, para voltar a mesma quantidade de caracteres, na hora de decifrar.
    lista4 = []
    for c in mensagem:
        c_index = lista3.index(c)
        t = lista3[(c_index + chave) % len(lista3)]
        lista4.append(t)
    return ''.join(lista4)
# O for que pega cada um dos caracteres da mensagem.
# depois, o .index(c), procura cada carácter da lista3 e armazena no c_index
# em seguida, é listada na lista3, os caracteres da mensagem.
# é usada a chave para avançar, de acordo com o tamanho da lista3.
# após isso, todo esse processo, é adicionado na lista4, através do .append
# Por fim, a lista4 é retornada e exibe a mensagem cifrada.


# bloco da decifra
def decifra(mensagem, lista3):
    lista5 = []
    for c in lista4:
        c_index = lista3.index(c)
        s = lista3[(c_index - chave) % len(lista3)]
        lista5.append(s)
    return ''.join(lista5)

# O for que pega, os caracteres da lista4, ou seja, cada carácter da mensagem cifrada.
# é usada a chave para voltar, os caracteres de volta a mensagem original.
# depois, a mensagem é adicionada na lista5.
# Por fim, a lista5 é retornada e exibe a mensagem decifrada.
