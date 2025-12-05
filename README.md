# Language Translator

A modern, full-stack language translation application featuring a beautiful glassmorphism UI and dynamic background animations. Built with React (Vite) for the frontend and Flask for the backend, utilizing the Google Translate API via RapidAPI.

## Features

-   **Real-time Translation**: Translate text between 30+ supported languages.
-   **Modern UI**: Glassmorphism design with a stunning, interactive gradient background animation.
-   **Responsive Design**: Fully responsive interface that works on all devices.
-   **Full Stack**: React frontend communicating with a Python Flask backend.

## Tech Stack

-   **Frontend**: React, Vite, Tailwind CSS v4, Aceternity UI, Lucide React.
-   **Backend**: Python, Flask, Flask-CORS.
-   **API**: Google Translate API (via RapidAPI).

## Prerequisites

-   Node.js (v18 or higher)
-   Python (v3.8 or higher)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Language-Translator
```

### 2. Backend Setup

1.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  Install Python dependencies:
    ```bash
    pip install flask flask-cors requests python-dotenv
    ```

3.  Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```

4.  Add your RapidAPI key to `.env`:
    ```env
    RAPIDAPI_KEY=your_rapidapi_key_here
    ```

5.  Start the backend server:
    ```bash
    python3 app.py
    ```
    The backend will run on `http://127.0.0.1:5000`.

### 3. Frontend Setup

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install Node dependencies:
    ```bash
    npm install
    ```

3.  Create a `.env` file in the `frontend` directory:
    ```bash
    touch .env
    ```

4.  Add the backend API URL to `.env`:
    ```env
    VITE_API_URL=http://127.0.0.1:5000
    ```

5.  Start the development server:
    ```bash
    npm run dev
    ```
    The frontend will run on `http://localhost:5173` (or similar).

## Usage

1.  Open the frontend URL in your browser.
2.  Enter the text you want to translate in the "Original Text" box.
3.  Select the target language from the dropdown menu.
4.  Click the "Translate" button.
5.  View the result in the "Translated Text" box.

## Deployment

The project is configured for deployment on Vercel using the `vercel.json` configuration file.

1.  Install Vercel CLI: `npm i -g vercel`
2.  Run `vercel` in the root directory.
3.  Set the `RAPIDAPI_KEY` environment variable in your Vercel project settings.

## License

MIT
