## Mirror of the Future

This project is an AI-powered web application that enhances user text inputs to predict and visualize how objects or concepts might look 20 years in the future.

## Features

- **Text Enhancement**: Transforms your inputs into detailed future predictions
- **Image Generation**: Creates visuals based on enhanced text descriptions
- **Voice Recognition**: Browser-based speech recognition for voice inputs
- **Modern Interface**: Intuitive and user-friendly web interface

## Installation

### Requirements

- Python 3.8 or newer
- pip (Python package manager)
- Git (for installation)
- Minimum 4GB RAM (for AI models)
- Disk space: minimum 2GB (for AI models)
- Modern web browser (Chrome, Firefox, Edge, or Safari)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/YOURUSERNAME/gelecegin-aynasi.git
   cd gelecegin-aynasi
   ```

2. Create and activate a virtual environment:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   Note: This step may take some time (approximately 5-10 minutes) as it downloads AI models

4. Set up environment variables (.env file):
   - Windows:
     ```
     copy .env.example .env
     ```
   - Mac/Linux:
     ```
     cp .env.example .env
     ```
   Note: Optionally, you can edit the .env file to add your own API keys

5. Start the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to: `http://127.0.0.1:5001`

## Troubleshooting

- **Models fail to download**: Check your internet connection or use a VPN
- **"CUDA out of memory" error**: If GPU memory is insufficient, reduce image dimensions and steps in `image_generator.py`
- **Speech recognition not working**: Ensure your browser has permission to access the microphone
- **Application is too slow**: It might be running in CPU mode; use a faster computer or GPU
