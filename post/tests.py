
from user.models import CustomUser
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import PetPost

User = get_user_model()

class PetPostTest(TestCase):
    def setUp(self):
        # Создаем несколько тестовых объектов пользователей
        self.user1 = CustomUser.objects.create(email='user1')
        self.user2 = CustomUser.objects.create(email='user2')

        # Создаем несколько тестовых объектов постов
        self.post1 = PetPost.objects.create(
            owner=self.user1,
            name='Собака Рекс',
            age=2,
            gender='male',
            description='Очень ласковый и дружелюбный',
            category='dogs'
        )
        self.post2 = PetPost.objects.create(
            owner=self.user2,
            name='Кошка Мурка',
            age=1,
            gender='female',
            description='Любит играть с мячиками',
            category='cats'
        )

    def test_petpost_created(self):
        # Тест проверяет, что при создании объекта PetPost создается запись в базе данных
        self.assertEqual(PetPost.objects.count(), 2)

    def test_petpost_owner(self):
        # Тест проверяет, что владелец созданного поста совпадает с создателем поста
        self.assertEqual(self.post1.owner, self.user1)

    def test_petpost_name(self):
        # Тест проверяет, что название созданного поста является уникальным
        with self.assertRaises(Exception):
            PetPost.objects.create(
                owner=self.user1,
                name='Собака Рекс',
                age=1,
                gender='male',
                description='Очень активный и игривый',
                category='dogs'
            )

    def test_petpost_str(self):
        # Тест проверяет, что метод __str__() модели PetPost возвращает корректное значение
        self.assertEqual(str(self.post1), 'Собака Рекс')
