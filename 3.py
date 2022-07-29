# Создайте программу для игры в ""Крестики-нолики"".

field = list(range(1, 10))

def draw_field(a):
    for i in range(3):
        print("|", a[0+ i*3], "|", a[1+ i*3], "|", a[2+ i*3], "|")


def get_input(player_choise):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_choise+"? ")
      if player_answer.isdigit:
            player_answer = int(player_answer)
      else:
        print("Вы ввели не число")
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_choise
            valid = True
         else:
            print("Kлетка занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(field):
   win_mean = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_mean:
       if field[i[0]] == field[i[1]] == field[i[2]]:
          return field[i[0]]
   return False

def main(field):
    count = 0
    win = False
    while not win:
        draw_field(field)
        if count % 2 == 0:
           get_input("X")
        else:
           get_input("O")
        count += 1
        if count > 4:
           с = check_win(field)
           if с:
              print(с, "выиграл!")
              win = True
              break
        if count == 9:
            print("Ничья!")
            break
    draw_field(field)
main(field)

input("Нажмите Enter для выхода!")
