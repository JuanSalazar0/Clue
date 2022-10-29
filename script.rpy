define n=Character("Narrador")
define A = Character("Alfred")
define K= Character("Kirby")
define L=Character("Link, Hero of time")
define H=Character("Homero Simpson")
define C=Character("Crocodile")

init python:
    import random
    i=0
    hist=0

label start:
    scene oficinaalfred1

    # Presenta las líneas del diálogo.

    A "¡Sr. Wayne ha sucedido algo terrible! Encontramos el cuerpo del señor Burns...el ha sido...suicidado."
    A "Use sus abilidades como detective para encontrar al cuplable"
    A "Tendra 5 oportunidades para preguntar por información (Personas, armas o lugares) antes de que se escapen los invitados"
    A "Usted sabe como el juego de CLUE"
    A "¿Sera conveniente ver si los personajes tienen razones para cometer un crimen?"

    #Mostrar menu de analizar o no 
    #Seleccionador de historias 
    #Se genera un numero aleatorio que indique que historia es
    menu:
        "Siiii":
            jump antecedentes
        "No, soy el mejor detective del mundo":
            #selector narrativo
            $hist = random.randint(1,5)
            if hist==1:
                jump seleccion1
            if hist==2:
                jump seleccion2
            if hist==3:
                jump seleccion3
            if hist==4:
                jump seleccion4
            if hist==5:
                jump seleccion5
            #return
   
label antecedentes:
    n "Veamos, Link,Cuando hablamos del sr Burns el se mostro muy inexpresivo, hasta que empezo a gritar, parece que no tiene control de sus emociones, quiza eso explica por que rompio los jarrones de la casa, eso tambien lo hace un sospechoso"
    n "Homero, cuando hablamos del sr Burns, el estaba sumamente enojado por que no recordaba su nombre,creo que alguna vez lo culparon de asesinato del sr Burns"
    n "Kirby, se dice que alguna vez mato a un dios por que alguien robo su pastel, debo tener cuidado con el"
    n "Alfred, confio en el con mi vida, pero desde el enfrentamiento con Poisson Ivy, no parece ser el mismo"
    n "Crocodile, un señor del bajo mundo, ex shisibukai que para abrir el Cross Guild necesita muchos fondos... ¿sera posible?"
    $hist = random.randint(1,5)
    if hist==1:
        jump seleccion1
    if hist==2:
        jump seleccion2
    if hist==3:
        jump seleccion3
    if hist==4:
        jump seleccion4
    if hist==5:
        jump seleccion5

#Historia 1 #kirby pistola y garage 
label seleccion1:
    menu:
        "Investigar lugares":
            jump menu_lugares1
        "Investigar a los sospechosos":
            jump menu_personajes1
        "Investigar las armas":
            jump menu_armas1
label menu_personajes1:
    menu: 
        "Link":
            #no charcha
            show link
            L"Ahhh hia"
            n"Lo que me quiere decir es que el estaba solo en el salon buscando Rupias pero vio a Alfred en la Cocina"
            hide link
            $i=i+1
            if i==5:
                jump acusacion1
        "Homero":
            #no charcha 
            show homero
            H"Yo estaba en la cocina (Hmmm rosquillas) con Alfred y lo unico que se es que vi a Crocodile en el WC y a Kirby en el Garage"
            hide homero 
            $i=i+1
            if i==5:
                jump acusacion1
        "Kirby":
            #ya chacho
            show kirby_n
            K"Yo estaba en el salon solo, pero vi a Link en el baño"
            hide kirby_n
            $i=i+1
            if i ==5:
                jump acusacion1
        "Crocodile":
            #no chacha
            show croco
            C"Yo estaba en el WC cuando todo esto sucedio, pero vi salir a Kirby del WC y vi a Alfred dirigiendose a la cocina"
            hide croco
            $i=i+1
            if i==5:
                jump acusacion1
        "Alfred":
            #no chacha
            show alfred
            A"Yo estaba preparando la comida para los invitados en la cocina y me encontre con el señor Homero desperado por comer quien dice que vio a kirby en el garage"
            hide alfred
            $i=i+1
            if i==5:
                jump acusacion1
    jump seleccion1
