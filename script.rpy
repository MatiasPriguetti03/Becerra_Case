# Declara los personajes usados en el juego como en el ejemplo:

define c = Character("Camile", color="#DB90CB")
define g = Character("Gladys", color="#ff2600")
define jack = Character("Jackson", color="#0051ff")
define jojo = Character("JOJO", color="#ffd000")
define m = Character("Maite", color="#645f55")
define sc = Character("Shanina", color="#752ab3")
define so = Character("Shanon", color="#f07400")
define me = Character("Me", color="#f6249f")

label start:

    "Es temprano por la mañana y sientes una comodidad interior. Acostada, tapada hasta el cuello, escuchas el sonido de la respiracion de annie a tu lado."

    me "Voy a quedarme un rato mas acostada..."

    me "Solo seran cinco minutos mas..."

    "Sientes como el sueño te vence de nuevo."

    "Y tu conciencia se apaga."

    scene bg bedroom:
        size(1920,1080)

    show cam at center:
        zoom 0.98

    c "He visto escenas del crimen más limpias que esta habitación."

    scene bg nightclub:
        size(1920,1080)

    show jojo at center 

    jojo "Ella se {i}fue a la pista directo, y todo el mundo se le acercó{/i}."


    return
