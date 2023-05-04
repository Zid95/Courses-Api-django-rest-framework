import os , django
os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'
django.setup()

from faker import Faker
import random
from courses.models import Category,Instructor,Courses


def seed_category(n):
    fake = Faker()
    for _  in range(n):
        name = fake.name()
        Category.objects.create(name = name)


def seed_instructor(n):
    fake = Faker()
    for _  in range(n):
        image = "instructor/default.jpg"
        name = fake.name()
        title = fake.text(max_nb_chars = 200)
        bio = fake.text(max_nb_chars = 1000)
        Instructor.objects.create(name = name,
                                 image=image,
                                  title=title,
                                   bio=bio )

def seed_courses(n):
    fake = Faker()
    for _ in range(n):
        name =fake.name()
        
        image = "courses/default.jpg"
        instructor = Instructor.objects.get(id=random.randint(1,30))
        price = round(random.uniform(20.99,99.99),2)
        subtitle = fake.text(max_nb_chars = 200)
        description = fake.text(max_nb_chars = 1000)
        category = Category.objects.get(id=random.randint(1,10))

        Courses.objects.create(
            name = name,
            image = image,
            price = price,
            category = category,
            subtitle = subtitle,
            description = description,
            instructor = instructor

        )


seed_category(10)
seed_instructor(30)
seed_courses(1000)