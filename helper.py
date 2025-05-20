from faker import Faker
from datetime import datetime, timedelta
faker = Faker('ru_RU')

def generate_data_comment():
    today = datetime.today()  # получаем сегодняшнюю дату
    future_day = today + timedelta(days=5)  # добавляем 5 дней вперед
    data = future_day.strftime('%d.%m.%Y')  # форматируем дату в формате dd.mm.yyyy
    commit = faker.sentence()
    return data, commit
