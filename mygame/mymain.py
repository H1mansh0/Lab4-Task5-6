import mygame.mygame as mygame

ivasuka = mygame.Room("Вулиця Івасюка")
ivasuka.set_description("Найперша ваша точка. Довга вулиця, яка є початком ваших пригод")

nezaleznosti = mygame.Room("Вулиця Незалежності")
nezaleznosti.set_description("Веде до центру, найдовша вулиця у місті")

sto_metrivka = mygame.Room("Стометрівка")
sto_metrivka.set_description("Довжина Стометрівки не 100 метрів")

town_hall = mygame.Final_room("Міська ратуша")
town_hall.set_description("Центр міста з великою кількістю розваг і пригод")

pozitron = mygame.Room('Позитрон')
pozitron.set_description('Район, де є пожежна станція. Цікаво, що тут можна знайти')

pozitron.link_room(ivasuka, "наступна")
ivasuka.link_room(pozitron, "попередня")
ivasuka.link_room(nezaleznosti, "наступна")
nezaleznosti.link_room(ivasuka, "попередня")
nezaleznosti.link_room(sto_metrivka, "наступна")
sto_metrivka.link_room(nezaleznosti, "попередня")
sto_metrivka.link_room(town_hall, "наступна")
town_hall.link_room(sto_metrivka, "попередня")


vova = mygame.Enemy("Вова", "Хлопець з не дуже привітнім виглядом")
vova.set_conversation("Опа, Стояти! Не буде подзвонити?")
vova.set_weakness("пиво")
nezaleznosti.set_character(vova)

dai_kopiiky = mygame.Friend("Дід Дайкопійку", "Місцева легенда. Ніколи не приймає паперові гроші")
dai_kopiiky.set_conversation("Дай копійку! Дай копійку!")
dai_kopiiky.set_treatment("копійка")
sto_metrivka.set_character(dai_kopiiky)

final_boss = mygame.Big_enemy("Пан Марцинків", "Міський голова, заклва все місто бруківкою")
final_boss.set_conversation("Покиньте МІСТО!")
final_boss.set_weakness("бруківка")
town_hall.set_character(final_boss)

coin = mygame.Item("копійка")
coin.set_description("Поцарапана копійка")
ivasuka.set_item(coin)

magic_drink = mygame.Item("пиво")
magic_drink.set_description('Просте пиво. Цікаво, навіщо воно вам?')
sto_metrivka.set_item(magic_drink)

brook = mygame.Item("бруківка")
brook.set_description("Звичайна бруківка")

hint = mygame.Hint('підказка')
hint.set_description("Дивний папірець від діда дай копійку")
dai_kopiiky.set_item(hint)

current_room = ivasuka
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if current_room == town_hall:
        while True:
            command = input("> ")
            if command == 'битись': break
            current_room.move(command)

    if command in ["наступна", "попередня"]:
        current_room = current_room.move(command)
    elif command == "говорити":
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant == dai_kopiiky:
                print("Що ви дасте йому?")
                give_item = input("> ")
                if (give_item in backpack) and (give_item == 'копійка'):
                    print(f'Ви отримали + {hint} + і поклали це у рюкзак')
                    backpack.append(hint)
                else:
                    print("Дайкопійку усміхнувся і розвернувся")
    elif command == "битись":
        if inhabitant is not None:
            if inhabitant == final_boss:
                print("Що ви використаєте у битві")
                fight_with = input()
                if fight_with in backpack: 
                    if inhabitant.fight(fight_with) == True:
                        print('AAAAA. Добре, якщо ти відгадаєш цю загадку - ти переміг!')
                        inhabitant.final_heet()
                        if hint in backpack:
                            print("Використати підказку?")
                            response = input('> ')
                            if ['т', 'а', 'к'] in list(response.lower()):
                                hint.use_hint() 
                        guess = input("> ")
                        if ['м','о','к','р','и','й'] in list(guess):
                            print("Ви перемогли!")
                            dead = True
                        else:
                            print("Неправильна відповідь! Ти програв")
                            dead = True
                    else:
                        print("Навіщо ви сюди прийшли без необхідних предметів?")
                        dead = True
                else:
                    print("У вас немає такого предмету " + fight_with)
                    print("Марцинків кинув у вас бруківку. Ви програли!")
                    dead = True
            else:
                print("Що ви використаєте у битві")
                fight_with = input()
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        print("Чудо! Вас не вбили. Продовжуйте йти далі")
                        print("Ви забрали " + brook.get_name() + "і поклали це у рюкзак")
                        backpack.append(brook.get_name())
                        current_room.character = None
                    else:
                        print("Ви програли...")
                        print("Це кінець.")
                        dead = True
                else:
                    print("У вас немає такого предмету " + fight_with)
        else:
            print("Заспокойтесь сонце вже низько. Тут немає з ким битися")
    elif command == "взяти":
        if item is not None:
            print("Ви забрали " + item.get_name() + "і поклали це у рюкзак")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Немає, що брати! Галяк!")
    else:
        print("Ви агресивно стоїте на місці незнаючи, що робити")