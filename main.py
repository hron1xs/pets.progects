import play #імпорт бібліотеки

play.set_backdrop("white")#встановлення кольору фона



@play.when_program_starts #декоратор
#Декоратор - це функція, яка дозволяє обернути іншу функцію для розширення її функціональності без безпосередньої зміни коду

def start():#функція для старту програми

    global player,speach,text2
    text1 = play.new_text(words='п - підключитися,х-ховати,у-убивати',x=0,y=250,font_size=40,font = "Arial")#команда для створення тексту
    text2 = play.new_text(words='ї - їсти ,с-спати,о-здивуватися',x=0,y=225,font_size=40,font = "Arial")#команда для створення тексту
    player = play.new_image(image='norm_face.png',x=0,y=0,size=150)#командва для додавання зображення
    speach = play.new_text(words='Привіт, підлючися до інтернету((',x= 0,y = -250 )


@play.repeat_forever #декоратор2

async def do():#ігровий цикл
    if play.key_is_pressed('п') or play.key_is_pressed('П'):
        player.image = 'internet face.jpg'
        speach.words = 'в тебе є 5 секунд'
        await play.timer(5)
        player.image = 'hochy eat.jpg'
        player.size = 100
        speach.words = 'Молодець,тепер накорми мене'
    elif play.key_is_pressed('ї') or play.key_is_pressed('Ї'):
        player.image = 'afiggenuy face.jpg'
        speach.words = 'Ммм,зараз спробуєм'
        await play.timer(5)
        player.image = 'angry_face.png'
        speach.words = 'Це не їстівне,що ти мені підсунув?Хочу тепер убивати'
    elif play.key_is_pressed('у') or play.key_is_pressed('У'):
        player.image = 'chacok mortis.jpg'
        speach.words = 'Ти не дозволяєш мені убивати?'
        await play.timer(5)
        player.image = 'afiggenuy face.jpg'
        speach.words = 'тоді давай хоча б тіло сховаємо'
    elif play.key_is_pressed('х') or play.key_is_pressed('Х'):
        player.image = 'norm_face.png'
        speach.words = 'Ох,сьогодні був тяжкий день'
        await play.timer(5)
        player.image = 'armyan face.jpg'
        speach.words = 'Давай підемо спати '
    elif play.key_is_pressed('с') or play.key_is_pressed('С'):
        player.image = 'im fine.jpg'
        





        




play.start_program()#запуск програми