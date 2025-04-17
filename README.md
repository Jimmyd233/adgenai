# AdGenAI: Generative AI for Personalized Advertisement Creation

AdGenAI is a prototype web application that demonstrates how Large Language Models (LLMs) and generative image synthesis can be used to automate the creation of personalized advertising content. Built with Flask and integrated with DeepSeek-Chat and DeepAI APIs, the system enables users to generate high-quality ad copy and visuals tailored to specific products, tones, platforms, and visual styles.

---

## 🚀 Features

- ✍️ Generates personalized ad copy using DeepSeek-Chat (LLM)
- 🖼 Creates corresponding ad visuals using DeepAI’s Stable Diffusion XL API
- ♻ Supports multiple tones, platforms, art styles, and compositions
- ⚡ Asynchronous parallel generation (copy and image) with `ThreadPoolExecutor`
- 📋 Optional advanced settings: color palette, text overlay position
- 📜 Logs anonymized inputs and outputs for academic auditing

---

## 📁 Project Structure

```plaintext
adgenai_web/
├── app.py                 # Main application (Flask controller)
├── .env                   # API keys (not included; create your own)
├── templates/
│   ├── index.html         # User input form
│   └── result.html        # Display results (ad copy + image)
├── static/
│   └── style.css          # Basic UI styling
```

---

## ⚙️ Dependencies

Install these using `pip install -r requirements.txt` or manually:

- Flask==3.0.2
- openai==0.28.1  *(for DeepSeek-Chat integration)*
- requests==2.31.0 *(for DeepAI image API calls)*
- python-dotenv==1.0.0 *(to securely manage API keys)*
- Pillow==10.1.0 *(optional: image metadata validation)*
- rouge==1.0.1 *(optional: text evaluation)*

---

## 🔑 Setup & Configuration

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/adgenai_web.git
cd adgenai_web
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the root directory:**

```ini
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPAI_API_KEY=your_deepai_api_key
```

5. **Run the application locally:**

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🧪 Sample Prompts

Try inputs like:

- **Product:** Smart Fitness Band  
- **Audience:** Busy young professionals  
- **Tone:** Friendly  
- **Platform:** Instagram  
- **Art Style:** Minimalism  
- **Picture Composition:** Close-up  

---

## 📝 Notes

- Make sure your API keys are valid and have enough quota.
- DeepAI image generation may take 10–15 seconds on average.
- Use responsibly — no NSFW prompts or sensitive data allowed.

---

## 📜 License

This project is released for educational purposes under the MIT License.

---

## 📬 Contact

For questions or academic evaluation, please reach out to:

**Student Name:** DING Haoran  
**Project:** Personalized Ads AI Intelligent Generation  
**Institution:** City University of Hong Kong