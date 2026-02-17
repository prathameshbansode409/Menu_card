menu_card=""
for i in range(1,5):
    inp1=input(f"item{i} : ")
    inp2=input(f"price{i} : ")
    dash=20-len(inp1)-len(inp2)
    menu_card += (inp1+"-"*dash + inp2)+"\n"

print(menu_card)