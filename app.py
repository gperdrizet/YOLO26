'''YOLO26 real-time object detection activity.

A Streamlit web application that performs real-time object detection using the
YOLO26 nano model and webcam input. The app processes video frames through streamlit-webrtc
and displays an annotated video stream with detected objects.
'''

import av
import streamlit as st
from streamlit_webrtc import (
    webrtc_streamer,
    WebRtcMode,
    RTCConfiguration,
    VideoProcessorBase,
)
from ultralytics import YOLO


@st.cache_resource
def load_model() -> YOLO:
    '''Load and cache the YOLO26 model.
    
    Uses Streamlit's cache_resource to load the model only once and reuse it
    across sessions, improving performance and reducing memory usage.
    
    Returns:
        YOLO: The loaded YOLO26 model instance.
    '''

    return YOLO('yolo26n.pt')


class VideoProcessor(VideoProcessorBase):
    '''Process video frames for real-time object detection.
    
    This class handles the video stream from the webcam, runs YOLO26 inference
    on each frame, and returns annotated frames with bounding boxes and labels.
    Inherits from VideoProcessorBase for proper streamlit-webrtc integration.
    '''

    def __init__(self) -> None:
        '''Initialize the video processor with the YOLO26 model.'''

        super().__init__()
        self.model = load_model()

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        '''Process a single video frame through the YOLO26 model.
        
        Args:
            frame: Input video frame from the webcam.
            
        Returns:
            av.VideoFrame: Annotated frame with detected objects, bounding boxes,
                and class labels.
        '''

        # Convert PyAV frame to numpy array in BGR format
        image = frame.to_ndarray(format='bgr24')
        
        # Run YOLO26 inference on the frame
        results = self.model.predict(image, verbose=False)
        
        # Plot bounding boxes and labels on the frame
        annotated = results[0].plot()

        # Convert back to PyAV frame for streaming
        return av.VideoFrame.from_ndarray(annotated, format='bgr24')


def main() -> None:
    '''Run the Streamlit application.
    
    Sets up the page configuration, displays the title, and initializes the
    webcam streamer with the YOLO26 video processor.
    '''

    st.set_page_config(page_title='YOLO26 real-time object detection', layout='centered')
    st.title('YOLO26 real-time object detection')

    # Configure WebRTC with STUN servers for cloud deployment
    rtc_configuration = RTCConfiguration(
        {'iceServers': [{'urls': ['stun:stun.l.google.com:19302']}]}
    )

    # Start the webcam streamer with async processing for better performance
    webrtc_streamer(
        key='yolo26-live',
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=rtc_configuration,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={'video': True, 'audio': False},
        async_processing=True,
    )


if __name__ == '__main__':
    main()
