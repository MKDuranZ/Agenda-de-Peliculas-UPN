# Proyecto 1 - Mi Agenda de Películas

**Curso:** Informatica 1 
**Lenguaje:** Python  
**Institución:** Universidad Pedagógica Nacional  de Colombia

## Integrantes
* **Mark Durán Zona** 
* **Jeison Felipe Palomino Ulloa** 

## Descripción del Proyecto
Este proyecto es una aplicación de consola desarrollada en Python diseñada para administrar una agenda personal de películas. El sistema permite gestionar la información de 20 películas iniciales, permitiendo realizar consultas de duración, filtros por año de estreno, conteos por clasificación y gestión de horarios.

El desarrollo aplica conceptos fundamentales de programación como:
* Modelado de datos mediante **diccionarios**.
* Implementación de la técnica **"dividir y conquistar"** con funciones modulares.
* Lógica condicional compleja para la validación de reglas de negocio y cruces de horarios.
* Interacción con el usuario a través de menús en consola.

## Funcionamiento 
1. **Consultar película más larga:** Identifica automáticamente la cinta con mayor duración en minutos.
2. **Consultar duración promedio:** Calcula el tiempo medio de las películas agendadas y lo muestra en formato HH:MM.
3. **Buscar estrenos:** Filtra los nombres de las películas estrenadas después de un año ingresado.
4. **Contar películas 18+:** Determina la cantidad de contenido exclusivo para adultos en la agenda.
5. **Reagendar película:** Permite modificar el día y la hora de una película, validando que no se cruce con otra y respetando restricciones de género (ej. no dramas los viernes).
6. **Verificar invitación:** Evalúa si una persona puede ver una película según su edad, la clasificación de la cinta y el género (especialmente en terror y documentales).
7. **Búsqueda por nombre:** Encuentra y muestra toda la información de una película específica.
8. **Crear película:** Permite registrar nuevas películas de forma dinámica durante la ejecución del programa.

## Pruebas de Funcionamiento
## 1. **Consultar película más larga:**
   <img width="423" height="249" alt="image" src="https://github.com/user-attachments/assets/0592967f-2603-4779-a67b-13d6a1a00157" />
   
## 2. **Consultar duración promedio:**
   <img width="421" height="200" alt="image" src="https://github.com/user-attachments/assets/6f635db0-fddf-4915-a6d8-1f2c0655bb46" />

## 3. **Buscar estrenos:**
   <img width="601" height="246" alt="image" src="https://github.com/user-attachments/assets/8f08ba7e-765a-4943-bdb0-a8019148b6e4" />

## 4. **Contar películas 18+:**
   <img width="423" height="202" alt="image" src="https://github.com/user-attachments/assets/42d50647-62b4-49fc-889f-396a0ef65be5" />
   
## 5. **Reagendar película:**
   <img width="446" height="261" alt="image" src="https://github.com/user-attachments/assets/957357bf-59e4-4510-b6d9-8212e7e0e62e" />
   5.1. **No se deben programar documentales a las 10:00 p. m. o más tarde.**
   <img width="520" height="264" alt="image" src="https://github.com/user-attachments/assets/e407106f-bdfb-43c8-86a5-16843d37de31" />
   5.2. **No se deben programar dramas los viernes.**
   <img width="467" height="261" alt="image" src="https://github.com/user-attachments/assets/de4690d6-803f-484a-9db4-82312821db34" />
   5.3. **Entre semana no se deben programar películas que inicien a las 11:00 p. m. o más tarde, ni antes de las 6:00 a. m.**
   <img width="437" height="263" alt="image" src="https://github.com/user-attachments/assets/ebc6b5ba-cb0c-4c02-b616-c5c81c1acdff" />
   
## 6. **Verificar invitación:**
   6.1. **Los mayores de edad pueden ser invitados a cualquier película.**
   <img width="428" height="246" alt="image" src="https://github.com/user-attachments/assets/a79cb553-1aba-486e-83df-5638f1474db3" />
   6.2. **Los menores de 15 años no pueden ver películas de terror.**
   <img width="418" height="247" alt="image" src="https://github.com/user-attachments/assets/afcd1021-daef-48da-9286-2cc8d4a6ab60" />
   6.3. **Los invitados de 10 años o menos solo pueden ver películas de género familiar.**
   <img width="413" height="244" alt="image" src="https://github.com/user-attachments/assets/33d0a1dc-59cf-4850-9b9c-2a817ff54c01" />
   <img width="416" height="246" alt="image" src="https://github.com/user-attachments/assets/32c56cb9-177e-4eca-817b-db187cc61ed4" />
   6.4. **Si la edad no cumple la clasificación de la película, se requiere autorización de los padres, excepto en documentales.**
   <img width="417" height="248" alt="image" src="https://github.com/user-attachments/assets/f580f573-0665-4967-9da6-00eea8c7be77" />
   
## 7. **Búsqueda por nombre:**
   <img width="415" height="299" alt="image" src="https://github.com/user-attachments/assets/dfb3608a-060a-469a-a02f-0f2da30506be" />
   
## 8. **Crear película:**
   <img width="478" height="335" alt="image" src="https://github.com/user-attachments/assets/213c64c7-4d26-4206-ac5a-641b52e7630c" />
   









