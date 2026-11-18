import hashlib
import io
from datetime import datetime, timezone
from pathlib import Path
import streamlit as st
from PIL import Image, ImageChops, ImageEnhance, ExifTags

st.set_page_config(page_title="MediaCheck", page_icon="🔎")
st.title("🔎 MediaCheck")
st.caption("A learning tool for checking media and context before sharing.")
st.warning("This app does not prove whether content is real or fake. Metadata and hashes are observations, not deepfake detection. Treat detector results as one signal and verify claims with independent sources.")

st.header("1. Inspect a media file")
uploaded = st.file_uploader("Choose an image, audio, or video", type=["jpg", "jpeg", "png", "webp", "gif", "mp3", "wav", "m4a", "ogg", "mp4", "mov", "webm", "mkv"])
if uploaded:
    data = uploaded.getvalue()
    digest = hashlib.sha256(data).hexdigest()
    st.write(f"File: {uploaded.name}")
    st.write(f"Type: {uploaded.type or 'Unknown'}")
    st.write(f"Size: {len(data):,} bytes")
    st.code(digest)
    st.caption("SHA-256 identifies this exact file; it does not indicate authenticity.")
    suffix = Path(uploaded.name).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        st.image(data, use_container_width=True)
        st.subheader("Image inspection")
        try:
            with Image.open(io.BytesIO(data)) as image:
                exif = image.getexif()
                exif_names = {ExifTags.TAGS.get(key, str(key)): str(value) for key, value in exif.items()}
                st.write(f"Dimensions: {image.width} × {image.height} pixels")
                st.write(f"Format: {image.format or 'Unknown'}")
                software = exif_names.get("Software")
                if software:
                    st.write(f"Software metadata: {software}")
                    st.caption("Editing software metadata can indicate a resave, but does not by itself mean an image is deceptive.")
                else:
                    st.write("No software field was found in EXIF metadata.")
                    st.caption("Metadata is often removed by messaging and social platforms; missing metadata is not evidence of manipulation.")
                if exif_names:
                    with st.expander("View available EXIF metadata"):
                        st.json(exif_names)
                if image.format in {"JPEG", "MPO"}:
                    recompressed = io.BytesIO()
                    image.convert("RGB").save(recompressed, format="JPEG", quality=90)
                    recompressed.seek(0)
                    with Image.open(recompressed) as reference:
                        diff = ImageChops.difference(image.convert("RGB"), reference.convert("RGB"))
                        extrema = diff.getextrema()
                        peak = max((channel[1] for channel in extrema), default=0)
                        if peak:
                            diff = ImageEnhance.Contrast(diff).enhance(min(255.0 / peak, 8.0))
                    st.image(diff, caption="Amplified JPEG recompression difference map", use_container_width=True)
                    st.caption("Bright areas show pixels that changed during recompression. Compression, texture, and editing can all create differences; this is a visual aid, not an AI detector or a fake-image verdict.")
                else:
                    st.info("JPEG recompression comparison is available for JPEG images only.")
        except Exception as exc:
            st.error(f"Could not inspect this image: {exc}")
    elif suffix in {".mp4", ".mov", ".webm", ".mkv"}:
        st.video(data)
    elif suffix in {".mp3", ".wav", ".m4a", ".ogg"}:
        st.audio(data)

st.header("2. Check a video with Deepware")
st.write("Deepware focuses on AI facial manipulation in video. It does not check still images or altered voices, and results can be wrong.")
st.link_button("Open Deepware Scanner", "https://scanner.deepware.ai/")
st.caption("Submit the video on Deepware's site, then record its result below. This app does not simulate a scan.")
deepware_result = st.text_input("Deepware result (optional)")

st.header("3. Verify the claim and source")
source_url = st.text_input("Source URL (optional)")
claim = st.text_area("What does the post claim?")
checks = ["I found the earliest available version.", "I checked the date and location.", "I searched independent reliable sources.", "I checked whether the media appeared earlier in another context.", "I treated automated results as clues, not proof."]
selected = [st.checkbox(item) for item in checks]
notes = st.text_area("Notes")
if st.button("Prepare verification notes"):
    lines = ["MEDIACHECK — VERIFICATION NOTES", f"Created: {datetime.now(timezone.utc).isoformat()}", f"File: {uploaded.name if uploaded else 'None selected'}", f"SHA-256: {digest if uploaded else 'Not available'}", f"Source URL: {source_url or 'Not provided'}", f"Claim: {claim or 'Not provided'}", f"Deepware result (user-entered): {deepware_result or 'Not provided'}", "Checks completed:", *[f"- {label}" for label, done in zip(checks, selected) if done], f"Notes: {notes or 'None'}", "", "These notes do not establish authenticity."]
    st.download_button("Download notes", data="\n".join(lines), file_name="mediacheck-notes.txt", mime="text/plain")

st.header("Useful resources")
st.markdown("- [Google Fact Check Explorer](https://toolbox.google.com/factcheck/explorer)\n- [Google Lens](https://lens.google.com/)\n- [Deepware FAQ](https://deepware.ai/us/faq/index.html)\n- [Content Credentials Verify](https://contentcredentials.org/verify)")
st.caption("Files are used in the app session. External services receive any media you submit to them under their own privacy terms.")

