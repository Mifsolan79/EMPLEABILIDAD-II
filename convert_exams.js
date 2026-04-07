const fs = require('fs');
const path = require('path');

function convertTxtToJson(inputPath, outputPath, themeNumber, titleOverride = null) {
    if (!fs.existsSync(inputPath)) {
        console.error(`Error: El archivo ${inputPath} no existe.`);
        return false;
    }

    const content = fs.readFileSync(inputPath, 'utf8');

    let title = titleOverride;
    if (!title) {
        const titleMatch = content.match(/^(.*?)\r?\n=+/);
        title = titleMatch ? titleMatch[1].trim() : `TEMA ${themeNumber}`;
    }

    const questionsRaw = content.split(/-{10,}/);
    const items = [];

    for (const rawBlock of questionsRaw) {
        const qRaw = rawBlock.trim();
        if (!qRaw) continue;

        const questionMatch =
            qRaw.match(/Pregunta\s+\d+:\s*(.*?)(?=\r?\n\s*[A-D]\))/s) ||
            qRaw.match(/^(.*?)(?=\r?\n\s*[A-D]\))/s);

        if (!questionMatch) continue;

        const questionText = questionMatch[1].trim();
        const options = [];

        for (const letter of ['A', 'B', 'C', 'D']) {
            const optionMatch = qRaw.match(
                new RegExp(`${letter}\\)\\s*(.*?)(?=\\r?\\n\\s*[A-D]\\)|$|\\r?\\n\\s*Respuesta)`, 's')
            );
            if (optionMatch) {
                options.push(optionMatch[1].trim());
            }
        }

        const answerMatch = qRaw.match(/Respuesta Correcta:\s*([A-D])/);
        if (!answerMatch || options.length !== 4) continue;

        const correctIndex = answerMatch[1].charCodeAt(0) - 'A'.charCodeAt(0);
        const explanationMatch = qRaw.match(/Explicación:\s*(.*?)$/s);
        const explanation = explanationMatch ? explanationMatch[1].trim() : '';

        items.push({
            question: questionText,
            options,
            correctAnswer: correctIndex,
            explanation
        });
    }

    const jsonData = { title, items };
    fs.writeFileSync(outputPath, JSON.stringify(jsonData, null, 4), 'utf8');
    console.log(`Convertido con éxito: ${outputPath} (${items.length} preguntas)`);
    return true;
}

const temas = [9, 10, 11, 12, 13, 14, 15].map((num) => ({
    num,
    input: path.join(__dirname, '..', `itinerario_personal_para_la_empleabilidad_ii__tema_${num}_examen.txt`),
    title: `ITINERARIO PERSONAL PARA LA EMPLEABILIDAD II - TEMA ${num}`
}));

const dataDir = path.join(__dirname, 'data');
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let generated = 0;
for (const tema of temas) {
    const outputPath = path.join(dataDir, `tema_${tema.num}.json`);
    if (convertTxtToJson(tema.input, outputPath, tema.num, tema.title)) {
        generated += 1;
    }
}

if (generated !== temas.length) {
    process.exitCode = 1;
}
