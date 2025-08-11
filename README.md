🧮 MathLensAi
A web-based application that leverages AI to extract, understand, and explain mathematical content from user-uploaded images. Built with Python and Flask, MathLensAi allows users to upload math problem images and receive step-by-step solutions powered by modern language models.

📌 Overview
MathLensAi is designed for students, educators, and lifelong learners seeking instant, in-depth explanations of mathematical problems directly from images. It combines image upload, text extraction, and AI-driven reasoning to demystify even challenging equations—right from your browser.

🚀 Features
Image Upload: Drop or select math problem images for processing

Optical Character Recognition (OCR): Extracts mathematical text from images

AI Reasoning: Uses LLMs to parse and solve extracted math content

Step-by-Step Solutions: Returns detailed answers and explanations

Easy Access: Hosted on Vercel for seamless deployment and use

📁 Project Structure
app.py – Main Flask application; handles requests and UI routing

extraction.py – Manages OCR and math text extraction pipeline

llm_response.py – Connects with LLM to parse and solve extracted expressions

templates/ – HTML templates for web frontend

user_images/ – Directory for uploaded images (session-based)

requirements.txt – All Python dependencies

⚙️ Installation
Prerequisites
Python 3.8+

Required packages from requirements.txt

(Optional) Vercel CLI for cloud deployment

Local Setup
bash
git clone https://github.com/Anikait04/MathLensAi.git
cd MathLensAi

# Create virtual environment (recommended)
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the Flask app
python app.py
Visit http://127.0.0.1:5000 in your browser.

🌐 Usage
Go to the app (locally or at: math-lens-ai.vercel.app)

Upload an image containing a math problem

The app extracts, parses, and solves the problem

View the solution and steps on screen

🛠 Technologies
Python 3

Flask – Web server and API framework

OCR Library (e.g., Tesseract via pytesseract or similar)

LLM Integration – Language model for reasoning

HTML/CSS for frontend templating

🚧 Roadmap / Future Improvements
Enhanced OCR for handwritten math

Support for multi-step and word problems

User accounts and solution history

API integration for mobile app support

UI/UX polish and real-time feedback

📜 License
This project is licensed under the MIT License. See the LICENSE file for more information.

🙏 Acknowledgements
OpenAI and Hugging Face for language models

Pytesseract for image-to-text extraction

Vercel for easy cloud deployment

Author: Anikait

Have a difficult math problem? Just snap, upload, and get learning with MathLensAi!
