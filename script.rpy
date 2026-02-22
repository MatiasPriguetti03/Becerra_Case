define c = Character("Camila", color="#DB90CB")
define g = Character("Gladys", color="#ff2600")
define joa = Character("Joaquin", color="#0051ff")
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

    me "{i}¿Quien mierda está despierto a las 7 de la mañana?{/i}"

    "Reafirmas tu agarre a las sabanas y te das la vuelta para seguir durmiendo, pero el sonido de los golpes se vuelve mas insistente." 

    play sound fast_knock fadein 0.5

    pause 8.0

    me "{i}Pero la puta que los pario, quien mierda...{w=2.0}{nw}{/i}"

    me "{i}Hoy es mi cumpleaños.{/i}"

    me "{i}Mierda.{/i}"

    me "¡No voy a abrir! Asi que mejor vete a la mierda y dejame dormir en paz! Lo unico que quiero es tranquilidad."

    "El sonido de los golpes se detiene por un momento, pero luego vuelve a sonar, esta vez con mas fuerza y violencia."

    play sound hard_knock fadein 0.5

    '{color=#0051ff}???{/color}' "Policia de CABA ¡Abra la puerta! Necesitamos hablar contigo."

    me "¿¡La policia!?"

    play music police fadein 0.5 volume 0.5 loop 

    "Abres los ojos de golpe y te sientas en la cama, con el corazon latiendo a mil por hora."

    scene bg bedroom with fade:
        size(1920,1080)

    me "{i}¿Que mierda quieren de mi? ¿Que hice? ¿Me van a meter presa? ¿Me van a llevar a la comisaria? ¿Me van a torturar? ¡¿Que mierda?!{/i}"

    me "{i}BASTA de ser tan dramatica. Solo querran hacerte unas preguntas y listo. Que tanto.{/i}"

    "Te levantas de la cama y te acercas a la puerta, con el corazon en la boca. Tomas aire y abres la puerta."

    play sound door_opening fadein 0.5 volume 0.5

    show cam at center with fade

    "Una mujer joven de pelo negro ondulado y expresion decidida entra por tu puerta sin esperar invitacion. Se queda analizando el monoambiente con detenimiento."

    '{color=#DB90CB}???{/color}' "Agustina Rosas. Tenemos que hablar de un asunto importante contigo."

    '{color=#DB90CB}???{/color}' "Me esperaba una habitación más ordenada sinceramente."

    "La mujer se dirige hacia la cama de la habitacion y la prueba suavemente con sus manos. Luego, se acuesta de un salto en ella."

    '{color=#DB90CB}???{/color}' "Al menos la cama es comoda. ;)"

    scene bg nightclub:
        size(1920,1080)

    show pixel at center 

    jojo "Ella se {i}fue a la pista directo, y todo el mundo se le acercó{/i}."


    return
