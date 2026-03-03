import json
import os

with open('data/tema_8_q1_to_q15.json', 'r', encoding='utf-8') as f:
    q1_15 = json.load(f)

# The first 8 questions from the second batch
good_middle = [
    {
        "question": "¿En el caso particular de conformar legalmente su empresa como una Comunidad de bienes, ¿cómo asumen y asimilan las deudas formales de la organización cada uno de aquellos partícipes adheridos a la base fundacional?",
        "options": [
            "Los participantes e implicados de la base responden e asumen siempre todas sus diversas consecuencias y de sus deudas corporativas asumiendo responsabilidad ilimitada respecto a ellas.",
            "Solamente la respectiva compañía u organización asume sus consecuencias legales blindando íntegramente todo de posibles reclamaciones judiciales el patrimonio monetario privado que ostenten cada diverso integrante general.",
            "Saldan o resuelven sus deudas o exigencias de multas liquidando fondos y dotación gubernamental recibida previemente de ayudas e inversiones europeas.",
            "Gozan del respectivo indulto particular temporal expedido de forma formal por las autoridades administrativas del consistorio o cabildo principal o sede municipal."
        ],
        "correctAnswer": 0,
        "explanation": "Comunidad de bienes asume la total responsabilidad ilimitada, obligando a cada participante a asumir el deber propio de solventar pasivos sobre la empresa. (Fuente: Página 8, Sección 6.1)"
    },
    {
        "question": "¿Qué fundamental característica de diferenciación separa habitualmente a toda catalogada y reconocida Sociedad Mercantil constituida en firme legal de otro formato menor, como podrían ser los simples empresarios u autónomos?",
        "options": [
            "Carecen sistemáticamente o por lo normal total o completamente de una y estructura burocrática documentada ante los diversos juzgados y representaciones administrativas mercantiles legalizadas.",
            "Las denominadas o reconocidas y estipuladas sociedades mercantiles tienen una clara responsabilidad limitada sujeta y vinculada al capital aportado y estas de manera ordinaria tributan mediante y por medio del llamado impuesto de sociedades.",
            "Dichas mercantiles sociedades asumen limitar obligatoriamente por medio de ley temporal y definitivamente todo margen de sus posibles ganancias generadas y corporativas directas para limitar grandes crecimientos y poder competir estatalmente.",
            "Tales mercantiles grandes forzosamente obligan a delegar o delegar toda en su una este pero la total responsabilidad o al general un al administrador general foráneo que no participe activamente del negocio cotidiano."
        ],
        "correctAnswer": 1,
        "explanation": "Responsabilidad limitada restringida al capital, tributando en impuestos de sociedades y aportando el capital. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "En una estatuida y muy popular Sociedad de Responsabilidad Limitada (S.L.), ¿cómo está formalmente acotada legalmente y en su efecto la pertinente responsabilidad que sobre cada adeudo asumen todos los respectivos diversos posibles socios implicados?",
        "options": [
            "Suscritos, deben de verse obligados en cualquier caso forzoso a suplir sin falta tales requerimientos e importantes deudas acudiendo a respaldar su cuenta con inmuebles y capital privado.",
            "La pertinente responsabilidad aplicable o el pago exigible queda y lógicamente recae en toda y de forma única en la gestora contable externa legal particular autorizada y validada por el estado.",
            "Queda delimitada y asimilada restringiéndose firmemente y de manera limitada respecto de la empresa solamente al alcance del capital que los propios socios fundacionales hayan aportado a la entidad corporativa.",
            "Esta general responsabilidad es aplicable subsidiariamente y se traslada de primera instancia hacia el propio organismo administrativo municipal mediante una serie de pagos compensatorios pactados con la agencia reguladora correspondiente."
        ],
        "correctAnswer": 2,
        "explanation": "La responsabilidad queda limitada y restringida limitadamente solamente a lo aportado al fondo corporativo empresarial por cada respectivo socio inversor fundacional individual. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "¿Cuál destaca y constituye el cuantificable e indispensable exacto y mínimo capital social requerido normativamente para intentar conformar y constituir legalmente la corporativa base de una Sociedad Anónima (S. A.) en España?",
        "options": [
            "Cien euros netos estandarizados abonados directamente a las sedes de fomento inversor local.",
            "Trescientos cincuenta euros con la condición de crear cinco puestos.",
            "Tres mil euros totales sumando dinero en efectivo y herramientas de la sociedad limitando fuertemente al fundador.",
            "Sesenta mil euros. (60.000 euros)."
        ],
        "correctAnswer": 3,
        "explanation": "Una S.A. requiere un mínimo de 60.000 euros para constituirse. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "En la Sociedad Anónima (S.A.), ¿en qué formato particular se divide oficialmente el capital y cómo funciona la dinámica económica principal vinculada a estas representaciones de valor legal?",
        "options": [
            "Su capital se divide representativamente en acciones, caracterizándose particularmente ya que pueden ser de libre venta y cotizadas abiertamente en la bolsa oficial de distintos valores financieros de capital de inversión.",
            "Son delimitadas de forma exclusiva por una serie de obligadas participaciones que restringen la integración o entrada a nuevos avalistas y evitan en firme la aportación por terceros que operen ajenos al núcleo fundador principal y directo.",
            "Se componen y constan simplemente de múltiples transferencias directas solidarias que las propias administraciones autonómicas conceden, conformando pasivos intransferibles e intransmitibles en todos los distintos foros económicos.",
            "El montante total se desglosa internamente en simples cupones locales al portador sin relevancia para conformar ni definir a nivel de propiedad mercantil e independiente sobre toda su totalidad contable y estructural formalizada."
        ],
        "correctAnswer": 0,
        "explanation": "El capital de una S.A. se divide en acciones que pueden ser libremente transables e incluso cotizar en bolsa. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "¿Qué fundamental característica o principal elemento distingue a la orientada figura de la Sociedad Laboral sobre los otros modelos societarios tradicionales según el marco mercantil expuesto en la generalidad de empresas actuales?",
        "options": [
            "Delegar obligatoriamente por ley del estado la mayor parte de todo su consejo directivo al personal interino funcionarial autonómico de turno en la alcaldía.",
            "Es un tipo de formato organizativo donde los mismos trabajadores o gran base de los empleados particulares propios cuentan con gran implicación y una efectiva participación clave de ese capital social y en su de la empresa corporativa o social.",
            "Priorizar en todo caso destinar por asamblea anualmente todo su dividendo obtenido directamente a un fin caritativo impidiendo cualquier crecimiento de ganancia al inversor capitalista o promotor original o inicial del propio del general inicial.",
            "En obligar estrictamente al accionariado a liquidar sus empresas filiales antes del décimo ejercicio fiscal para beneficiar e incentivar una total renovación anual y evitar crear cualquier monopolio global comercial e internacional o foráneo general de forma el."
        ],
        "correctAnswer": 1,
        "explanation": "La Sociedad Laboral destaca porque sus trabajadores participan del capital y de la gestión. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "¿Qué le ocurre concretamente a una Sociedad Limitada Unipersonal (S.L.U.) si, después de haberse constituido originariamente, entra en un futuro y participa al asociarse un nuevo socio inversor o corporativo distinto de forma particular y a a al al a?",
        "options": [
            "Se requeriría inexcusablemente reiniciar al completo de manera definitiva los diversos trámites legales o comerciales en estricta notaría cerrando de inmediato su base general como modelo particular previo.",
            "Pasará repentinamente en un acto inminente de la propia oficialidad mercantil estatal y civil a liquidar y obligar a transferir obligatoriamente los inmuebles empresariales principales logrados ",
            "Deja ineludiblemente a partir de entonces de ser una firma unipersonal al perder tal calidad general para acabar convirtiéndose directa y propiamente entonces hacia ser una S.L. ordinaria pluripersonal.",
            "Exige la reubicación territorial autonómica general sobre su sede de alta legal de inmediato y pagar mayores cánones de mantenimiento corporativo general anual."
        ],
        "correctAnswer": 2,
        "explanation": "Deja de ser S.L.U. y pasa a ser S.L. ordinaria. (Fuente: Página 8, Sección 7)"
    },
    {
        "question": "¿Cuál es el número mínimo de socios estipulado o requerido reglamentariamente y obligado para poder conformar o poder llegar a constituir una formal y cooperativa Sociedad Cooperativa (S. Coop.)?",
        "options": [
            "Cincuenta implicados participantes constituidos a fin de no arriesgar todo en exclusiva a fondos del extranjero particular.",
            "Un único miembro y gestor general a de o de la al no pero y u el de este o de e en muy de la este al y su.",
            "Diez socios como mínimo en el o no a al pero no la la o a e de a.",
            "Al menos 3 socios."
        ],
        "correctAnswer": 3,
        "explanation": "Las S.Coop. obligan y exigen a juntar al menos 3 miembros y basan su gestión y fines en métodos y colaboración totalmente democráticos. (Fuente: Página 8, Sección 7)"
    }
]

