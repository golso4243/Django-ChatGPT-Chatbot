from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')


def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')

        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
        )
        return render(request, 'home.html', {'question': question, 'response': response.choices[0].message.content})
    return render(request, 'home.html', {})
