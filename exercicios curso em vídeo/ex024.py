print("esse programa informa se você nasceu em uma cidade que começa com santo")
city = input("digite o nome da cidade que você nasceu:").strip()
'''zap = city.lower().find('santo')
if zap == -1:
    print("False")
else:
    print("True")'''
print(city[:5].lower() == "santo")
#print("santo" in city.lower())