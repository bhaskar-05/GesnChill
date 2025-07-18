🎮 Hand Gesture Controlled Game with OpenCV & PyAutoGUI

This project allows you to control your game character (or simulate key presses) using hand gestures captured via your webcam!It uses OpenCV for video capture & display, MediaPipe-based hand tracking, and PyAutoGUI to send keyboard inputs.

📋 Features

✅ Detects your hand and fingers in real-time✅ Recognizes the following gestures:

✋ Index finger up: Move forward (W)

👍 Thumb up: Turn left (A)

✌️ Index + Middle fingers up: Turn right (D)

👊 Fist (all fingers down): Brake (S)

✅ Sends corresponding key presses to control your game or application.✅ Displays FPS and highlights the detected gesture.

🛠️ Technologies Used

Python 3

OpenCV

PyAutoGUI

HandTrackingModule (custom module for hand landmarks detection)

🚀 Installation

Clone the repo:

git clone https://github.com/yourusername/gesture-controlled-game.git
cd gesture-controlled-game

Install dependencies:

pip install opencv-python pyautogui mediapipe

Make sure you also include the HandTrackingModule.py file in the same folder.You can download it from here.

📷 Usage

Run the script:

python main.py

The webcam feed will open.

Show the desired gesture.

The gestures are as follow:
  1. Only index - forward
  2. only thumb - left
  3. only pinky - right
  4. fist - break

The corresponding key (W, A, S, D) will be pressed and held as long as you keep the gesture.

Press Q to quit.

🧪 Notes

Works best in good lighting conditions.

Make sure your full hand is visible in the camera.

If gestures don’t match, print the fingersUp() output and adjust the mapping accordingly.

📄 License

This project is open-source under the MIT License.

🙏 Acknowledgements

Inspired by Murtaza's Workshop - Computer Vision

Uses MediaPipe under the hood for hand tracking.

