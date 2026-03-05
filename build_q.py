import json
import os

def build_tema_8():
    data_dir = 'data'
    file_part1 = os.path.join(data_dir, 'tema_8_q1_to_q15.json')
    file_part2 = os.path.join(data_dir, 'tema_8_q16_to_q30.json')
    output_file = os.path.join(data_dir, 'tema_8.json')

    print(f"Leyendo {file_part1}...")
    with open(file_part1, 'r', encoding='utf-8') as f:
        q1_15 = json.load(f)

    print(f"Leyendo {file_part2}...")
    with open(file_part2, 'r', encoding='utf-8') as f:
        q16_30 = json.load(f)

    final_questions = q1_15 + q16_30

    output_data = {
        "title": "ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA 8",
        "items": final_questions
    }

    print(f"Generando {output_file} con {len(final_questions)} preguntas...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print("¡Exitoso! tema_8.json ha sido regenerado con las preguntas oficiales.")

if __name__ == "__main__":
    build_tema_8()