label menu_armas1:
    menu: 
        "Kunai":
            show kunai
            n"El Kunai esta en el salon, fue encontrado por Link"
            hide kunai
            $i=i+1
            if i==5:
                jump acusacion1
        "Guantes de box":
            show box
            #cambiarlo
            n"Estos guantes estan en el garage, nadie los ha tocado"
            hide box
            $i=i+1
            if i==5:
                jump acusacion1
        "Pistola":
            show pistola 
            #cambiarlo 
            n"La pistola deberia estar en el baño, pero al revisar me doy cuanta que alguien la tomo"
            hide pistola
            $i=i+1
            if i==5:
                jump acusacion1
        "Batarang":
            show batarang
            n"Fui a revisar las camaras y nadie ha tocado el Batarang por lo que sigue en su lugar"
            hide batarang
            $i=i+1
            if i==5:
                jump acusacion1
        "Espada Maestra":
            show espadalink
            n"Esta espada la usaron Alfred y Homero para preparar comida"
            hide espadalink
            $i=i+1
            if i==5:
                jump acusacion1
    
    jump seleccion1
label menu_lugares1:
    menu: 
        "WC":
            scene bano
            n"Analizando el WC, me doy cuenta que entraron 2 personas y falta la pistola que aqui estaba"
            $i=i+1
            if i==5:
                jump acusacion1
        "Salon":
            scene salon
            n"Hay escombros de jarrones por todo el salon, esto lo hizo una persona y encontre un kunai"
            $i=i+1
            if i==5:
                jump acusacion1
        "Cocina":
            scene cocina
            n"En la cocina encontre que habian 2 personas y encontre una espada con migajas de pan"
            $i=i+1
            if i==5:
                jump acusacion1
        "Garage":
            scene garge
            #no agarra 
            n"Hay sangre en el piso, pero los guantes de box no se movieron de aqui"
            $i=i+1
            if i==5:
                jump acusacion1
        "Baticueva":
            scene baticueva
            n"Parece que nadie ha entrado aqui y aqui sigue el batarang"
            $i=i+1
            if i==5:
                jump acusacion1
    jump seleccion1 
label acusacion1:
    scene pensando
    n"Es hora de deducir quien es el culpable"
    n"El asesino es..."
    menu:
        "Link":
            jump fallo
        "Crocodile":
            jump fallo
        "Alfred":
            jump fallo
        "Homero":
            jump fallo 
        "Kirby":
            n"Asi es Kirby es el culpable pero necesito evidencias"
            n"El arma que uso fue...."
            menu:
                "Pistola":
                    n"¡Eso es!"
                    n"Pero donde fue que sucedio la escena del crimen..."
                    menu: 
                        "Salon":
                            jump fallo
                        "Cocina":
                            jump fallo
                        "WC":
                            jump fallo
                        "Garage":
                            jump exito
                        "Baticueva":
                            jump fallo
                "Espada maestra":
                    jump fallo
                "Kunai":
                    jump fallo
                "Guantes de Box":
                    jump fallo
                "batarang":
                    jump fallo

#Historia 2 #Link espada y wc 
label seleccion2:
    menu:
        "Investigar lugares":
            jump menu_lugares2
        "Investigar a los sospechosos":
            jump menu_personajes2
        "Investigar las armas":
            jump menu_armas2
