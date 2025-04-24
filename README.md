# python-week2

## Grok 3 Web App with Flask & FastAPI

This project demonstrates how to build a simple web chat app using:

- Python
- Flask (main web interface)
- FastAPI (bonus modern API framework)
- OpenAI API (Grok 3)

## Installation

```bash
pip install -r requirements.txt
```

Set your API key in a .env file:

```
XAI_API_KEY=your_key
```

## Usage

**Run with Flask**

```
python app.py
```

Visit: http://127.0.0.1:5000

**Run with FastAPI**

```
uvicorn app_fastapi:app --reload
```

Visit Swagger UI: http://127.0.0.1:8000/docs
