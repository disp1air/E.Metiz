                                      message = "Hello Python world!"  
                                      print(message)  

                                      message = "Hello Python Crash Course world!"  
                                      print(message)  

При запуске данного кода на экране должны появляться две строки:  

                                      Hello Python world!
                                      Hello Python Crash Course world!

Вы можете в любой момент изменить значение переменной в своей программе; Python всегда отслеживает его текущее состояние.  

Имена переменных могут состоять только из букв, цифр и символов подчеркивания. Они могут начинаться с буквы или символа подчеркивания, но не с цифры. Например, переменной можно присвоить имя message_1, но не 1_message.  

**Строки**  
Метод title() - преобразует первый символ каждого слова в строке к верхнему регистру, тогда как все остальные символы выводятся в нижнем регистре.  

                                      name = "ada lovelace"
                                      print(name.title())

                                      Ada Lovelace

                                      name = "Ada Lovelace"
                                      print(name.upper())
                                      print(name.lower())

                                      ADA LOVELACE
                                      ada lovelace

Пропуски можно удалить у левого края строки при помощи метода lstrip(), а метод strip() удаляет пропуски с обоих концов.  
