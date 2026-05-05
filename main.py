name = input("Введите ваше имя: ")
language = input("Какой язык программирования вы учите? ")
place = input("Где бы вы хотели жить и работать? ")

print("------------------------------")
print("   ВИЗИТКА РАЗРАБОТЧИКА")
print(f"Имя: {name}")
print(f"Специализация: {language} Developer")
print(f"Локация мечты: {place}")
print("------------------------------")

if language == "Python" or language == "JavaScript" or language == "TypeScript":
    print("Отличный выбор для начинающих разработчиков!")
elif language == "Java" or language == "C#" or language == "C++":
    print("Вы выбрали мощный язык для разработки крупных проектов!")
else:    
    print("Интересный выбор!")