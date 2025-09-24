# What this app runs on
I have used Streamlit, which uses Flask under the hood. This is to simplify the UI Building process, as well as to host an endpoint for the YOLO model - two goals with one solution.  

# Design notes
I have kept both Streamlit and YOLO code in a single file. Logically separating the model and API serving in separate files is an easy change, which however, I am skipping in this version to move fast with the main scope.  

I have chosen not to dump the image and json files locally, at this moment, but that is one easy change if needed.  

I haven't uploaded the model weights file to the repo, or configured docker for its inclusion to work around potential Git LFS issues when trying to replicate this project, or having to download the file yourself. The tradeoff: this results into a one-time load_model() call when the first ever detection is performed.  

My goal with this project has been to showcase the core functionality. Further improvements could be made on the directory structure and logic segregation.

# I/O
Users upload one image at a time into the UI, and they get back two results on the UI:
1. Image with bounding boxes.
2. Structured JSON results.

# Running the App
Make sure Docker is running on your system.

Use `docker buildx build --platform=linux/amd64 -t yolo-app .` to build an image.

Use `docker run -p 8501:8501 yolo-app` to run the container locally.

Use URL `https://localhost:8501` to try out the application on a browser.

Alternatively, you can create a new venv, install dependencies from requirements.txt and run `streamlit run app.py` to get started faster.
