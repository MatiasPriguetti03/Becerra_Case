define c = Character("Camile", color="#DB90CB")
define g = Character("Gladys", color="#ff2600")
define jack = Character("Jackson", color="#0051ff")
define jojo = Character("JOJO", color="#ffd000")
define m = Character("Maite", color="#645f55")
define sc = Character("Shanina", color="#752ab3")
define so = Character("Shanon", color="#f07400")
define me = Character("Agus", color="#f6249f")

label start:
    play music sleep fadein 1.0 loop

    "Es temprano por la mañana y sientes una comodidad interior. Acostada, tapada hasta el cuello, escuchas el sonido de la respiracion de annie a tu lado."

    me "{i}Voy a quedarme un rato mas acostada...{/i}"

    me "{i}Solo seran cinco minutos mas...{/i}"

    "Sientes como el sueño te vence de nuevo y tu conciencia se apaga."

    pause 10.0

    stop music fadeout 1.0
    play sound rythmic_knock fadein 0.5

    pause 4.0

    "Alguien esta tocando la puerta de tu casa. Te preguntas quien podria ser a esta hora, pero no te levantas a abrir."

    me "{i}¿Quien putas esta rompiendo los ovarios a las 7 de la mañana?{/i}"

    "Reafirmas tu agarre a las sabanas y te das la vuelta para seguir durmiendo, pero el sonido de los golpes se vuelve mas insistente." 

    play sound fast_knock fadein 0.5

    pause 4.0

    me "{i}Pero la puta que los pario, quien carajos... {/i}"

    "El sonido de los golpes se vuelve mas insistente, y te preguntas si deberias levantarte a abrir la puerta."

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
