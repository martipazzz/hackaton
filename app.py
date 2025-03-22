nombre=input("Hola, ¿Cuál es tu nombre?")
print(f"¡Bienvenid@ {nombre}!")
print("Por favor, para las siguientes preguntas, escribe sólo una alternativa (ej: A, B, C, D)")
curso=input("¿En qué curso te encuentras?\nA. 7° y 8° Básico\nB. 1° y 2° Medio\nC. 3° y 4° Medio\n")
materia=input("¿Qué materia quieres estudiar hoy?\nA. Matemática\nB. Lenguaje\nC. Historia\n D. Ciencias\n")
horas=input("¿Cuántas horas de estudio puedes dedicarle?\nA. Menos de 1 hora\nB. 1-2 horas\nC. 2-3 horas\n")
metodo=input("¿Cómo se te hace más sencillo aprender?:\nA. Leyendo u Observando \nB. Escribiendo o Hablando\nC. Escuchando\n")

#----------------MATERIA A MATEMATICA
if materia=="A": #Matemática
  if horas=="A": # Menos de 1 hora
    if metodo=="A": #Leyendo/Observando
        print("Según tus respuestas, te recomendamos:\nEjemplos resueltos: Se observan ejercicios ya resueltos y se sigue el paso a paso para entender el procedimiento. Esta técnica ayuda a visualizar la aplicación de fórmulas y métodos matemáticos.")
    elif metodo=="B":#Escribiendo/Hablando
      print("Según tus respuestas, te recomendamos:\nResolver ejercicios básicos: Realizar ejercicios sencillos sobre el tema, enfocándose en comprender cada paso. Escribir cada operación ayuda a reforzar el aprendizaje.")
    elif metodo=="C": #Escuchando
      print("Según tus respuestas, te recomendamos:\nVideos explicativos cortos: Escuchar explicaciones en video sin mirar la pantalla y tratar de imaginar los pasos en la mente. Luego, intentar resolver un problema similar basándose en lo que se ha escuchado.")
  elif horas=="B": #1-2 horas
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos:\nMapas de fórmulas: Se elaboran esquemas con las fórmulas más importantes y sus aplicaciones. Relacionarlas con ejemplos facilita su memorización y uso en ejercicios.")
    elif metodo=="B": #Escribiendo/Hablando
        print("Según tus respuestas, te recomendamos:\nExplicar por escrito: Escribir una explicación detallada sobre un problema matemático difícil, describiendo cada paso como si se estuviera enseñando a otra persona. Esto ayuda a estructurar el pensamiento lógico. ")
    elif metodo=="C": #Escuchando
        print("Según tus respuestas, te recomendamos:\nEscuchar problemas resueltos y visualizar mentalmente: Escuchar la resolución de un problema matemático sin ver la pantalla e intentar imaginar los pasos en la mente. Luego, comprobar si la solución mental coincide con la real. ")
  elif horas=="C":#2-3+ horas
    if metodo=="A": #Leyendo/Observando
        print("Según tus respuestas, te recomendamos:\nResolución de problemas aplicados: Trabajar en ejercicios que tengan aplicaciones en la vida real, como cálculos financieros o mediciones. Relacionar los problemas con situaciones prácticas mejora la comprensión.")
    elif metodo=="B":#Escribiendo/Hablando
        print("Según tus respuestas, te recomendamos:\nTécnica Pomodoro: Se estudia en ciclos de 25 minutos de concentración, seguidos de 5 minutos de descanso. Después de cuatro ciclos, se toma un descanso más largo. Este método mejora la productividad y el enfoque.")
    elif metodo=="C": #Escuchando
        print("Según tus respuestas, te recomendamos:\nEstudio en grupo con discusión: Escuchar a otras personas explicando problemas matemáticos y participar en discusiones sobre las soluciones. Esto permite ver diferentes enfoques y aclarar dudas. ")
