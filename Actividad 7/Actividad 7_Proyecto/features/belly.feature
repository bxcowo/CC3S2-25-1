# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en segundos
    Dado que he comido 20 pepinos
    Cuando espero 3600 segundos
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar muchísimo tiempo
    Dado que he comido 50 pepinos
    Cuando espero cinco horas, 45 minutos y 15 segundos
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos en muchísimos minutos y segundos
    Dado que he comido 8 pepinos
    Cuando espero 200 minutos y 145 segundos
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos enteros y partes de este en minutos
    Dado que he comido 9.5 pepinos
    Cuando espero 2000 minutos
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos enteros y partes de este en horas
    Dado que he comido 20.7512 pepinos
    Cuando espero tres horas
    Entonces mi estómago debería gruñir
