import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--worked-out',
        type=float,
        required=True,
        help='Количество часов отработанных сотрудником',
        metavar='<HOURS_WORKED>')

    parser.add_argument(
        '-r', '--hourly-rate',
        type=float,
        required=True,
        help='Часовая ставка сотрудника по тарифной сетке',
        metavar='<HOURLY_RATE>')

    parser.add_argument(
        '-b', '--bounty',
        type=float,
        help='Премия',
        required=False,
        default=0,
        metavar='<BOUNTY>')

    args = parser.parse_args()

    salary = args.worked_out * args.hourly_rate + args.bounty

    print(f'Зарплата сотрудника составляет {round(salary, 2)} руб.')
