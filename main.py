import play #імпорт бібліотеки

play.set_backdrop("violet")



@play.when_program_starts #декоратор 
#Декоратор - це функція, яка дозволяє обернути іншу функцію для розширення її функціональності без безпосередньої зміни коду

def start():#функція для старту програми
    pass


@play.repeat_forever #декоратор2

def do():#ігровий цикл
    play.new_text(words='к-копати,х-ховати,у-убивати',x=0,y=250,font_size=40,font = "Calibry")
    play.new_text(words='з-злитися,с-спати,о-здивуватися',x=0,y=225,font_size=40,font = "Calibry")
    play.new_image(image='norm_face.png',x=0,y=0,size=100)
play.start_program()#запуск програми