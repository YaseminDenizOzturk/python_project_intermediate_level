from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Fruit Name " , ["Strawberry" , "Banana" , "Grape"])
table.add_column("Vitamin " , ["C" , "A" , "A" ])
table.align = "l"
# bu şekilde yaparsam sola hizalı bir tablom olur.
#bu özelliği bu şekilde değiştirebilirim.
print(table)
