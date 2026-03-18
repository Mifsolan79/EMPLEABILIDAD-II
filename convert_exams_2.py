import json
import re
import os

def convert_txt_to_json(input_path, output_path, theme_number, title_override=None):
    if not os.path.exists(input_path):
        print(f"Error: El archivo {input_path} no existe.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer el título del archivo si no se proporciona uno
    if title_override:
        title = title_override
    else:
        title_match = re.search(r'^(.*?)\n=+', content)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title = f"TEMA {theme_number}"

    # Dividir por preguntas usando el separador de guiones o el patrón de Pregunta X
    questions_raw = re.split(r'-{10,}', content)
    
    items = []
    for q_raw in questions_raw:
        q_raw = q_raw.strip()
        if not q_raw:
            continue
            
        # Buscar pregunta
        question_match = re.search(r'Pregunta\s+\d+:\s*(.*?)(?=\n\s*[A-D]\))', q_raw, re.DOTALL)
        if not question_match:
            # Reintentar si no hay prefijo Pregunta X
            question_match = re.search(r'^(.*?)(?=\n\s*[A-D]\))', q_raw, re.DOTALL)
            
        if not question_match:
            continue
            
        question_text = question_match.group(1).strip()
        
        # Buscar opciones
        options = []
        for letter in ['A', 'B', 'C', 'D']:
            option_match = re.search(rf'{letter}\)\s*(.*?)(?=\n\s*[A-D]\)|$|\n\s*Respuesta)', q_raw, re.DOTALL)
            if option_match:
                options.append(option_match.group(1).strip())
        
        # Buscar respuesta correcta
        answer_match = re.search(r'Respuesta Correcta:\s*([A-D])', q_raw)
        if not answer_match:
            continue
            
        correct_letter = answer_match.group(1)
        correct_index = ord(correct_letter) - ord('A')
        
        # Buscar explicación
        explanation_match = re.search(r'Explicación:\s*(.*?)$', q_raw, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        items.append({
            "question": question_text,
            "options": options,
            "correctAnswer": correct_index,
            "explanation": explanation
        })

    json_data = {
        "title": title,
        "items": items
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    
    print(f"Convertido con éxito: {output_path} ({len(items)} preguntas)")

# Temas a convertir para Empleabilidad II
temas = [
    {
        "num": 9,
        "input": r"f:\16. EMPLEABILIDAD II\itinerario_personal_para_la_empleabilidad_ii__tema_9_examen.txt",
        "title": "ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA 9"
    },
    {
        "num": 10,
        "input": r"f:\16. EMPLEABILIDAD II\itinerario_personal_para_la_empleabilidad_ii__tema_10_examen.txt",
        "title": "ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA 10"
    },
    {
        "num": 11,
        "input": r"f:\16. EMPLEABILIDAD II\itinerario_personal_para_la_empleabilidad_ii__tema_11_examen.txt",
        "title": "ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA 11"
    },
    {
        "num": 12,
        "input": r"f:\16. EMPLEABILIDAD II\itinerario_personal_para_la_empleabilidad_ii__tema_12_examen.txt",
        "title": "ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA 12"
    }
]

data_dir = r"f:\16. EMPLEABILIDAD II\EXAMEN GITHUB\data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

for tema in temas:
    output_filename = f"tema_{tema['num']}.json"
    output_path = os.path.join(data_dir, output_filename)
    convert_txt_to_json(tema['input'], output_path, tema['num'], title_override=tema['title'])
