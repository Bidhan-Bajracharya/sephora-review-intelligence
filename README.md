# Sephora Review Intelligence

**Sephora Review Intelligence** is an end-to-end project that applies **sentiment analysis** on Sephora product reviews using a **BERT** model and visualizes insights through an interactive **Dash** web application.

This app allows users to analyze customer feedback, understand sentiment distribution, and explore product performance intuitively.

<br/>

## 🗂️ Project Structure

```
sephora-review-intelligence/
│
├── app/
│   ├── assets/               # Static assets (CSS, images, logos)
│   ├── pages/
│   │   ├── dashboard.py       # Dashboard page: data visualizations
│   │   ├── homepage.py        # Landing/Home page
│   │   ├── login.py           # Login page (simple authentication setup)
│   │   ├── sentiment.py       # Sentiment analysis input and results
│   ├── main.py                # Main entry point to run the Dash app
│
├── .gitignore                # Static files (screenshots)
├── .gitignore                # Git ignore file
├── requirements.txt          # Project dependencies
├── README.md                  # Project overview and setup instructions
```

<br/>

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Bidhan-Bajracharya/sephora-review-intelligence.git
cd sephora-review-intelligence
```

2. **Install the required packages**

```bash
pip install -r requirements.txt
```

<br/>

## ▶️ Running the App

Once installed, start the app by running:

```bash
cd app
python main.py
```

The application will launch locally at:  
`http://127.0.0.1:8050/`

<br/>

## 📸 Screenshots

![](https://github.com/Bidhan-Bajracharya/sephora-review-intelligence/blob/main/static/p1.png)
![](https://github.com/Bidhan-Bajracharya/sephora-review-intelligence/blob/main/static/p2.png)
![](https://github.com/Bidhan-Bajracharya/sephora-review-intelligence/blob/main/static/p3.png)
![](https://github.com/Bidhan-Bajracharya/sephora-review-intelligence/blob/main/static/p4.png)
![](https://github.com/Bidhan-Bajracharya/sephora-review-intelligence/blob/main/static/p5.png)

<br/>

## 🙏 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Sephora Product Dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews)

---
