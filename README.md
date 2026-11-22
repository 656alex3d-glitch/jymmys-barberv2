# 💈 JYMMY'S BARBER - Agenda de Citas, Barberos & Cortes de Moda

Aplicación web profesional para **Jymmy's Barber** con estética **Negro con Neones (Cian, Rojo, Dorado)**, sonidos de tijeras y caja registradora (Web Audio API), bloqueo de seguridad por roles, gestor dinámico de barberos, gestor de cortes de moda y punto de venta con ticket térmico.

---

## ✂️ Novedades Recientes

### 1. Gestor de Barberos del Equipo (Panel Admin)
- Ahora puedes **cambiar los nombres de los barberos existentes**, agregar nuevos barberos y eliminar los que ya no laboren.
- Puedes asignarle a cada barbero su:
  - **Nombre completo** (ej: *Jymmy Master, Carlos Fade, Alex Scissors, etc.*).
  - **Especialidad o Títulos** (ej: *Especialista en Taper & Fade, Barbas Deluxe, etc.*).
  - **Avatar / Emoji representativo** (✂️, 💈, 🪒, 👑, 🔥, ⚡, 😎).
  - **Color de distintivo neón** (Dorado, Cian, Rojo, Verde, Morado).
- Al guardar o editar un barbero, **se actualiza al instante en la agenda de los clientes**.

### 2. Cortes de Moda & Tendencias Urbanas Precargados
Ya vienen integrados los cortes más pedidos actualmente, con opción de modificar sus precios o agregar nuevos cortes en 1 clic:
- ✂️ **Taper Fade (Low / Mid / High)**: Desvanecido moderno en sienes y nuca con caída superior.
- 💈 **Mullet Moderno / Burst Fade**: Tendencia urbana con degradado circular en orejas y nuca texturizada.
- ✂️ **French Crop Texturizado**: Flequillo frontal recto con desvanecido alto y textura.
- 🪒 **Buzz Cut + Diseño / Greca**: Rapado degradado con líneas o figuras a navaja libre.
- ✂️ **Mid Fade con Pompadour / Quiff**: Tupé estilizado con desvanecido medio pulido.
- 🪒 **Skin Fade a Navaja Cero**: Desvanecido ultra rasurado con shaver eléctrica o navaja clásica.
- ✂️ **Wolf Cut Barber Edition**: Capas degrafiladas con tijera dentada, estilo rebelde con volumen.
- 👑 **Combo Corte + Barba Deluxe**: Corte completo, toalla caliente al vapor, aceites y perfilado.
- 🧔 **Barba Vikinga & Vapor de Ozono**: Recorte de volumen, navaja, toalla caliente y bálsamo.
- ⚡ **Platinado / Decoloración Neón**: Matizado blanco plata o mechas urbanas.
- 🖤 **Mascarilla Negra & Exfoliación Facial**: Limpieza profunda de poros y tónico refrescante.

---

## 🔒 Credenciales del Sistema

- **Cliente Normal**: Solo puede ver la Agenda para apartar su cita. No ve el POS ni el Panel Admin.
- **Trabajadores / POS**:
  - **Usuario**: `Jymmys`
  - **Contraseña**: `123321` *(Modificable por el Administrador)*
  - Acceso para cobrar y generar tickets.
- **Administrador Maestro**:
  - **Usuario**: `admin`
  - **Contraseña**: `1234` *(Modificable desde el panel)*
  - Acceso total para cambiar precios, crear cortes, gestionar barberos, cambiar contraseñas y corte de caja.

---

## 🚀 Despliegue con URL Limpia y 100% Gratis (Sin Firebase ni Netlify)

- **Vercel** ([vercel.com](https://vercel.com)): Sube la carpeta y nómbrala `jymmys-barber` para obtener gratis `https://jymmys-barber.vercel.app`.
- **Cloudflare Pages** ([pages.cloudflare.com](https://pages.cloudflare.com)): Subida directa arrastrando el archivo para obtener gratis `https://jymmysbarber.pages.dev`.
