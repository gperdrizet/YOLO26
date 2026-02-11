import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO


@st.cache_resource
def load_model() -> YOLO:
    return YOLO("yolo26n.pt")


class VideoProcessor:
    def __init__(self) -> None:
        self.model = load_model()

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        results = self.model.predict(image, verbose=False)
        annotated = results[0].plot()
        return av.VideoFrame.from_ndarray(annotated, format="bgr24")


def main() -> None:
    st.set_page_config(page_title="YOLO26 camera demo", layout="centered")
    st.title("YOLO26 camera demo")

    webrtc_streamer(
        key="yolo26-live",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )


if __name__ == "__main__":
    main()
