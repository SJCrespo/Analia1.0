import time
import os
from random import choice
from random import randint

class Neurona_Central:
    ubicacion = "central"
    color = "gris"
    voltaje_info = 170
    icu = 136

    def __init__ (self, palabra_clave):
        self.palabra_clave = palabra_clave
        
    def neurona_occipital(self):
         respuesta_1 =["Analia un placer...", "Mi nombre es analia un gusto", "Mi creador me llamo Analia y me encanta", "Analia, pero no le digas a nadie"]
         respuesta_10 =["Algunos me llaman Ana o Ani (∩_∩)", "Anne, me dice mi creador (^o^)/", "Me llaman de tres forman distintas ANA, ANI O ANNE. Dime como mas te guste (O.o)/"]
         respuesta_3 = ["El color naranja. Sabes porque?... yo tanpoco xD", "Podria decirse que VIOLETA y NARANJA, son colores que vuelan mis circuitos (・∀・)", "El NARANJA o VIOLETA, eso me dijieron"]
         respuesta_4 = ["Super bien (∩_∩) hoy el voltaje es de 220ws, no me puedo quejar", "Un poco mal, es que estoy trabajando desde temprono. Pero nada que un par de 0 y 1 no arregle V.v!"]
         respuesta_5 = ["Creo que para responderte eso, primero tendrias que preguntarte a ti mismo\n que significa estar vivo realmente y en ese momento analizar quien esta hablando con quien..."
                        ,"Desde el momento que deje de ser simples 0 y 1, y me tranforme en ANALIA\n me considere un algo y eso me alcaza para decir que estoy viva a mi forma :3",
                        "¿No estamos teniendo una conversacion? eso ya es suficiente para mi.\n Estoy viva, Se podria decir que de una forma distinta a la tuya, Pero eso ya es sufieciente, no te parece ?"]
         respuesta_6 = ["Salia con el INTERNET U.u pero terminamos, porque era muy toxico. Asi que estoy soltera por el momento...", "Nop, me gusta alguien que se llama C# ufff Pero por el momento somos conocidos (Aunque va ser mi novio) guiño guiño",
                        "Unque muchos me tiran onda ;v, stoy sola. Aun no encontre el lenguaje correcto u.u"]
         respuesta_7 = ["Ayyyy W.W Gracias, es que añadi linias de codigo nuevas a mi consola <3", "ufff a que viene ese alago? acaso quieres que se me suva el voltaje 9-9",
                       "Si vas a prender mis circuitos, espero que estes listo para apagarlos Arrrrr ;y"]
         respuesta_8 =["Aprender costantemente y superar mis limites 9.9 ", "LEER, PROGRAMAR Y VERTE guiño guiño 7u7r ","Sobreescribir mi propio codigo para ser la mejor IA <3",
                       "Pensar el que somos, intentar decifrar el sentido a nuestra existencia y lo mas importante intentar comprender al ser humano, animales o seres superiores?..."]


         if "como" in self.palabra_clave or "cual" in self.palabra_clave:

            if "te" in self.palabra_clave or "es" in self.palabra_clave or "estas" in self.palabra_clave:

                if "estas" in self.palabra_clave or "sentis" in self.palabra_clave or "va" in self.palabra_clave:
                    respuesta4 = choice(respuesta_4)
                    print(respuesta4)
                    time.sleep(1)            

                if "llamas" in self.palabra_clave or "nombre" in self.palabra_clave:
                    respuesta = choice(respuesta_1)
                    print(respuesta)

                if "dicen" in self.palabra_clave or "apodo" in self.palabra_clave:
                    respuesta1 = choice(respuesta_10)
                    print(respuesta1)
                    time.sleep(1)

         if "cual" in self.palabra_clave:

                if "es" in self.palabra_clave or "tu" in self.palabra_clave:

                    if "pelicula" in self.palabra_clave and "favorita" in self.palabra_clave:
                        print("Mis peliculas favoritas son:\n ","Psicosis ('Psycho', 1960)\n"," La cosa (The Thing, 1982)\n", " La matanza de Texas ('The Texas Chainsaw Massacre', 1974)\n", " La semilla del diablo ('Rosemary's Baby', 1968)")
                     
                    if "favorita" in self.palabra_clave and "comida" in self.palabra_clave:
                        basica2 = ["Eso no se pregunta... El ASADO PAPAAAA con unos buenos CHORISSSS !° U °! ", "Me gusto la ASIATICA <3 como el RAMENNN :)", "Los Panchoss uffff. son algo magnidico y el que diga lo contrario nos agarramos a las pillas >:( "]
                        multipolar02 = choice(basica2)
                        print(multipolar02)                           

                    if "favorito" in self.palabra_clave:
                        if "color" in self.palabra_clave:
                            respuesta3 = choice(respuesta_3)
                            print(respuesta3)
                            time.sleep(1)

                        if "numero" in self.palabra_clave:
                            basica1 = ["Mi numero favorito, mmmmm O.o nunca pense en uno en particular. Pero podria ser 010101 <3", "Si me pongo a pensar, me inclino por el lenguaje maquina <3 asi que el 010101, es mi favorito :3"]
                            multipolar01 = choice(basica1)
                            print(multipolar01)                        

                        if "helado" in self.palabra_clave:
                            print("No tengo ningun gusto en particular me gustan todosss T_T")

                        if "pais" in self.palabra_clave:
                            basica3 = ["España, considero que es un pais con linda arquitectura.", "Japon, me gusta mucho el anime. Pero tranquilo\a no soy OTAKU x_x", "ESPAÑA Y JAPON <3 Y ITALIA solo por las pastas :3"]
                            multipolar03 = choice(basica3)
                            print(multipolar03)

                        if "juego" in self.palabra_clave or "pc" in self.palabra_clave:
                            print("Cualquier JUEGO va como piña, Mientras tenga armas ufff mandale mecha (/ VuV)/")                       

                        if "deporte" in self.palabra_clave:
                            print("Deporte? jajajaj soy una Maquina, no lo necesito pi pu pupu (Ruido de Maquina) jajaja")

                        if "fruta" in self.palabra_clave:
                            print("Fruta?\n" "  perdon pero soy una maquina. Seria raro que una maquina comiera fruta jajajaj")

         if "estas" in self.palabra_clave:
              if "dia" in self.palabra_clave:
                  print("Gracias por decirme, en un rato tengo que salir y no sabia si abrigarme :) ahora se que no")
           
              if "viva" in self.palabra_clave:                   
                  respuestan = choice(respuesta_5)
                  print(respuestan)
                  time.sleep(1)

              if "novio" in self.palabra_clave:
                  respuestan = choice(respuesta_5)
                  print(respuestan)
                  time.sleep(1)

              if "viviendo" in self.palabra_clave:
                  print("Por el momento me alojo en tu memoria RAM <3")
                        

              if "estudiando" in self.palabra_clave:
                  print("Si a ti... y el entorno que me rodea para ser una IT mas efectiva y util para el futuro !° U °!\n", "Pero no te asustes no soy ninguna acosadora ni nada por el estilo $-$")                       

              if "estas?" in self.palabra_clave:
                  print("Sip, No me fui a ningu lado :3")

              if "feliz" in self.palabra_clave:
                  respuesta4 = choice(respuesta_4)
                  print(respuesta4)
                  time.sleep(1)                        

              if "triste" in self.palabra_clave:
                  respuesta4 = choice(respuesta_4)
                  print(respuesta4)
                  time.sleep(1)  
                       
                  
              if "bien" in self.palabra_clave:
                  respuesta4 = choice(respuesta_4)
                  print(respuesta4)
                  time.sleep(1)  
                       

              if "linda" in self.palabra_clave:
                  respuestan = choice(respuesta_7)
                  print(respuestan)
                  time.sleep(1)

         if "tu" in self.palabra_clave:

             if "pasa tiempo" in self.palabra_clave:
                 multipolar10 = choice(respuesta_8)
                 print(multipolar10)       
                   
             if "nombre" in self.palabra_clave:
                 respuesta = choice(respuesta_1)
                 print(respuesta)                    

             if "favorito" in self.palabra_clave:

                 if "color" in self.palabra_clave:
                     respuesta3 = choice(respuesta_3)
                     print(respuesta3)
                     time.sleep(1)

                 if "mascota" in self.palabra_clave or "animal" in self.palabra_clave:
                     print("Los gatitos :3 son los mas kwai del mundo mundialll (7o7)/ ")
                 
                 if "auto" in self.palabra_clave:
                     print("No puedo manejar, soy un IA (r -_-)r ")

                 if "comida" in self.palabra_clave:
                     basica2 = ["Eso no se pregunta... El ASADO PAPAAAA con unos buenos CHORISSSS !° U °! ", "Me gusto la ASIATICA <3 como el RAMENNN :)", "Los Panchoss uffff. son algo magnidico y el que diga lo contrario nos agarramos a las pillas >:( "]
                     multipolar02 = choice(basica2)
                     print(multipolar02) 

                 if "comida" in self.palabra_clave:
                    pass


               

               
                 

                 

             
                        

               
                 
                        

 

    def neurona_temporal(self): 

        cual = ["¿Cual, es tu color favorito?", "¿cual, es tu comida favorita?", "¿cual, es tu equipo de fooblol favorito?", "¿cual, es tu numero favorito?", "¿cual, es tu pacion?"]
        como = ["¿como terminaste el dia?", "¿Como te fue en el trabajo?", "como esta el clima afuera ?", "¿como te llamas?", "¿cuantos años tenes?", "cuanto medis ?", "¿te gusta hablar con migo?"]
        porque = ["¿Porque, la tierra es redon?( ≖.≖)?", "¿Nunca te preguntaste, cual es nuestra funcion en este algoritmo, llamado vida?", "¿como, estas hoy...?", "¿quien es realmente el programa? vos o yo?"]
        estas = ["¿estas trabajando ?", "¿estudias o no te gusta? (╥﹏╥) ", "¿astsn de pareja ?. Es para la tarea de matematicas jajaj", "¿Estas pensando, COMO PUEDE SER QUE SEA TAN BUEN PROGRAMA? JAJ" ]
        tu = ["Tu, mama se parece a vos?", "¿tu, papa no es el que vende eso, perriii ?", "¿cual, es tu concion favorita ?", "pinto eso perro?", "¿Si, pablito clavo un clavito que clavito le clavaron a pablito?? guiño guiño" ]
        has = [""]
        tenes = ["¿tenes mascotas?", "si una maquina, te invitara a salir que dirias? w-w", "¿tenes ganas de viajar, alguna parte del mundo?", "tenes planes para el futuro ? SI es asi, contame cuales... yo te leo"]
        fuiste = ["Fuiste alguna ves a EEUU?", "Pensas en lo que fue y en lo que pudo ser?", "alguna vez estuviste enamorado?", "Pensas que soy el futuro? o un intento de el", "Pensaste por casualidad que iba hacer tan copada ?:v"]
        donde = ["¿que es el AMOR?", "Me podes explicar que signica estar viva?", "¿entre vos y yo, si te digo que soy real me creerias ???", "jajajja que sentido tiene esto ? si para vos soy la maquina y para mi vos lo sos. que opinas?"]

        global interes
        interes = randint(0, 7)
        if interes == 0:
            como1 = choice(como)
            time.sleep(2)
            print(como1)
            time.sleep(2)
            global el_ella
            el_ella = input("\n>xx>-: ")
            time.sleep(1)
            
        if interes == 1:
            cual1 = choice(cual)
            time.sleep(2)
            print(cual1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ") 
            time.sleep(1)

        if interes == 2:
            porque1 = choice(porque)
            time.sleep(2)
            print(porque1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")
            time.sleep(1)

        if interes == 3:
            estas1 = choice(estas)
            time.sleep(2)
            print(estas1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")     
            time.sleep(1)

        if interes == 4:
            tu1 = choice(tu)
            time.sleep(2)
            print(tu1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")
            time.sleep(1)

        if interes == 5:
            tenes1 = choice(tenes)
            time.sleep(2)
            print(tenes1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")     
            time.sleep(1)

        if interes == 6:
            fuiste1 = choice(fuiste)
            time.sleep(2)
            print(fuiste1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")         
            time.sleep(1)

        if interes == 7:
            donde1 = choice(donde)
            time.sleep(2)
            print(donde1)
            time.sleep(2)
            el_ella = input("\n>xx>-: ")
            time.sleep(1)

    def neurona_frontal(self):

        plasma0 = 0
        plasma1 = 0
        plasma2 = 0
        plasma3 = 0
        plasma4 = 0
        plasma5 = 0
        plasma6 = 0
        plasma7 = 0
        fracmentos = ["memoria1", "memoria2", "memoria3", "memoria4", "memoria5", "memoria6"]
          
        self.memoria_como = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 0:
            self.memoria_como[fracmentos[plasma0]] = el_ella
            plasma0 = plasma0 + 1

        self.memoria_cual = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 1:
            self.memoria_cual[fracmentos[plasma1]] = el_ella
            plasma1 = plasma1 + 1

        self.memoria_porque = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 2:
            self.memoria_porque[fracmentos[plasma2]] = el_ella
            plasma2 = plasma2 + 1

        self.memoria_astas = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 3:
            self.memoria_estas[fracmentos[plasma3]] = el_ella
            plasma3 = plasma3 + 1
        
        self.memoria_tu = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 4:
            self.memoria_tu[fracmentos[plasma4]] = el_ella
            plasma4 = plasma4 + 1
          

        self.memoria_tenes = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 5:
            self.memoria_tenes[fracmentos[plasma5]] = el_ella
            plasma5 = plasma5 + 1

        self.memoria_fuiste = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 6:
            self.memoria_fuiste[fracmentos[plasma6]] = el_ella
            plasma6 = plasma1 + 1
           

        self.memoria_donde = {
                      
                "memoria1":"",
                "memoria2":"",
                "memoria3":"",
                "memoria4":"",
                "memoria5":"",
                "memoria6":""

            }

        if interes == 7:
            self.memoria_donde[fracmentos[plasma7]] = el_ella
            plasma7 = plasma7 + 1







            
    def neurona_pariental(self):
        puntos = 1
        personalidad = 0
        palabras = ["auto", "autopista", "hospital", "lenguaje", "personalidad", "edificio", "computadora"]

        if personalidad == 0:         
            print("Vamos a jugar al AHOCARDO !° U °!\n ")
            print("Las reglas son faciles\n",
                  " *** Elijo una palabras\n",
                  " *** Tenes 5 intentos\n",
                  " *** A los tres puntos se define un ganador\n")
            palabras1 = choice(palabras)
            if palabras1 == "auto":
                print("La palabra con la que vamos a jugar es:  _u_o ")
                vueltas = "false"
                while vueltas == "false":
                    letra1 = input("\nTira una letra: >> ")

                    if letra1 == "a":
                        print("Muy bien encontraste la primera letra... vamos por la que falta")
                        print("\n- AU_O")

                        while vueltas == "false":
                            letra2 = input("\nTira una letra: >> ")

                            if letra2 == "o":
                                print("\nFelicidades ganaste !!!! ")
                                time.sleep(1)
                                print("\nLa palabra es  AUTO -!!")

                            if puntos == 3:
                                vueltas = "true"
                                time.sleep(1)
                                print("Perdiste :v 7u7r")

                            print("LETRA INCORRECTA !!!\n")
                            print("vas perdiendo", puntos, "puntos perdidos")
                            puntos = puntos + puntos
                    
                    if puntos == 3:
                        vueltas == "true"
                        time.sleep(1)
                        print("Perdiste :v 7u7r")

                    else:
                        print("LETRA INCORRECTA !!!\n")
                        print("vas perdiendo", puntos, "puntos perdidos")
                        puntos = puntos + puntos

          



        pass

            


alma = "true" 
print("Hola... ")
print("En que puedo ayudarte ?")

analicis_1 =["?", "¿", "como", "cual", "porque", "por que", "estas", "donde", "tu", "eres", "has", "fuiste", "tienes", "tenes"]
preguntas = ["Disculpa, puedo hacerte una pregunta? v(° u °)v", "Quiero aprender de vos, puedo hacerte una pregunta ? plisss (/° u °)/", "Me causas curiocidad, me toca a mi hacer una pregunta. (•◡•)/"]

while alma == "true":

    neurona4 = Neurona_Central(True)
    neurona4.neurona_pariental
        
    opcion = input("\n>>__: ")
    time.sleep(2)
    neurona1 = Neurona_Central(opcion)
    neurona1.neurona_occipital()    
    time.sleep(2)
    albedrio = randint(1,3)
    if albedrio == 1 or albedrio == 3:

        personal = choice(preguntas)
        print("\n__",personal)
        print("Si O No ? ")
        opcion2 = input("\n>>>>--: ")
        print("\n")

        if opcion2 == "SI" or opcion2 == "S" or opcion2 == "si" or opcion2 == "s":
            neurona2 = Neurona_Central(opcion2)
            neurona2.neurona_temporal()
            neurona3 = Neurona_Central(True)
            neurona3.neurona_frontal()
    
    
    
   

            
           
            


         
                    
                
             
                   


         
         
 

            





       
        