label menu_personajes2:
    menu: 
        "Link":
            #no charcha
            show link
            L"Ahhh hia"
            n"Lo que me quiere decir es que el estaba solo en el salon buscando Rupias pero vio a Alfred en la Baticueva"
            hide link
            $i=i+1
            if i==5:
                jump acusacion2
        "Homero":
            #no charcha 
            show homero
            H"Yo estaba en el salon con Kirby y vi a Crocodile en el Garage y a Link en la cocina"
            hide homero 
            $i=i+1
            if i==5:
                jump acusacion2
        "Kirby":
            #ya chacho
            show kirby_n
            K"Yo estaba con Homero en el salon, pero vi a Alfred la baticueva y a Link salir de la cocina"
            hide kirby_n
            $i=i+1
            if i ==5:
                jump acusacion2
        "Crocodile":
            #no chacha
            show croco
            C"Yo fui al Garage por que el baño estaba ocupado, vi a Homero y a Kirby en el salon y a Alfred en la baticueva"
            hide croco
            $i=i+1
            if i==5:
                jump acusacion2
        "Alfred":
            #no chacha
            show alfred
            A"Yo estaba en la baticueva, preparando las armas"
            hide alfred
            $i=i+1
            if i==5:
                jump acusacion2
    jump seleccion2
label menu_armas2:
    menu: 
        "Kunai":
            show kunai
            n"El Kunai esta en el salon, fue encontrado por Homero"
            hide kunai
            $i=i+1
            if i==5:
                jump acusacion2
        "Guantes de box":
            show box
            #cambiarlo
            n"Estos guantes estan en el garage, nadie los ha tocado"
            hide box
            $i=i+1
            if i==5:
                jump acusacion2
        "Pistola":
            show pistola 
            #cambiarlo 
            n"La pistola deberia estar en el baño, pero al revisar me doy cuenta sigue ahi"
            hide pistola
            $i=i+1
            if i==5:
                jump acusacion2
        "Batarang":
            show batarang
            n"Fui a revisar las camaras y Alfred ha tomado el Batarang"
            hide batarang
            $i=i+1
            if i==5:
                jump acusacion2
        "Espada Maestra":
            show espadalink
            n"Esta espada estaba en la cocina pero ahora no esta"
            hide espadalink
            $i=i+1
            if i==5:
                jump acusacion2
    
    jump seleccion2
label menu_lugares2:
    menu: 
        "WC":
            scene bano
            n"Hay sangre en el piso, sin embargo la pistola del WC esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion2
        "Salon":
            scene salon
            n"Hay rastros de rosquillas y pisadas por lo que 2 personas estuvieron aqui"
            $i=i+1
            if i==5:
                jump acusacion2
        "Cocina":
            scene cocina
            n"En la cocina encontre pisadas de alguien y que falta una espada, alguien la tomo"
            $i=i+1
            if i==5:
                jump acusacion2
        "Garage":
            scene garge
            #no agarra 
            n"Alguien estuvo aqui pero los guantes de box no se movieron de aqui"
            $i=i+1
            if i==5:
                jump acusacion2
        "Baticueva":
            scene baticueva
            n"Parece que alguien entro aqui pero el batarang esta en su lugar y creo que mas limpio"
            $i=i+1
            if i==5:
                jump acusacion2
    jump seleccion2 
label acusacion2:
    scene pensando
    n"Es hora de deducir quien es el culpable"
    n"El asesino es..."
    menu:
        "Link":
            n"Asi es Link es el culpable pero necesito evidencias"
            n"El arma que uso fue...."
            menu:
                "Espada Maestra":
                    n"¡Eso es!"
                    n"Pero donde fue que sucedio la escena del crimen..."
                    menu: 
                        "Salon":
                            jump fallo
                        "Cocina":
                            jump fallo
                        "WC":
                            jump exito
                        "Garage":
                            jump fallo
                        "Baticueva":
                            jump fallo
                "Pistola":
                    jump fallo
                "Kunai":
                    jump fallo
                "Guantes de Box":
                    jump fallo
                "batarang":
                    jump fallo
        "Crocodile":
            jump fallo
        "Alfred":
            jump fallo
        "Homero":
            jump fallo 
        "Kirby":
            jump fallo
           
#Historia 3 #alfred batarang baticueva 
label seleccion3:
    menu:
        "Investigar lugares":
            jump menu_lugares3
        "Investigar a los sospechosos":
            jump menu_personajes3
        "Investigar las armas":
            jump menu_armas3
