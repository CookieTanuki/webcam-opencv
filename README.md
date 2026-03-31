# webcam-opencv

Simple desktop webcam app built with OpenCV and PyQt6.

The application opens your default camera, processes each frame in real time, and shows the original image next to the selected effect inside a GUI window.

## Core functionality

- Real-time webcam capture
- PyQt6 desktop GUI
- Side-by-side preview of original and processed video
- Live FPS counter
- Effect selection from a dropdown

## Available video effects

- `None` - show the original frame
- `Negative` - invert the frame colors
- `Grayscale` - convert the frame to grayscale
- `GaussianBlur` - apply blur to the frame
- `EdgeDetection` - highlight edges
- `Sepia` - apply a warm vintage-style filter

## Run locally

Requirements:

- Python 3.13+
- OpenCV
- PyQt6


Clone the repository:

```bash
git clone <repository_url>
cd webcam-opencv
```


Install dependencies with `uv`:

```bash
uv sync
```

Run the GUI app:

```bash
uv run python main.py
```

If you are using your own virtual environment instead of `uv`, install the dependencies manually and run:

```bash
python main.py
```

## How to use

1. Start the app.
2. Allow camera access if your operating system asks for permission.
3. Use the dropdown in the window to switch between effects.
4. Press `Q` or close the window to exit.

## Program interface

<img width="1432" height="718" alt="Screenshot 2026-03-31 at 13 54 02" src="https://github.com/user-attachments/assets/a721d6df-c860-4ae5-9f0c-4a7d4e4ade4d" />
