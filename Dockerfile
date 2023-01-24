FROM python:3.9

# Add your dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add your .env file
COPY .env .

COPY src/ /src/

# Add your main.py file
COPY main.py .

# Run the bot
CMD ["python3", "main.py"]