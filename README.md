# YOLO26

## Deploy to Hugging Face Spaces (GitHub integration)

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

3. Connect the Space to GitHub
	- In the Space, open the "Settings" tab.
	- Under "Repository", select "Connect to GitHub".
	- Authorize Hugging Face to access your GitHub account.
	- Choose this repository and the branch to deploy (main).
	- Save the settings.

4. Wait for the build to finish
	- The Space will start building automatically from the GitHub repo.
	- When the build completes, open the "App" tab to see the demo.
	- Any new push to the connected branch triggers a rebuild.

5. Troubleshooting
	- If the build fails, open the "Logs" tab to see the error.
	- Common issue: missing system libraries. If you see a libGL error,
	  add a file named packages.txt with a single line:
		 libgl1
	  Then commit the change and push to trigger a rebuild.