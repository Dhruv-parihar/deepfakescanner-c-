# MediaCheck

A beginner-friendly cybersecurity mini project for inspecting media and practicing source verification.

Features: file preview for image/audio/video, SHA-256 fingerprint, Deepware link for manual video scans, source-checking checklist, and downloadable notes.

The app does not run an AI deepfake model or declare files authentic. Deepware scans must be submitted on Deepware's website. Deepware focuses on face manipulation in video, not images or altered audio, and results are probabilistic.

## Run locally

Install Python 3.10 or newer. In Git Bash, from this folder:

    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install -r requirements.txt
    streamlit run app.py

On macOS/Linux, activate with `source .venv/bin/activate`. Streamlit opens at http://localhost:8501.

## Publish

Create an empty GitHub repository, then push this folder. For a hosted app, deploy with Streamlit Community Cloud and select app.py.

References: [Deepware FAQ](https://deepware.ai/us/faq/index.html), [Google Fact Check Explorer](https://toolbox.google.com/factcheck/explorer), [Content Credentials](https://contentcredentials.org/verify).
