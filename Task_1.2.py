import argparse

parser = argparse.ArgumentParser(description='Расчет зарплаты сотрудника')
parser.add_argument('worked', type=float, help='Количество отработанных сотрудником часов')
parser.add_argument('rate', type=float, help='Ставка сотрудника')
parser.add_argument('prize', type=float, help='Премия сотрудника')
args = parser.parse_args()
print(f'Заработная плата сотрудника: {args.worked * args.rate + args.prize}')
