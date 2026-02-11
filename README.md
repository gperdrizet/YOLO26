---
title: YOLO26 Camera Demo
emoji: 📹
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.31.0"
app_file: app.py
pinned: false
---

# YOLO26

## Try the app in GitHub Codespaces

1. Fork this repository
	- Click the "Fork" button at the top right of this page
	- This creates a copy in your GitHub account

2. Create a Codespace
	- In your forked repo, click the green "Code" button
	- Select the "Codespaces" tab
	- Click "Create codespace on main"
	- Wait for the environment to build (this installs all dependencies automatically)

3. Run the Streamlit app
	- Once the Codespace is ready, open a terminal and run:

	  ```bash
	  streamlit run app.py
	  ```

	- The app will open in a new browser tab automatically
	- Grant camera permissions when prompted to test object detection

## Deploy to Hugging Face Spaces (git remote push)

These steps assume you do not have a Hugging Face account yet.

1. Create a HuggingFace account
	- Go to https://huggingface.co/join and create a new account.
	- Verify your email if prompted.

2. Create a new HuggingFace Space
	- Go to https://huggingface.co/spaces and select "Create new Space".
	- Fill in the form:
	  - Owner: your username
	  - Space name: yolo26-demo (or any name you want)
	  - License: choose any
	  - SDK: Docker -> Streamlit
	  - Space visibility: Public (recommended for first try)
	- Select "Create Space".

3. Configure the Space as a git remote
	- Create a Hugging Face access token:
	  - Go to https://huggingface.co/settings/tokens
	  - Create a new token with write permissions
	  - Copy the token

	- Add the token as a Codespaces secret:
	  - Go to your GitHub repository settings
	  - Navigate to Settings -> Secrets and variables → Codespaces
	  - Create a new secret named `HF_TOKEN` and paste your token
	  - If the codespace is currently running, you will need to rebuild

	- Add the Space as a remote using the token (will be available as `$HF_TOKEN` in Codespaces):

	  ```bash
	  git remote add hf https://YOUR_HF_USERNAME:$HF_TOKEN@huggingface.co/spaces/<your-username>/<your-space-name>
	  ```

4. Push the repo to the Space
	- Push your main branch (force required for first push since the Space has its own initial commit):

	  ```bash
	  git push hf main --force
	  ```


	- You will only need to use the `--force` option on the first push.
	- The Space will build automatically. Open the "App" tab once it finishes.

5. Troubleshooting
	- If the build fails, open the "Logs" tab to see the error.
	- Common issue: missing system libraries. If you see a libGL error,
	  add a file named packages.txt with a single line:
		 libgl1
	  Then commit and push again to trigger a rebuild.