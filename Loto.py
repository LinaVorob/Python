import random


class LotoGame:
    def __init__(self, gamer_1, gamer_2):
        self.gamer_1 = gamer_1
        self.gamer_2 = gamer_2

    def generate_numbers(self):
        numbers = [x for x in range(1, 91)]
        random.shuffle(numbers)
        for i in numbers:
            yield i

    def game_start(self):
        g_num = LotoGame.generate_numbers(self)
        counter = 0
        for i in g_num:
            counter += 1
            print(f'Новый бочонок: {i} (осталось {90 - counter})')
            print(self.gamer_1)
            print(self.gamer_2)
            user_answer = input("Зачеркнуть цифру? (y/n)")

            interval_val_1 = self.control_cards(self.gamer_1, i)
            self.control_cards(self.gamer_2, i)

            if user_answer == 'y':
                if interval_val_1 is None:
                    print(f'Ошибка! Победил(а) {self.gamer_2.gamer}')
                    break
            elif user_answer == 'n':
                if interval_val_1 is not None:
                    print(f'Ошибка! Победил(а) {self.gamer_2.gamer}')
                    break
            else:
                print('Ошибка! Неизвестный символ!')
                break

            control_card = list(map(lambda x: x.replace(' ', '').replace('-', '').isnumeric(), self.gamer_1._card))
            control_card_2 = list(map(lambda x: x.replace(' ', '').replace('-', '').isnumeric(), self.gamer_2._card))
            if True not in control_card or True not in control_card_2:
                print(f'Победил(а): {self.gamer_1.gamer if True not in control_card else self.gamer_2.gamer}')
                break

    # Проверка наличия числа в карточке
    def control_cards(self, gamer, i):
        find_number = [next_number for next_number in gamer._card if
                       (' ' if len(str(i)) == 1 else '') + str(i) + (
                           ' ' if len(str(i)) == 1 else '') in next_number]

        if find_number:
            index = gamer._card.index(find_number[0])
            find_number = find_number[0].replace(
                (' ' if len(str(i)) == 1 else '') + str(i) + (' ' if len(str(i)) == 1 else ''), '- ')
            gamer._card[index] = find_number
            return gamer._card
        else:
            return None


class LotoCard:
    def __init__(self, gamer):
        self.gamer = gamer
        self.len_name = int((27 - len(self.gamer)) / 2)
        card = random.sample(range(1, 91), 15)
        self._card = [card[x:x + 5] for x in range(0, 15, 5)]
        self._card = list(map(sorted, self._card))
        for string in range(len(self._card)):
            for _ in range(4):
                self._card[string].insert(random.randrange(0, 8), '  ')
            self._card[string] = list(map(str, self._card[string]))
            self._card[string] = ' '.join([x.rjust(2) for x in self._card[string]])

    def __str__(self):
        return "-" * self.len_name + self.gamer + "-" * (27 - self.len_name - len(self.gamer)) + '\n' + '\n'.join(
            self._card) + '\n' + '-' * 27


gamer_name = LotoCard('Lina Vorobeva')
computer = LotoCard('Computer')
game = LotoGame(gamer_name, computer)
game.game_start()
