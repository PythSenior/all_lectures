courses = []

def create_course(category, subcategory, title, description, level, currency, price):
    course = {
        "category": category,
        "subcategory": subcategory,
        "title": title,
        "description": description,
        "level": level,
        "currency": currency,
        "price": price
    }
    courses.append(course)
    print("Курс успешно создан.")
f``
def read_course(index):
    if 0 <= index < len(courses):
        return courses[index]
    else:
        print("Индекс находится вне диапазона.")

def update_course(index, category, subcategory, title, description, level, currency, price):
    if 0 <= index < len(courses):
        course = courses[index]
        course["category"] = category
        course["subcategory"] = subcategory
        course["title"] = title
        course["description"] = description
        course["level"] = level
        course["currency"] = currency
        course["price"] = price
        print("Курс успешно обновлен.")
    else:
        print("Индекс находится вне диапазона.")


def delete_course(index):
    if 0 <= index < len(courses):
        del courses[index]
        print("Курс успешно удален.")
    else:
        print("Индекс находится вне диапазона.")

create_course("Веб-разработка", "Python", "Основы веб-разработки на Python", "Этот курс предоставляет введение в основы веб-разработки на языке Python.", "начальный", "сом", 500)
create_course("Разработка игр", "Java", "Введение в разработку игр на Java", "Изучите основы разработки игр, используя язык программирования Java.", "средний", "сом", 800)

print(courses) 

course = read_course(0)
print(course) 

update_course(1, "Веб-разработка", "JavaScript", "Основы веб-разработки на JavaScript", "Этот курс предоставляет введение в основы веб-разработки на языке JavaScript.", "средний", "сом", 600)
print(courses)  

delete_course(0)
print(courses)  