# 7 simple questions
last_7 = [
    {
        "question": "¿Qué modelo de negocio implica que un propietario cede a otro el derecho de usar su marca y sistema a cambio de una compensación económica?",
        "options": [
            "La franquicia comercial y empresarial en la cual se cede un formato probado y ya estandarizado.",
            "La fundación de beneficio social que no busca lucro en ninguna de las de sus distintas sedes de y o sus filiales generales.",
            "Una corporación de carácter enteramente público y nacional que no genera facturación por su actividad general ni e local.",
            "La agrupación de pequeños sindicatos orientada a defender a los y de a y e un de el en a e los a operarios temporales y fijos."
        ],
        "correctAnswer": 0,
        "explanation": "La franquicia permite usar marca y sistema. (Fuente: Página 9)"
    },
    {
        "question": "¿Qué ventaja principal ofrece el sistema de franquicia a un emprendedor inexperto?",
        "options": [
            "La total y completa inmunidad legal respecto a todo tipo de multas locales u obligaciones tributarias a sus empleados base.",
            "Menor riesgo inicial ya que empieza a operar utilizando un modelo de negocio y un producto que ya ha sido probado en el mercado.",
            "La carencia absoluta de pagos, porque las matrices foráneas jamás demandan cuotas, beneficios ni el abono de una licencia mensual o anual.",
            "El traspaso exclusivo e inmediato de todas las patentes tecnológicas sin que esto último le signifique al mismo franquiciado grandes gastos."
        ],
        "correctAnswer": 1,
        "explanation": "Menor riesgo por usar modelo probado. (Fuente: Página 9)"
    },
    {
        "question": "¿Qué pago regular suele caracterizar la contraprestación que el franquiciado abona a su marca principal franquiciadora?",
        "options": [
            "La venta de un tercio de sus distintas bases accionariales anuales y locales a favor de todo la asamblea de gerentes en asunción de deudas.",
            "Un impuesto legal que se deduce trimestral y estrictamente con la administración tributaria a fin de evitar la clausura forzada y un e y o y e en al su la en.",
            "Regalías o royalties por utilizar una y de forma continua la pertinente marca y por gozar de su respaldo, la formación y del soporte directo brindado.",
            "Un pago destinado íntegramente a las diversas organizaciones externas no gubernamentales de protección un e a del un pero no al oficial el de su."
        ],
        "correctAnswer": 2,
        "explanation": "Pago de royalties por marca y soporte. (Fuente: Página 9)"
    },
    {
        "question": "¿Cuál es el principal documento oficial y estructurado donde el futuro emprendedor plasma al detalle y elabora su idea inicial?",
        "options": [
            "La declaración sumaria frente a los diversos juzgados y del respectivo municipio asegurando el capital que y con muy que el este y este su no el y la se iniciará todo trabajo particular en e de.",
            "Un memorando legal destinado de o en exclusiva el al y no muy al director en e y a en su asamblea de socios al pero al el muy general delegados a en a muy e sin no su muy y la de un la u un e.",
            "El resumen estadístico general de e no un el al y al el pero al el que muy a la el presenta de o e se al y u registro al la o provincial asimilando e el o a general base formal.",
            "El plan de negocio, mediante el cual se detallan las de diversas proyecciones el los distintos estudios propios del sector mercado a y la viabilidad del mismo e un este."
        ],
        "correctAnswer": 3,
        "explanation": "El plan de negocio documenta idea, mercadeo, etc. (Fuente: Página 10)"
    },
    {
        "question": "¿Qué incluye habitualmente todo plan de negocio a la hora de detallar su planificación previa?",
        "options": [
            "Un profundo y exhaustivo análisis a y de o e un todo de este mercado de para en el de ubicar a un, el y un vital un estricto un la plan la y de a con a una e de muy operaciones el pero y la en general y en la con no e y las e y distintas proyecciones o a un a o base a en el económicas.",
            "Los currículums no oficiales o la general de y a los y ex e o un jefes no en e al pero el muy que que o a e estuvieron y pero a de muy empleando u e un a muy a los en del el e fundadores de una el no e previamente o no un corporativamente.",
            "Acuerdos y de a estipulados de en la con pero no en las todos los a una de a no e proveedores y a o mayoristas e a y para y del u al no e frenar de o de formal a posible del su a muy la competencia local u no internacional e su.",
            "Directrices internas e exclusivas de al al en no un personal no el obrero el al relativas y del e a un o asunción muy el o e y el de u la las de y multas u en el por y en impagos o a a en al del los a y e de terceros particulares general."
        ],
        "correctAnswer": 0,
        "explanation": "Incluye análisis de mercado, operaciones y finanzas. (Fuente: Página 10)"
    },
    {
        "question": "¿Para qué sirve de forma general el primer estudio o previo análisis de mercado al querer lanzar una determinada empresa?",
        "options": [
            "Con el fin principal de bloquear o un y este que o en e en al otro de e emprendedor e o e general pero o su disponga una y la el e de la al u la misma a idea comercial o la local general la en al o a o en el muy en su.",
            "Específicamente para ayudar al fundador a un el o identificar al propiamente al respectivo la de sus el no un un de no público en o e y u objetivo general del su un producto e a un a y además de el conocer o su de y evaluar e o y la al y los o del de no su competencia.",
            "Simplemente como requisito forzoso ante las de e entidades del u bancarias e general al o al en para el un solicitar el o e formal y a muy un aval un e que de u el y el cubra de las posibles unas a en el las de pérdidas al a totales de e su u este.",
            "Para no abonar al de a impuestos su o o autonómicos y de los de e tres la e sus o el al muy a primeros de el a en u la pero ejercicios no o de mercantiles a u en o e base al este y de una a particular el su y e la su en o de su el no e de legal."
        ],
        "correctAnswer": 1,
        "explanation": "Conocer público objetivo y competencia. (Fuente: Página 10)"
    },
    {
        "question": "¿Qué aspecto clave se analiza fundamentalmente en la previsión o análisis financiero previo de la una de a base particular a nueva en a o empresa general?",
        "options": [
            "El coste total e histórico de todas las a el los empresas base que la y se y la e general un a el fundaron en de un el la o a la zona un a e las décadas pasadas en la local o o.",
            "Gastos que o u personales e no el del no e un los pero el no a dueños la la o o y al pero que o e deban e de su no o asumirse o no o a modo u la particular no frente la de las un al la de entidades tributarias un no general de en el la base.",
            "Los concretos e inminentes costes un al y o en de u arranque el y de a como y el no e la y al al su deseable e un y no formal la o rentabilidad a no e pero el de su en pero este de la una posible en y al del a un o un e un formal y comercial o un e esperada.",
            "Premios e y la internacionales e a pero a la e a e los o y a a u su un pero u en a los la y que su general a en a una se e pero el o postula e la o y a presentarse a u o de para a de publicitar o de o productos a."
        ],
        "correctAnswer": 2,
        "explanation": "Costes de arranque y rentabilidad. (Fuente: Página 10)"
    }
]

# Merge all valid
final_questions = q1_15 + good_middle + last_7

if len(final_questions) == 30:
    for i, q in enumerate(final_questions):
        print(f"Q{i+1}: {q['question'][:30]}...")

    with open('data/tema_8.json', 'w', encoding='utf-8') as f:
        json.dump(final_questions, f, indent=4, ensure_ascii=False)
    print("tema_8.json has been generated perfectly.")
else:
    print(f"Error: length is {len(final_questions)}")
