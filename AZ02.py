import pandas as pd
import random

names = ["Иван", "Мария", "Алексей", "Анна", "Дмитрий", "Екатерина", "Сергей", "Ольга", "Михаил", "Елена"]
subjects = ["Математика", "Физика", "Информатика", "История", "Литература"]

possible_grades = [2, 3, 4, 5]
chances = [1, 2, 5, 3]

data = {"Name": names}
for subject in subjects:
    data[subject] = random.choices(possible_grades, weights=chances, k=10)

df = pd.DataFrame(data)

subjects_df = df[subjects]

print("--- Студенты и оценки ---")
print(df.to_string(index=False))

mean_grades = subjects_df.mean()
print("\n--- Средняя оценка по каждому предмету ---")
print(mean_grades)

median_grades = subjects_df.median()
print("\n--- Медианная оценка по каждому предмету ---")
print(median_grades)

std_grades = subjects_df.std()
print("\n--- Стандартное отклонение по каждому предмету ---")
print(std_grades)

Q1_math = df['Математика'].quantile(0.25)
print("\n--- Q1 по математике ---")
print(Q1_math)

Q3_math = df['Математика'].quantile(0.75)
print("\n--- Q3 по математике ---")
print(Q3_math)

IQR_math = Q3_math - Q1_math
print("\n--- IQR по математике ---")
print(IQR_math)