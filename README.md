# FoodyBA – Trabajo Práctico Final FIUBA

## Descripción del proyecto

**FoodyBA** es una aplicación web donde los usuarios podrán buscar restaurantes, consultar reseñas realizadas por otros y dejar sus propias opiniones y calificaciones. La plataforma está pensada para ser intuitiva y funcional, permitiendo a cualquier usuario encontrar lugares para comer según criterios como tipo de comida, ubicación o calificación.

Además, ofrece herramientas a los comerciantes para administrar su restaurante, recibir reservas y acceder a estadísticas útiles, mejorando su visibilidad y conexión con potenciales clientes.

Este proyecto se desarrolla como trabajo práctico integrador de la materia **Introducción al Desarrollo de Software (FIUBA)**, siguiendo una metodología ágil basada en tareas asignadas en un tablero Kanban, control de versiones con GitHub y entregas progresivas que generen valor funcional.

---

## Objetivos del proyecto

* Brindar a los usuarios una herramienta para descubrir y calificar restaurantes.
* Fomentar la interacción entre usuarios a través de reseñas y reservas.
* Facilitar a los comercios la gestión online de su presencia gastronómica.
* Aplicar conocimientos adquiridos en el curso (backend, frontend, base de datos, trabajo en equipo).
* Presentar un proyecto funcional, organizado y bien documentado.

---

## Progreso final del proyecto

* ✅ Proyecto definido y planificado
* ✅ Mockup visual completo
* ✅ Backlog en Trello con tareas divididas por integrante
* ✅ Rutas de autenticación para consumidores y comercios
* ✅ Sistema de reservas con validación por día y horario
* ✅ Perfiles diferenciados para cada tipo de usuario
* ✅ Reseñas con sistema de calificación y comentarios
* ✅ Sistema de favoritos funcional
* ✅ Filtros de búsqueda por cocina, etiquetas, días, horarios y calificación
* ✅ Mapa integrado para visualizar ubicación de restaurantes
* ✅ Documentación técnica completa
* ✅ Testing y verificación de funcionalidades

---

## Herramientas utilizadas

* **Backend**: Flask (Python)
* **Base de datos**: MySQL
* **Frontend**: HTML, CSS, Jinja, JavaScript
* **Mapas**: Leaflet/OpenStreetMap
* **Calendario para reservar**: Flatpickr
* **Control de versiones**: GitHub
* **Organización del trabajo**: Trello (Kanban)

---
## Solución propuesta

Para satisfacer la necesidad de los usuarios de encontrar y calificar restaurantes de una manera simple, desarrollamo FoodyBA como una plataforma que conecta consumidor y comercios. Nuestra solución permite a los usuarios buscar restaurantes mediante filtros avanzados, consultar reseñas, dejar opiniones y gestionar reservas en tiempo real. Desde el aspecto de los comercios pusimos el foco en diseñar una plataforma que permita a cualquier comerciante, desde el pequeño hasta el más grande, administrar su presencia, tanto como recibir reservas y acceder a estadísticas útiles para potenciar su negocio. Se integraron mapas y la capacidad de diferenciar perfiles para enriquecer la experiencia.

* Diferenciacion de tipos de usuario
  Se pudo realizar esta implementacion gracias al objeto **session** el cual es brindado por el framework Flask. Al utilizar el mismo el backend puede identificar el tipo de usuario que realiza cada accion y responde acorde a los permisos y funcionalidad asignadas a cada usuario.
  <u>Funcionalidades asignadas a cada tipo de usuario</u>
  _Usuario consumidor_:Capacidad de tener comercios favoritos, realizar reservas y reseñas.
  _Usuario comercio_: Visualizar las reseñas y las reservas realizadas a su establecimiento. El mismo tambien puede elminar las reservas que quiera, como tambien acceder al QR que le permite a un usuario consumidor confirmar su reserva

---

## Integrantes del equipo

* Lucio Osvaldo Frete
* Kennia Vázquez Gamarra
* Matías Ariel Sapienza
* Rocco Grassano Barbieri
* Santiago del Monaco

---

## Conclusion final

FoodyBA no solo fue una oportunidad para aplicar lo aprendido, sino también una experiencia que nos acercó al trabajo real en equipo dentro del desarrollo de software. A lo largo del proyecto enfrentamos desafíos técnicos y de organización que pudimos superar colaborando, escuchándonos y adaptándonos constantemente. Ver la plataforma funcionando, con todas sus funcionalidades integradas, fue una gran satisfacción que nos mostró cuánto crecimos desde el primer día. Este trabajo no solo consolidó nuestros conocimientos técnicos, sino también nuestras habilidades para trabajar juntos con responsabilidad, compromiso y creatividad. Nos llevamos no solo un proyecto completo, sino también un aprendizaje que va más allá del código.

---
