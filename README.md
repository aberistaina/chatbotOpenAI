# 🤖 **Chatbot OpenAI**

> Un chatbot basado en OpenAI GPT-3.5, diseñado para interactuar con los usuarios y responder preguntas. Utiliza Flask para el backend y permite una fácil integración con OpenAI a través de una API key.

---

## 📋 **Tabla de Contenidos**

- [✨ Características](#-características)
- [💻 Instalación](#-instalación)
- [🔧 Uso](#-uso)
- [⚙️ Tecnologías](#-tecnologías)
- [🔑 Variables de Entorno](#-variables-de-entorno)
- [👥 Autores](#-autores)


---

## ✨ **Características**

- 🤖 **Interacción con el usuario**: El chatbot responde a los mensajes del usuario utilizando el modelo GPT-3.5 de OpenAI.
- 🔄 **API flexible**: Permite personalizar el comportamiento del asistente ajustando el contenido del "prompt" en el archivo `prompt.py`.
- 🌍 **Compatibilidad CORS**: Habilita la comunicación entre el servidor Flask y cualquier frontend.

---

## 💻 **Instalación**

Para poner en marcha este proyecto en tu máquina local, sigue estos pasos:

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/aberistaina/chatbotOpenAI.git
2. Navega al directorio del proyecto:
    ```bash
    cd chatbotOpenAI
3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
4. Activa el entorno virtual:

      En Windows:
   
         venv\Scripts\activate
   
      En Linux:
   
         source venv/bin/activate

6. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
7. Crea un archivo .env en el directorio raíz y agrega tu clave API de OpenAI:
   ```bash
   OPENAI_API_KEY=tu_clave_api_de_openai
8. Ejecuta el servidor Flask
   ```bash
   python app.py
El servidor debería iniciarse en http://127.0.0.1:5000/.


## 🔧 **Uso**

### Realizar una solicitud de chat:
Para interactuar con el chatbot, realiza una solicitud POST a la ruta `/chat` con el siguiente formato JSON:

      {
        "message": "Tu mensaje aquí"
      }

## ⚙️ **Tecnologías**

Este proyecto está construido con las siguientes tecnologías:

- 🐍 **Python**: Lenguaje de programación utilizado.
- 🧑‍💻 **Flask**: Framework para el backend.
- 🌐 **OpenAI GPT-3.5**: Modelo utilizado para generar respuestas de chat.
- 🔑 **OpenAI API**: Se requiere una clave API para usar el modelo de OpenAI.
- 🌍 **CORS**: Para permitir solicitudes desde cualquier origen.

## 🔑 **Variables de Entorno**

Este proyecto requiere una clave API de OpenAI para funcionar. Crea un archivo `.env` en el directorio raíz y agrega la siguiente variable:

   ```bash
   OPENAI_API_KEY=tu_clave_api_de_openai

## 👥 **Autores**

- Alejandro Beristain - [@aberistaina](https://github.com/aberistaina)


