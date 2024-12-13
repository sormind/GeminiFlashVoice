# Simple Gemini Voice Interaction

**Unlock Real-Time Conversations with Gemini 2.0 Flash Live API in Just 60 Lines of Python Code!** 🎤  

This project demonstrates how to integrate the **Google DeepMind Gemini 2.0 Flash API** for real-time, interactive voice conversations. Stream audio from your microphone, send it to Gemini for processing, and hear the AI's response—all in one simple script!

---

## 🚀 Features
- Real-time audio streaming and processing.
- Uses **60 lines of clean, beginner-friendly Python code**.
- Sends user audio to the Gemini 2.0 API and plays back the response.
- Beginner-friendly setup and easy to customize.

---

## 🛠️ Requirements
- Python 3.8+
- **Dependencies**:
  - `pyaudio`  
  - `websockets`

---

## 🔧 Installation
1. **Clone this repository** or copy the script directly.
   ```bash
   git clone https://github.com/your-repo/simple-gemini-voice.git
   cd simple-gemini-voice

	2.	Install the required dependencies:

pip install pyaudio websockets


	3.	Set up your API key:
Obtain your API key from Google DeepMind Gemini 2.0 and export it:

export GEMINI_API_KEY="your_api_key_here"


	4.	Run the script:

python simple_gemini_voice.py

📜 Usage
	1.	Speak into your microphone after running the script.
	2.	The script streams your audio to Gemini 2.0.
	3.	Listen to Gemini’s real-time response!

⚙️ Configuration
	•	Audio Settings: Modify FORMAT, CHANNELS, RATE, and CHUNK in the script to adjust audio streaming settings.
	•	Model: Change the self.model variable in the script if you wish to experiment with other Gemini API models.

🧰 Troubleshooting
	•	Error: OSError: [Errno -9996] Invalid input device:
	•	Ensure your microphone is properly connected.
	•	Check that your system permissions allow microphone access.
	•	API Key Error:
	•	Make sure you set GEMINI_API_KEY properly using the export command.

🌟 Contributions

Feel free to fork, customize, and create a pull request! Feedback and improvements are always welcome.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Acknowledgements
	•	Thanks to Google DeepMind for the Gemini 2.0 API.
	•	Inspired by Philipp Schmid’s post on Flash Live API integration.

