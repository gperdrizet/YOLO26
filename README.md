# YOLO26

## Deploy to Hugging Face Spaces (git remote push)

These steps assume you do not have a Hugging Face account yet.

1. Create an account
	- Go to https://huggingface.co/join and create a new account.
	- Verify your email if prompted.

2. Create a new Space
	- Go to https://huggingface.co/spaces and select "Create new Space".
	- Fill in the form:
	  - Owner: your username
	  - Space name: yolo26-demo (or any name you want)
	  - License: choose any
	  - SDK: Docker -> Streamlit
	  - Space visibility: Public (recommended for first try)
	- Select "Create Space".

3. Configure the Space as a git remote
	- Log into HuggingFace:

	  ```bash
	  huggingface-cli login
	  ```

	- Add the Space as a remote in this repo:

	  ```bash
	  git remote add hf https://huggingface.co/spaces/<your-username>/<your-space-name>
	  ```

4. Push the repo to the Space
	- Push your main branch:

	  ```bash
	  git push hf main
	  ```

	- The Space will build automatically. Open the "App" tab once it finishes.

5. Troubleshooting
	- If the build fails, open the "Logs" tab to see the error.
	- Common issue: missing system libraries. If you see a libGL error,
	  add a file named packages.txt with a single line:
		 libgl1
	  Then commit and push again to trigger a rebuild.