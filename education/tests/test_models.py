from django.test import TestCase
from education.models import *


class ModelsTest(TestCase):
    def setUp(self):
        Religion.objects.create(name='Буддизм')
        Topic.objects.create(title='История возникновения Буддизма', religion_id=1)
        Subtopic.objects.create(title='Жизнь Будды', topic_id=1, content='Согласно традиции, исторический Будда Сиддхартха Гаутама родился в роде Шакья касты кшатриев в стране Магадха (546—324 до н. э.), в районе Лумбини на юге современного Непала. Его также называли Шакьямуни — мудрец, принадлежащий к клану Шакья. После жизни в роскоши во дворце своего отца, короля Капилавасту (царство которого потом вошло в государство Магадха), Сиддхарта случайно столкнулся с жестокой реальностью и сделал вывод, что реальная жизнь связана со страданиями и горем. Он отказался от жизни во дворце и стал вести аскетическую жизнь вместе с лесными отшельниками, в том числе выполняя практики мучения и умерщвления тела.[2] Позднее он пришёл к выводу, что крайние формы аскетизма не ведут к освобождению от страданий, связанных с рождением и смертью, и следует находить промежуточный путь между стремлением к чувственным удовольствиям и стремлением к самоумерщвлению.[3]Во время медитации под деревом Бодхи он принял решение во что бы то ни стало найти Истину, и в возрасте 35 лет достиг Просветления. После этого он стал называться Будда Гаутама, или просто Будда, что означает «пробуждённый».Остальные 45 лет жизни он путешествовал по Центральной Индии в долине Ганга, обучая своих последователей и учеников.В дальнейшем последователи Будды в течение последующих 400 лет сформировали много разных учений — школы раннего буддизма (Никая), из которых сохранилось учение Тхеравада и многочисленные ветви Махаяны.')

    def test_religion_name(self):
        religion_name = Religion.objects.get(id=1).name
        self.assertEquals(religion_name, 'Буддизм')

    def test_topic_title(self):
        topic_title = Topic.objects.get(id=1).title
        self.assertEquals(topic_title, 'История возникновения Буддизма')

    def test_topic_relates_to_right_religion(self):
         related_religion = Topic.objects.get(id=1).religion.name
         self.assertEquals(related_religion, 'Буддизм')

    def test_subtopic_title(self):
        subtopic_title = Subtopic.objects.get(id=1).title
        self.assertEquals(subtopic_title, 'Жизнь Будды')

    def test_subtopic_related_to_right_topic(self):
        related_topic = Subtopic.objects.get(id=1).topic.title
        self.assertEquals(related_topic, 'История возникновения Буддизма')

    #test_of_content