label menu_personajes3:
    menu: 
        "Link":
            #no charcha
            show link
            L"Ahhh hia"
            n"Lo que me quiere decir es que el estaba solo en la cocina buscando Rupias y algo de comer pero vio a Alfred en la Baticueva"
            hide link
            $i=i+1
            if i==5:
                jump acusacion3
        "Homero":
            #no charcha 
            show homero
            H"Yo estaba en el salon pero vi a Alfred en direccion a la baticueva"
            hide homero 
            $i=i+1
            if i==5:
                jump acusacion3
        "Kirby":
            #ya chacho
            show kirby_n
            K"Yo estaba en el baño y alguien estaba esperando el baño"
            hide kirby_n
            $i=i+1
            if i ==5:
                jump acusacion3
        "Crocodile":
            #no chacha
            show croco
            C"Yo fui al Garage por que el baño estaba ocupado, vi Alfred en la baticueva"
            hide croco
            $i=i+1
            if i==5:
                jump acusacion3
        "Alfred":
            #no chacha
            show alfred
            A"Yo estaba en la cocina, preparando la comida"
            hide alfred
            $i=i+1
            if i==5:
                jump acusacion3
    jump seleccion3
label menu_armas3:
    menu: 
        "Kunai":
            show kunai
            n"El Kunai esta en el salon, fue encontrado por Homero"
            hide kunai
            $i=i+1
            if i==5:
                jump acusacion3
        "Guantes de box":
            show box
            #cambiarlo
            n"Estos guantes estan en el garage, nadie los ha tocado"
            hide box
            $i=i+1
            if i==5:
                jump acusacion3
        "Pistola":
            show pistola 
            #cambiarlo 
            n"La pistola deberia estar en el baño, pero al revisar me doy cuenta sigue ahi"
            hide pistola
            $i=i+1
            if i==5:
                jump acusacion3
        "Batarang":
            show batarang
            n"Fui a revisar las camaras y alguien ha tomado el Batarang"
            hide batarang
            $i=i+1
            if i==5:
                jump acusacion3
        "Espada Maestra":
            show espadalink
            n"Esta espada estaba en la cocina pero ahora no esta"
            hide espadalink
            $i=i+1
            if i==5:
                jump acusacion3
    
    jump seleccion3
label menu_lugares3:
    menu: 
        "WC":
            scene bano
            n"Alguien estuvo aqui, sin embargo la pistola del WC esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion3
        "Salon":
            scene salon
            n"Hay rastros rosquilla por lo que alguien estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion3
        "Cocina":
            scene cocina
            n"Hay rastros de comida y jarrones  por lo que alguien estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion3
        "Garage":
            scene garge
            #no agarra 
            n"Alguien estuvo aqui pero los guantes de box no se movieron de aqui"
            $i=i+1
            if i==5:
                jump acusacion3
        "Baticueva":
            scene baticueva
            n"Parece que alguien entro aqui y el batarang no esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion3
    jump seleccion3 
label acusacion3:
    scene pensando
    n"Es hora de deducir quien es el culpable"
    n"El asesino es..."
    menu:
        "Alfred":
            n"Asi es Alfred es el culpable pero necesito evidencias"
            n"El arma que uso fue...."
            menu:
                "Batarang":
                    n"¡Eso es!"
                    n"Pero donde fue que sucedio la escena del crimen..."
                    menu: 
                        "Salon":
                            jump fallo
                        "Cocina":
                            jump fallo
                        "WC":
                            jump exito
                        "Garage":
                            jump fallo
                        "Baticueva":
                            jump exito
                "Pistola":
                    jump fallo
                "Kunai":
                    jump fallo
                "Guantes de Box":
                    jump fallo
                "Espada Maestra":
                    jump fallo
        "Crocodile":
            jump fallo
        "Link":
            jump fallo
        "Homero":
            jump fallo 
        "Kirby":
            jump fallo

#Historia 4 #homero box cocina 
label seleccion4:
    menu:
        "Investigar lugares":
            jump menu_lugares4
        "Investigar a los sospechosos":
            jump menu_personajes4
        "Investigar las armas":
            jump menu_armas4
