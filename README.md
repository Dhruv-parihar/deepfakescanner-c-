# MediaCheck

A beginner-friendly cybersecurity project for inspecting media files and practicing source verification.

## What it does

- Previews supported image, audio, and video files.
- Displays basic file details and a SHA-256 fingerprint.
- For images, shows dimensions and available EXIF metadata, checks selected embedded generator/editing markers, and displays a JPEG recompression difference map.
- Shows a rule-based image indicator score. This is not the probability an image is fake and is not produced by a trained image detector.
- Links to WeDetect for an optional external image check. The app does not upload the file to WeDetect automatically.
- Links to Deepware for manual video screening. Deepware focuses on facial manipulation in video; it does not scan still images or altered voices.
- Provides a source-verification checklist and downloadable notes.

## Run locally

Clone the repository and enter its folder:

```bash
git clone https://github.com/Dhruv-parihar/deepfakescanner-c-.git
cd deepfakescanner-c-
```

Install dependencies and start the app:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If you already cloned the repo, run those two commands from inside the `deepfakescanner-c-` folder. Open the local address Streamlit prints, usually http://localhost:8501.

## External verification tools

- [WeDetect AI image detector](https://wedetect.ai/) accepts images and returns an estimate. Its [face-swap image checker](https://wedetect.ai/deepfake-detector) also accepts still images, not video files. To use it for a video, submit a clear screenshot of a face frame. You upload manually on WeDetect; this app does not integrate an API or send files automatically. Review WeDetect's privacy terms before submitting sensitive content.
- [Deepware Scanner](https://scanner.deepware.ai/) is the original video link. If it is unavailable, try again later; the app does not simulate Deepware results.

Both services can be wrong. Scores are estimates, not proof. Check the source, date, context, and claim against independent reporting.

## Host as a web app

GitHub stores the project files; it does not run the app itself. To host it, sign in to [Streamlit Community Cloud](https://share.streamlit.io/), create an app, select repository `Dhruv-parihar/deepfakescanner-c-`, branch `main`, and app file `app.py`, then deploy. See the [official deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Privacy

The app has no database or custom backend. Uploaded media is used in the active app session for preview and inspection. Any media you submit to WeDetect or another external service is handled under that provider's terms. No API key is included in this repository.

## References

- [WeDetect AI image detector](https://wedetect.ai/)
- [WeDetect face-swap image checker](https://wedetect.ai/deepfake-detector)
- [DetectVideo AI video detector](https://detectvideo.ai/)
- [Deepfake Detector AI voice checker](https://deepfakedetector.aiaware.io/)
- [Deepware FAQ](https://deepware.ai/us/faq/index.html)
- [Google Fact Check Explorer](https://toolbox.google.com/factcheck/explorer)
- [Content Credentials Verify](https://contentcredentials.org/verify)
