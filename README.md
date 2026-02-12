---
title: YOLO26 Camera Demo
emoji: 📹
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.38.0"
python_version: "3.12"
app_file: app.py
pinned: false
---

# YOLO26

A real-time object detection demo using the YOLO26 nano model. This Streamlit web application uses your webcam to detect objects in real-time, demonstrating state-of-the-art computer vision in an interactive format.

This repository includes everything you need to run the demo locally in GitHub Codespaces and deploy it to Hugging Face Spaces.

## Activity goals

1. Successfully deploy the YOLO26 web app to HuggingFace.
2. **Challenge:** Add a confidence threshold slider to the app sidebar that lets users filter detections based on confidence score (hint: use `st.sidebar.slider()` and pass the `conf` parameter to `model.predict()`)
3. **Challenge:** Display a live count of detected objects grouped by class below the video feed (hint: iterate through `results[0].boxes` to access detection data including class names and counts)

## Getting Started

### 1. Create Hugging Face account and Space

- Create a Hugging Face account:
  - Go to https://huggingface.co/join and create a new account
  - Verify your email if prompted

- Create a new Space:
  - Go to https://huggingface.co/spaces and select "Create new Space"
  - Fill in the form:
    - Owner: your username
    - Space name: yolo26-demo (or any name you want)
    - License: choose any
    - SDK: Docker -> Streamlit
    - Space visibility: Public (recommended for first try)
  - Select "Create Space"

- Create an access token:
  - Go to https://huggingface.co/settings/tokens
  - Create a new token with write permissions
  - Copy the token (you'll need it in the next step)

### 2. Fork repository and add token secret

- Fork this repository:
  - Click the "Fork" button at the top right of this page
  - This creates a copy in your GitHub account

- Add the Hugging Face token as a Codespaces secret:
  - In your forked repo, go to Settings → Secrets and variables → Codespaces
  - Create a new secret named `HF_TOKEN` and paste your token

### 3. Start Codespace and try the app

- Create a Codespace:
  - In your forked repo, click the green "Code" button
  - Select the "Codespaces" tab
  - Click "Create codespace on main"
  - Wait for the environment to build (this installs all dependencies automatically)

- Run the Streamlit app:
  - Once the Codespace is ready, open a terminal and run:

    ```bash
    streamlit run app.py
    ```

  - The app will open in a new browser tab automatically
  - Grant camera permissions when prompted to test object detection

### 4. Deploy to Hugging Face Space

- Add the Space as a git remote:

  ```bash
  git remote add hf https://YOUR_HF_USERNAME:$HF_TOKEN@huggingface.co/spaces/<your-username>/<your-space-name>
  ```

- Push to the Space (force required for first push):

  ```bash
  git push hf main --force
  ```

  - You only need `--force` on the first push
  - The Space will build automatically. Open the "App" tab once it finishes

## Troubleshooting

- If the Space build fails, open the "Logs" tab to see the error
- Common issue: missing system libraries. If you see a libGL error, add a file named `packages.txt` with a single line:
  ```
  libgl1
  ```
  Then commit and push again to trigger a rebuild

### WebRTC Camera Issues on Hugging Face Spaces

**Note:** WebRTC (webcam streaming) may not work reliably on Hugging Face Spaces due to networking restrictions and asyncio event loop limitations in the cloud environment. You may see errors like "AttributeError: 'NoneType' object has no attribute 'sendto'" in the logs.

**Recommended workflow:**
- Use **GitHub Codespaces** for testing the webcam/camera features (works reliably)
- Deploy to **Hugging Face Spaces** for portfolio/sharing purposes, but be aware webcam functionality may be limited
- The Space deployment demonstrates your ability to containerize and deploy ML applications, even if WebRTC doesn't fully work