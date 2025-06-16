import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
# url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    
ru_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


animals = {}

while True:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        category_groups = soup.find_all('div', class_='mw-category-columns')
        for group in category_groups:
            items = group.find_all('li')
            
            for item in items:
                name = item.get_text(strip=True)[0]
                if not name:
                    continue
                
                first_name_letter = name[0].upper()
                
                if first_name_letter in ru_letters:
                    animals[first_name_letter] = animals.get(first_name_letter, 0) + 1
                    
        next_url = soup.find('a', string='Следующая страница')
        if not next_url:
            break
        
        url ='https://ru.wikipedia.org' + next_url['href']
        
    except Exception as e:
        print(f"Ошибка: {e}")
        break

import csv

file_name = 'beasts.csv'

sorted_animals = sorted(
    animals.keys(),
    key=lambda x: ru_letters.index(x)
)

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for letter in sorted_animals:
        writer.writerow([letter, animals[letter]])

print("Данные  сохранены в файл", file_name)
