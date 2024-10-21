# Форматирование строк

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
challenge_result = ''


# Использование символа %
print('В команде Мастера кода: %s%s' % (team1_num, '!'))
print('Итого сегодня в командах участников: %s %s %s%s' % (team1_num, 'и', team2_num, '!'))

# Использование метода format()
print('Команда Волшебники данных решила задач: {}{}'.format(score_2, '!'))
print('Волшебники данных решили задачи за {} {} '.format(team2_time, 'с !'))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.{2}f} секунды на задачу!.')