#----------------MATERIA B LENGUAJE
elif materia=="B":
  if horas=="A": # Menos de 1 hora
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos:\nLectura rápida + Resúmenes visuales: Consiste en leer rápidamente un texto sin detenerse en cada palabra, buscando captar la idea principal. Luego, se crean mapas conceptuales, esquemas o dibujos que representen lo más importante del texto. Esto ayuda a procesar la información sin perder tiempo en detalles innecesarios.")
    elif metodo=="B":#Escribiendo/Hablando
        print("Según tus respuestas, te recomendamos:\nEscritura libre + Resumen corto: Escribir lo que se recuerda sin mirar el texto, tratando de explicarlo con palabras propias. Luego, se hace un pequeño resumen con las ideas clave. Esta técnica fortalece la memoria y mejora la comprensión al obligar al cerebro a estructurar la información.")
    elif metodo=="C": #Escuchando
        print("Según tus respuestas, te recomendamos:\nAudiolibros + Pódcast: Escuchar un audiolibro o un pódcast sobre el tema mientras se realiza otra actividad como caminar o descansar. Para reforzar la comprensión, se puede intentar resumir en la mente lo más importante de lo escuchado. Usar una velocidad de reproducción más rápida ayuda a mantener la concentración.")
  elif horas=="B": #1-2 horas
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos:\nMétodo SQ3R (Survey, Question, Read, Recite, Review): Se basa en cinco pasos: 1) Explorar el texto por encima para captar la idea general. 2) Formular preguntas sobre el contenido. 3) Leer detenidamente en busca de respuestas. 4) Repetir en voz alta o escribir lo más importante. 5) Revisar y repasar lo aprendido. Este método mejora la comprensión y la retención a largo plazo.")
    elif metodo=="B":#Escribiendo/Hablando
      print("Según tus respuestas, te recomendamos:\nMétodo Cornell: Consiste en dividir una hoja en tres secciones: una columna estrecha a la izquierda para palabras clave, una columna más ancha a la derecha para notas detalladas y un espacio en la parte inferior para un resumen general. Esta estructura facilita la organización de la información y el repaso posterior.")
    elif metodo=="C": #Escuchando
      print("Según tus respuestas, te recomendamos:\nEscuchar resúmenes y repetir mentalmente: Buscar resúmenes en formato de audio y escucharlos atentamente. Luego, tratar de repetir mentalmente las ideas clave o explicarlas en voz alta. Esto refuerza la comprensión auditiva y ayuda a fijar la información en la memoria.")
  elif horas=="C":#2-3+ horas
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos:\nAnálisis literario + Mapas mentales: Consiste en leer un texto con profundidad, analizando personajes, ideas principales y mensajes del autor. Luego, se usa un mapa mental para conectar conceptos, estableciendo relaciones entre ellos. Esto facilita la comprensión y ayuda a recordar los detalles importantes. ")
    elif metodo=="B":#Escribiendo/Hablando
       print("Según tus respuestas, te recomendamos:\nTécnica Feynman (escribir para entender): Se elige un concepto y se escribe sobre él como si se estuviera explicando a un niño. Se identifican las partes confusas y se vuelve a escribir de forma más clara. Esto ayuda a detectar lagunas en el conocimiento y a mejorar la comprensión.")
    elif metodo=="C": #Escuchando
       print("Según tus respuestas, te recomendamos:\nClub de lectura o audioclases: Escuchar audioclases sobre el tema o participar en un club de lectura en el que se discuten libros y textos. La interacción con otras personas permite reflexionar sobre lo aprendido y reforzar la comprensión.")


  #----------------MATERIA C HISTORIA
elif materia=="C":
  if horas=="A": # Menos de 1 hora
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos:")
    elif metodo=="B":#Escribiendo/Hablando
        print("Según tus respuestas, te recomendamos: ")
    elif metodo=="C": #Escuchando
        print("Según tus respuestas, te recomendamos: ")
  elif horas=="B": #1-2 horas
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos: ")
    elif metodo=="B":#Escribiendo/Hablando
      print("Según tus respuestas, te recomendamos: ")
    elif metodo=="C": #Escuchando
        print("Según tus respuestas, te recomendamos: ")
  elif horas=="C":#2-3+ horas
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos: ")
    elif metodo=="B":#Escribiendo/Hablando
      print("Según tus respuestas, te recomendamos: ")
    elif metodo=="C": #Escuchando
      print("Según tus respuestas, te recomendamos: ")

  #----------------MATERIA D CIENCIAS
elif materia=="D":
  if horas=="A": # Menos de 1 hora
    if metodo=="A": #Leyendo/Observando
      print("Según tus respuestas, te recomendamos: ")
    elif metodo=="B":#Escribiendo/Hablando
      print("")
    elif metodo=="C": #Escuchando
      print("")
  elif horas=="B": #1-2 horas
    if metodo=="A": #Leyendo/Observando
      print("")
    elif metodo=="B":#Escribiendo/Hablando
      print("")
    elif metodo=="C": #Escuchando
      print("")
  elif horas=="C":#2-3+ horas
    if metodo=="A": #Leyendo/Observando
      print("")
    elif metodo=="B":#Escribiendo/Hablando
      print("")
    elif metodo=="C": #Escuchando
      print("")

  
