#Задание "Свой YouTube"
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User

    def log_in(self, nickname, password):
        for i in range(0, len(self.users)):
            if self.users[i].nickname == nickname and self.users[i].password == hash(password):
                self.current_user = self.users[i]
        return

    def log_out(self):
        self.current_user = None
        return

    def register(self, nickname, password, age):
        ur.log_in(nickname, password)
        if self.current_user in self.users:
            ur.log_out()
        else:
            list_users_nickname = []
            for i in range(0, len(self.users)):
                list_users_nickname.append(self.users[i].nickname)
            if nickname in list_users_nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                self.current_user = User(nickname, password, age)
                self.users.append(self.current_user)
                self.current_user = self.current_user.nickname
        return

    def add(self, *args):
        new_list_video = []
        for obj in args:
            new_video = Video(obj.title, obj.duration, obj.time_now, obj.adult_mode)
            if len(self.videos) == 0:
                self.videos.append(new_video)
                new_list_video.append(new_video.title)
            for i in range(0, len(self.videos)):
                if obj.title in new_list_video:
                    continue
                else:
                    self.videos.append(new_video)
                    new_list_video.append(new_video.title)
        return

    def get_videos(self, new_words):
        list_videos = []
        new_list_videos = []
        for i in range(0, len(self.videos)):
            list_videos.append(self.videos[i].title)
        for i in range(0, len(list_videos)):
            videos_word = list(list_videos[i].split())
            for j in range(0, len(videos_word)):
                if new_words.lower() in videos_word[j].lower():
                    new_list_videos.append(list_videos[i])
                else:
                    continue
        return new_list_videos

    def watch_video(self, title):
        list_videos = []
        list_users = []
        dict_users = {}
        for i in range(0, len(self.users)):
            list_users.append(self.users[i].nickname)
            if ur.current_user in list_users:
                dict_users[ur.current_user] = self.users[i].age
        for i in range(0, len(self.videos)):
            list_videos.append(self.videos[i].title)
            if title in list_videos:
                current_video = self.videos[i]
                if len(dict_users) > 0:
                    if current_video.adult_mode:
                        if dict_users[ur.current_user] > 18:
                            for j in range(0, current_video.duration):
                                current_video.time_now += 1
                                print(current_video.time_now, sep=" ", end=" ")
                                time.sleep(1)
                            print("Конец видео")
                            time.sleep(2)
                            current_video.time_now = 0
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска##
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Лучший язык программирования 2024 года')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
