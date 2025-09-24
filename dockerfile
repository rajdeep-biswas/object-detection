# Python image and working directory
FROM python:3.12.11
WORKDIR /app

# Dependencies
COPY requirements.txt .
COPY yolov3u.pt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copy application code
COPY . .

# Expose Streamlit port and run app
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
