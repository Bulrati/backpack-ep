import random

# Список предметов с указанием веса и ценности
items = [
    ("Карта", 9, 150),
    ("Компас", 13, 35),
    ("Вода", 153, 200),
    ("Сэндвич", 50, 160),
    ("Глюкоза", 15, 60),
    ("Кружка", 68, 45),
    ("Банан", 27, 60),
    ("Яблоко", 39, 40),
    ("Сыр", 23, 30),
    ("Пиво", 52, 10),
    ("Крем от загара", 11, 70),
    ("Камера", 32, 30),
    ("Футболка", 24, 15),
    ("Брюки", 48, 10),
    ("Зонтик", 73, 40),
    ("Непромокаемые штаны", 42, 70),
    ("Непромокаемый плащ", 43, 75),
    ("Бумажник", 22, 80),
    ("Солнечные очки", 7, 20),
    ("Полотенце", 18, 12),
    ("Носки", 4, 50),
    ("Книга", 30, 10)
]

# Максимальная вместимость рюкзака
max_capacity = 400

# Количество поколений и размер популяции
num_generations = 100
population_size = 100

def generate_individual():
    # Генерация случайного индивида (битовой строки)
    return [random.randint(0, 1) for _ in range(len(items))]

def fitness(individual):
    # Рассчитываем ценность и вес индивида
    total_value = 0
    total_weight = 0
    for i in range(len(items)):
        if individual[i] == 1:
            total_value += items[i][2]
            total_weight += items[i][1]
    
    # Если вес превышает максимальную вместимость, устанавливаем ценность в 0
    if total_weight > max_capacity:
        total_value = 0
    
    return total_value

def evolve_population(population):
    # Сортировка популяции по фитнес-функции (ценности)
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    
    # Отбор лучших особей (элитизм)
    elite = sorted_population[:int(0.1 * population_size)]
    
    # Генерация новой популяции
    new_population = elite.copy()
    while len(new_population) < population_size:
        # Выбор двух случайных особей из предыдущей популяции
        parent1, parent2 = random.choices(sorted_population, k=2)
        
        # Скрещивание родителей
        child = []
        for i in range(len(items)):
            # Случайное выбор значения гена от одного из родителей
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        
        # Мутация гена
        if random.random() < 0.05:
            mutated_gene = random.randint(0, len(items) - 1)
            child[mutated_gene] = 1 - child[mutated_gene]
        
        new_population.append(child)
    
    return new_population

# Создание начальной популяции
population = [generate_individual() for _ in range(population_size)]

# Основной цикл эволюции
for generation in range(num_generations):
    # Вычисление и вывод лучшего результата текущего поколения
    best_individual = max(population, key=lambda x: fitness(x))
    best_fitness = fitness(best_individual)
    print(f"Generation {generation+1}: Value = {best_fitness}")
    
    # Продвижение популяции к следующему поколению
    population = evolve_population(population)

# Вывод результатов
best_individual = max(population, key=lambda x: fitness(x))
best_fitness = fitness(best_individual)
print("\nSolution")
for i in range(len(items)):
    if best_individual[i] == 1:
        print(f"{items[i][0]} (weight: {items[i][1]}, value: {items[i][2]})")
print(f"Total value: {best_fitness}")
