print("!PIZZARIA COMA BASTANE - SEJA BEM VINDO!")
print("     ------ Cardapio - Preços ------")
print("=======================================")
print("       =====Pizzas - Sabores=====")
print("--- 3 Queijos,Bolonhesa, carne c/ Cheadar ---")
print("       =====Pizzas - Tamanhos=====")
print("Pizza - Pequena - R$ 10,90")
print("Pizza - Média - R$ 12,50")
print("Pizza - Grande - R$ 20,00")
print("       -----Refrigerantes-----")
print("--Coca-Cola - R$9,00--")
print("---Guaraná Jesus - R$8,00---")
print("---Mate Couro - R$7,50---")
print("=======================================")
print("=====Faça seu pedido para Pizza:=====")
print("-- 1 - Bolonhesa --")
print("-- 2 - 3 Queijos --")
print("-- 3 - carne c/ Cheadar --")
print("=======================================")

pedidopizza = int(input())

print("---- Qual o Tamanho da Pizza ----")
print("P - Pequena")
print("M - Média")
print("G - Grande")
print("=======================================")

tampizza = input().upper()

print("---- Qual o Refrigerante ----")
print(" 1 - Coca-Cola")
print(" 2 - Guaraná Jesus")
print(" 3 - Mate Couro")
print("=======================================")

pedidorefri = int(input())

print("=======================================")


if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    precototal=10.90 + 9.00 
    pedidos = "Bolonhesa,Pequena,Coca-Cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza == "P") and (pedidorefri == 2):
    precototal=10.90 + 8.00
    pedidos =  "Bolonhesa,Pequena,Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precototal=10.90 + 7.50
    pedidos = "Bolonhesa,Pequena,Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza == "M") and (pedidorefri ==1):
    precototal= 12.50 + 9.00
    pedidos = "Bolonhesa, Média, coca-cola"
    formapag = 1 ,2, 3

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precototal=12.50 + 8.00
    pedidos = "Bolonhesa, Média, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza == "M") and (pedidorefri ==3):
    precototal= 12.50 + 7.50
    pedidos = "Bolonhesa, Média, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza == "G") and (pedidorefri ==1):
    precototal= 20.00 + 9.00
    pedidos = "Bolonhesa, Grande, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza == "G") and (pedidorefri ==2):
    precototal= 20.00 + 8.00
    pedidos = "Bolonhesa, Grande, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==1) and (tampizza =="G") and (pedidorefri ==3):
    precototal= 20.00 + 7.50
    pedidos = "Bolonhesa, Grande, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "P") and (pedidorefri ==1):
    precototal= 10.90 + 9.00
    pedidos = "3 Queijos, Pequena, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "P") and (pedidorefri ==2):
    precototal= 10.90 + 8.00
    pedidos = "3 Queijos, Pequena, Guaramá Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "P") and (pedidorefri ==3):
    precototal= 10,90 + 7.50
    pedidos = "3 Queijos, Pequena, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "M") and (pedidorefri ==1):
    precototal= 12.50 + 9.00
    pedidos = "3 Queijos, Média, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "M") and (pedidorefri ==2):
    precototal= 12.50 + 8.00
    pedidos = "3 Queijos, Média, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "M") and (pedidorefri ==3):
    precototal= 12.50 + 7.50
    pedidos = "3 Queijos, Média, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "G") and (pedidorefri ==1):
    precototal= 20.00 + 9.00
    pedidos = "3 Queijos, Grande, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "G") and (pedidorefri ==2):
    precototal= 20.00 + 8.00
    pedidos = "3 Queijos, Grande, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==2) and (tampizza == "G") and (pedidorefri ==3):
    precototal= 20.00 + 7.50
    pedidos = "3 Queijos, Grande, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "P") and (pedidorefri ==1):
    precototal= 10.90 + 9.00
    pedidos = "Carne c/ Cheadar, Pequena, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "P") and (pedidorefri ==2):
    precototal= 10.90 + 8.00
    pedidos = "Carne c/ Cheadar, Pequena, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "P") and (pedidorefri ==3):
    precototal= 10.90 + 7.50
    pedidos = "Carne c/ Cheadar, Pequena, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "M") and (pedidorefri ==1):
    precototal= 12.50 + 9.00
    pedidos = "Carne c/ Cheadar, Média, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "M") and (pedidorefri ==2):
    precototal= 12.50 + 8.00
    pedidos = "Carne c/ Cheadar, Média, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "M") and (pedidorefri ==3):
    precototal= 12.50 + 7.50
    pedidos = "Carne c/ Cheadar, Média, Mate Couro"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "G") and (pedidorefri ==1):
    precototal= 20.00 + 9.00
    pedidos = "Carne c/ Cheadar, Grande, Coca-cola"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "G") and (pedidorefri ==2):
    precototal= 20.00 + 8.00
    pedidos = "Carne c/ Cheadar, Grande, Guaraná Jesus"
    formapag = 1 ,2, 3

elif (pedidopizza ==3) and (tampizza == "G") and (pedidorefri ==3):
    precototal= 20.00 + 7.50
    pedidos = "Carne c/ Cheadar, Grande, Mate Couro"
    formapag = 1 ,2, 3

    

print(f"pedido: {pedidos}")
print(f"Valor Total do Pedido: R$ {precototal}")


print("=======================================")
print("Forma De Pagamento")
print("1 - Cartão")
print("2 - Dinheiro")
print("3 - Pix")
print("=======================================")

formapag = int(input())

if (formapag == 1, 2, 3):
    print("pagamento Aprovado")

elif (formapag == 1):
    print("Pagamento Aprovado")
    print("=======================================")
    print("Aguarde seu pedido, em breve estará pronto!")
    print("=======================================")

elif (formapag == 2):
    print("Pagamento Aprovado")
    print("=======================================")
    print("Aguarde seu pedido, em breve estará pronto!")
    print("=======================================")

elif (formapag == 3):
    print("Pagamento Aprovado")
    print("=======================================")
    print("Aguarde seu pedido, em breve estará pronto!")
    print("=======================================")
