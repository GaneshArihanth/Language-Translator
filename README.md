# 🌐 Language Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/React-19.x-blue?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6.x-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.x-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?logo=vercel&logoColor=white)](https://vercel.com/)

A modern, full-stack language translation application featuring a beautiful glassmorphism UI and dynamic background animations. Built with **React (Vite)** for the frontend and **Flask** for the backend, utilizing the **Google Translate API** via RapidAPI.


## ✨ Features

-   **🌍 Real-time Translation**: Translate text between 30+ supported languages instantly.
-   **🎨 Modern UI**: Stunning glassmorphism design with a "Gradients X Animations" background.
-   **⚡ High Performance**: Powered by Vite for lightning-fast frontend performance.
-   **📱 Fully Responsive**: Seamless experience across desktop, tablet, and mobile devices.
-   **🔌 Robust Backend**: Python Flask API handling secure communication with translation services.

## 🛠️ Tech Stack

### Frontend
-   **Framework**: React 19
-   **Build Tool**: Vite
-   **Styling**: Tailwind CSS v4
-   **UI Components**: Aceternity UI, Lucide React
-   **Animations**: CSS Keyframes & Canvas

### Backend
-   **Framework**: Flask
-   **Language**: Python 3
-   **Utilities**: Flask-CORS, Python-Dotenv
-   **API**: Google Translate API (RapidAPI)

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

-   **Node.js** (v18 or higher)
-   **Python** (v3.8 or higher)
-   **Git**

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/GaneshArihanth/Language-Translator.git
    cd Language-Translator
    ```

2.  **Backend Setup**
    ```bash
    # Create virtual environment
    python3 -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate  # Windows: venv\Scripts\activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

3.  **Frontend Setup**
    ```bash
    cd frontend
    npm install
    ```

## 🔑 Environment Variables

To run this project, you will need to add the following environment variables.

### Backend (`.env` in root)
Create a `.env` file in the root directory:
```env
RAPIDAPI_KEY=your_rapidapi_key_here
```
*Get your key from [RapidAPI Google Translate](https://rapidapi.com/googlecloud/api/google-translate1).*

### Frontend (`frontend/.env`)
Create a `.env` file in the `frontend` directory:
```env
VITE_API_URL=http://127.0.0.1:5000
```

## 🏃‍♂️ Usage

1.  **Start the Backend**
    ```bash
    # From root directory
    source venv/bin/activate
    python3 app.py
    ```
    Server runs at `http://127.0.0.1:5000`

2.  **Start the Frontend**
    ```bash
    # From frontend directory
    npm run dev
    ```
    App runs at `http://localhost:5173`

3.  **Translate!**
    -   Enter text in the input box.
    -   Select a target language.
    -   Click "Translate".

## ☁️ Deployment

This project is configured for seamless deployment on **Vercel**.

1.  Install Vercel CLI: `npm i -g vercel`
2.  Run `vercel` in the root directory.
3.  **Important**: Add `RAPIDAPI_KEY` to your Vercel Project Settings > Environment Variables.

*The `vercel.json` file handles the configuration for deploying both the Flask backend and React frontend together.*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️ by Ganesh Arihanth
</p>
