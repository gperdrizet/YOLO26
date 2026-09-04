# YOLO26: live object detection activity

A real-time object detection activity using the YOLO26 nano model. This Streamlit web application uses your webcam to detect objects in real-time, demonstrating state-of-the-art computer vision in an interactive format.

This repository includes everything you need to run the app locally in GitHub Codespaces and deploy it to Streamlit Community Cloud.

Check out a live deployment on [Streamlit Community Cloud]([https://yolo26.streamlit.app](https://yolo26-n7mx7s8vdxr2hxncchjvzs.streamlit.app/))

For a deep dive into how YOLO26 works under the hood, see: Hidayatullah, P., & Tubagus, R. (2026). [*YOLO26: A Comprehensive Architecture Overview and Key Improvements*](https://arxiv.org/abs/2602.14582). arXiv:2602.14582.

## Activity goals

1. Successfully deploy your own YOLO26 web app to Streamlit Community Cloud following the instructions below
2. **Challenge:** Add a confidence threshold slider to the app that lets users filter detections based on confidence score (hint: use `st.sidebar.slider()` and pass the `conf` parameter to `model.predict()`)
3. **Challenge:** Display a live count of detected objects grouped by class below the video feed (hint: iterate through `results[0].boxes` to access detection data including class names and counts)

## Getting Started

### 1. Fork this repository

- Click the "Fork" button at the top right of this page
- This creates a copy in your GitHub account

### 2. Start Codespace and try the app

- Create a Codespace:
  - In your forked repo, click the green "Code" button
  - Select the "Codespaces" tab
  - Click "Create codespace on main"
  - Wait for the environment to build (this installs all dependencies automatically)

- Run the Streamlit app:
  - Once the Codespace is ready, open a terminal and run:

    ```bash
    streamlit run src/app.py
    ```

  - The app will open in a new browser tab automatically
  - Grant camera permissions when prompted to test object detection

### 3. Deploy to Streamlit Community Cloud

- Create an account:
  - Go to https://share.streamlit.io
  - Sign in with your GitHub account

- Deploy your app:
  - Click "New app"
  - Select your repository from the dropdown
  - Choose the `main` branch
  - Set the main file path to `src/app.py`
  - Click "Deploy"

- The app will build and deploy automatically. Once ready, you'll get a public URL to share!

## Troubleshooting

- If the build fails, check the deployment logs in Streamlit Community Cloud
- For WebRTC camera issues, ensure your browser has camera permissions enabled
- Make sure nothing else is using your camera (e.g. Zoom)
