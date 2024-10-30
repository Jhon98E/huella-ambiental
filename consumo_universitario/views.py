from django.shortcuts import render


preguntas = {
    "p1": {
        "titulo": "Uso de dispositivos electrónicos",
        "pregunta": "¿Cuántas horas al día usas dispositivos electrónicos (laptop, celular, tablet) para estudiar o trabajar?",
        "unidad": ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]
    },
    "p2": {
        "titulo": "Energía en la universidad",
        "pregunta": "¿Con qué frecuencia utilizas los tomas electricos para cargar tus dispositivos electrónicos dentro del campus de la universidad?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p3": {
        "titulo": "Desperdicio Energetico",
        "pregunta": "¿Con qué frecuencia dejas tus dispositivos conectados después de que se han cargado por completo?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p4": {
        "titulo": "Energia en las aulas",
        "pregunta": "¿Al finalizar las clases desconectan los dispositivos y apagan las luces del aula?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p5": {
        "titulo": "Uso de baños",
        "pregunta": "¿Con qué frecuencia utiliza los baños de la universidad durante la semana?",
        "unidad": ["0","1 a 5","6 a 10","11 a 15","16 a 20","21 a 25"]
    },
    "p6": {
        "titulo": "Cerrar la llave",
        "pregunta": "¿Cierra la llave mientras se cepilla los dientes o se lava las manos?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p7": {
        "titulo": "Hidratacion",
        "pregunta": "¿Con que frecuencia utilizas las fuentes o bebederos de agua de la universidad al Dia?",
        "unidad": ["0","1","2","3","4","5","6","7","8","9","10"]
    },
    "p8": {
        "titulo": "Desperdicios",
        "pregunta": "¿Qué tipo de residuos arrojas al sanitario de la universidad?",
        "unidad": ["Ninguno","Liquidos","Solidos","Ambos"]
    },
    "p9": {
        "titulo": "Manejo de residuos",
        "pregunta": "¿Antes de desechar tu basura conoces en que recipiente debe de ir?",
        "unidad": ["No","Si"]
    },
    "p10": {
        "titulo": "Reutilizacion de recipientes",
        "pregunta": "¿Sueles reutilizar las botellas plásticas o prefieres comprar una nueva cada vez que necesitas agua?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p11": {
        "titulo": "Compartir transporte",
        "pregunta": "¿Sueles compartir tus medios de transporte con otros compañeros para reducir la huella de carbono?",
        "unidad": ["Nunca","Rara vez","Ocasionalmente","Frecuentemente","Siempre"]
    },
    "p12": {
        "titulo": "Medio de transporte",
        "pregunta": "¿Sueles caminar o usar bicicleta para llegar a la universidad? ¿Con qué frecuencia?",
        "unidad": ["Nunca","Ocasionalmente","Frecuentemente","Siempre"]
    }
}


def home(request):
    return render(request, 'home.html')

def calcular_huella(request):
    context = {
        'preguntas': preguntas
    }
    
    return render(request, 'calcular_huella.html', context)
