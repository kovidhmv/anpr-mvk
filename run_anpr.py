import argparse
import cv2
import os

cv2.startWindowThread()

from Indian_LPR.video_pipeline import process_video


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ANPR pipeline")
    parser.add_argument("--video", required=True, help="Input video path or camera index")
    parser.add_argument("--output", default="vidres/output_tracked.mp4", help="Output video path or directory")
    parser.add_argument("--mode", choices=["offline", "realtime"], default="offline")
    args = parser.parse_args()

    input_path = str(args.video)
    abs_path = os.path.abspath(input_path)

    print("🚀 Running ANPR pipeline...")
    print("CWD:", os.getcwd())
    print("Input video path:", input_path)
    print("Resolved path:", abs_path)

    if not os.path.exists(abs_path):
        print("[ERROR] File not found:", abs_path)
        raise SystemExit(1)

    process_video(abs_path, args.output, mode=args.mode)