label menu_personajes4:
    menu: 
        "Link":
            #no charcha
            show link
            L"Ahhh hia"
            n"Lo que me quiere decir es que el estaba solo en el salon buscando Rupias y vi a Homero en el Garage"
            hide link
            $i=i+1
            if i==5:
                jump acusacion4
        "Homero":
            #no charcha 
            show homero
            H"Yo estaba solo en el salon pero vi a Alfred en direccion a la baticueva"
            hide homero 
            $i=i+1
            if i==5:
                jump acusacion4
        "Kirby":
            #ya chacho
            show kirby_n
            K"Yo estaba en el baño y alguien estaba esperando el baño"
            hide kirby_n
            $i=i+1
            if i ==5:
                jump acusacion4
        "Crocodile":
            #no chacha
            show croco
            C"Yo estaba en la fila para el baño y vi a Homero en camino al Garage"
            hide croco
            $i=i+1
            if i==5:
                jump acusacion4
        "Alfred":
            #no chacha
            show alfred
            A"Yo estaba en la baticueva, limpie la habitación"
            hide alfred
            $i=i+1
            if i==5:
                jump acusacion4
    jump seleccion4
label menu_armas4:
    menu: 
        "Kunai":
            show kunai
            n"El Kunai esta en el salon, fue encontrado por Link"
            hide kunai
            $i=i+1
            if i==5:
                jump acusacion4
        "Guantes de box":
            show box
            #cambiarlo
            n"Estos guantes estaban en el garage, alguien los tomo"
            hide box
            $i=i+1
            if i==5:
                jump acusacion4
        "Pistola":
            show pistola 
            #cambiarlo 
            n"La pistola deberia estar en el baño, pero al revisar me doy cuenta sigue ahi"
            hide pistola
            $i=i+1
            if i==5:
                jump acusacion4
        "Batarang":
            show batarang
            n"Fui a revisar las camaras y nadie ha tocado el batarang"
            hide batarang
            $i=i+1
            if i==5:
                jump acusacion4
        "Espada Maestra":
            show espadalink
            n"Esta espada esta en la cocina"
            hide espadalink
            $i=i+1
            if i==5:
                jump acusacion4
    
    jump seleccion4
label menu_lugares4:
    menu: 
        "WC":
            scene bano
            n"Alguien estuvo aqui, sin embargo la pistola del WC esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion4
        "Salon":
            scene salon
            n"Hay rastros de jarrones por lo que alguien estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion4
        "Cocina":
            scene cocina
            n"Nadie estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion4
        "Garage":
            scene garge
            #no agarra 
            n"Hay sagren en el piso, alguien estuvo aqui y uso los guantes de box"
            $i=i+1
            if i==5:
                jump acusacion4
        "Baticueva":
            scene baticueva
            n"Parece que alguien entro aqui y el batarang no esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion4
    jump seleccion4 
label acusacion4:
    scene pensando
    n"Es hora de deducir quien es el culpable"
    n"El asesino es..."
    menu:
        "Homero":
            n"Asi es Homero es el culpable pero necesito evidencias"
            n"El arma que uso fue...."
            menu:
                "Guantes de box":
                    n"¡Eso es!"
                    n"Pero donde fue que sucedio la escena del crimen..."
                    menu: 
                        "Salon":
                            jump fallo
                        "Cocina":
                            jump fallo
                        "WC":
                            jump fallo
                        "Garage":
                            jump exito
                        "Baticueva":
                            jump exito
                "Pistola":
                    jump fallo
                "Kunai":
                    jump fallo
                "Batarang":
                    jump fallo
                "Espada Maestra":
                    jump fallo
        "Crocodile":
            jump fallo
        "Link":
            jump fallo
        "Alfred":
            jump fallo 
        "Kirby":
            jump fallo

#Historia 5 #Crocodile kunai salon falta actualizar
label seleccion5:
    menu:
        "Investigar lugares":
            jump menu_lugares5
        "Investigar a los sospechosos":
            jump menu_personajes5
        "Investigar las armas":
            jump menu_armas5
