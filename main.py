import keep_alive
import stream

if __name__ == "__main__":
    # Start Flask keep_alive server
    keep_alive.keep_alive()

    # Start YouTube Stream (ffmpeg loop)
    stream.stream_video_loop()
