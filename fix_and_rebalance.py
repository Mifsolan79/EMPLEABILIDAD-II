import json
import random

def fix_and_rebalance(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    items = data['items']
    
    # Target distribution for 30 questions: 7, 7, 8, 8 (or 8, 7, 8, 7 etc.)
    # We will randomly assign target answers that meet this criteria
    targets = [0]*8 + [1]*8 + [2]*7 + [3]*7
    random.shuffle(targets)
    
    for idx, item in enumerate(items):
        target_correct = targets[idx]
        current_correct = item['correctAnswer']
        
        if current_correct != target_correct:
            # Swap the options
            options = item['options']
            # Swap target position and current correct position
            options[target_correct], options[current_correct] = options[current_correct], options[target_correct]
            item['correctAnswer'] = target_correct
            item['options'] = options
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"File {filepath} processed. Answer distribution: { {i: targets.count(i) for i in range(4)} }")
    return items

def check_forbidden_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    forbidden = ['caso práctico', 'fidel', 'mario', 'virginia', 'juan', 'vanesa', 'resumen', 'introducción', 'bibliografía']
    
    for idx, item in enumerate(data['items']):
        text = (item['question'] + " " + item['explanation']).lower()
        for word in forbidden:
            if word in text:
                print(f"WARNING {filepath} Q{idx+1}: Found forbidden word '{word}' -> {item['question']}")

files = [
    'f:/16. EMPLEABILIDAD II/EXAMEN GITHUB/data/tema_1.json',
    'f:/16. EMPLEABILIDAD II/EXAMEN GITHUB/data/tema_2.json',
    'f:/16. EMPLEABILIDAD II/EXAMEN GITHUB/data/tema_3.json',
    'f:/16. EMPLEABILIDAD II/EXAMEN GITHUB/data/tema_4.json'
]

for f in files:
    check_forbidden_words(f)
    fix_and_rebalance(f)

