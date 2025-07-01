from waitress import serve
import app  # this should be your Flask app file

print("✅ Waitress server is live on http://127.0.0.1:5000")

# This is correct: call the Flask app object inside app.py
serve(app.app, host='0.0.0.0', port=5000)