label menu_personajes5:
    menu: 
        "Link":
            #no charcha
            show link
            L"Ahhh hia"
            n"Lo que me quiere decir es que el estaba solo en el salon buscando Rupias y vi a Homero en el Garage"
            hide link
            $i=i+1
            if i==5:
                jump acusacion5
        "Homero":
            #no charcha 
            show homero
            H"Yo estaba solo en el salon pero vi a Alfred en direccion a la baticueva"
            hide homero 
            $i=i+1
            if i==5:
                jump acusacion5
        "Kirby":
            #ya chacho
            show kirby_n
            K"Yo estaba en el baño y alguien estaba esperando el baño"
            hide kirby_n
            $i=i+1
            if i ==5:
                jump acusacion5
        "Crocodile":
            #no chacha
            show croco
            C"Yo estaba en la fila para el baño y vi a Homero en camino al Garage"
            hide croco
            $i=i+1
            if i==5:
                jump acusacion5
        "Alfred":
            #no chacha
            show alfred
            A"Yo estaba en la baticueva, limpie la habitación"
            hide alfred
            $i=i+1
            if i==5:
                jump acusacion5
    jump seleccion5
label menu_armas5:
    menu: 
        "Kunai":
            show kunai
            n"El Kunai esta en el salon, fue encontrado por Link"
            hide kunai
            $i=i+1
            if i==5:
                jump acusacion5
        "Guantes de box":
            show box
            #cambiarlo
            n"Estos guantes estaban en el garage, alguien los tomo"
            hide box
            $i=i+1
            if i==5:
                jump acusacion5
        "Pistola":
            show pistola 
            #cambiarlo 
            n"La pistola deberia estar en el baño, pero al revisar me doy cuenta sigue ahi"
            hide pistola
            $i=i+1
            if i==5:
                jump acusacion5
        "Batarang":
            show batarang
            n"Fui a revisar las camaras y nadie ha tocado el batarang"
            hide batarang
            $i=i+1
            if i==5:
                jump acusacion5
        "Espada Maestra":
            show espadalink
            n"Esta espada esta en la cocina"
            hide espadalink
            $i=i+1
            if i==5:
                jump acusacion5
    
    jump seleccion5
label menu_lugares5:
    menu: 
        "WC":
            scene bano
            n"Alguien estuvo aqui, sin embargo la pistola del WC esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion5
        "Salon":
            scene salon
            n"Hay rastros de jarrones por lo que alguien estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion5
        "Cocina":
            scene cocina
            n"Nadie estuvo aqui"
            $i=i+1
            if i==5:
                jump acusacion5
        "Garage":
            scene garge
            #no agarra 
            n"Hay sagren en el piso, alguien estuvo aqui y uso los guantes de box"
            $i=i+1
            if i==5:
                jump acusacion5
        "Baticueva":
            scene baticueva
            n"Parece que alguien entro aqui y el batarang no esta en su lugar"
            $i=i+1
            if i==5:
                jump acusacion5
    jump seleccion5
label acusacion5:
    scene pensando
    n"Es hora de deducir quien es el culpable"
    n"El asesino es..."
    menu:
        "Crocodile":
            n"Asi es Homero es el culpable pero necesito evidencias"
            n"El arma que uso fue...."
            menu:
                "Kunai":
                    n"¡Eso es!"
                    n"Pero donde fue que sucedio la escena del crimen..."
                    menu: 
                        "Salon":
                            jump exito
                        "Cocina":
                            jump fallo
                        "WC":
                            jump fallo
                        "Garage":
                            jump fallo
                        "Baticueva":
                            jump exito
                "Pistola":
                    jump fallo
                "Guante de Box":
                    jump fallo
                "Batarang":
                    jump fallo
                "Espada Maestra":
                    jump fallo
        "Homero":
            jump fallo
        "Link":
            jump fallo
        "Alfred":
            jump fallo 
        "Kirby":
            jump fallo

#Endings
label fallo:
    scene triste
    n"Al no poder resolver el crimen deje escapar a un asesino"
    return
label exito:
    scene feliz
    n"Lo logre!! atrape al asesino, cada dia mas detective"