#!/bin/bash

# Step 1: Start the Flask server in the background
echo "🚀 Starting Flask server..."
python app.py &
FLASK_PID=$!

# Step 2: Wait for the server to initialize
echo "⌛ Waiting for server to start..."
sleep 3  # Adjust if your system is slower
echo ""

# Step 3: Send a test prediction
echo "➡️  Sending test prediction request..."
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
echo ""

# Step 4: Kill the Flask server
echo "🧹 Stopping Flask server (PID: $FLASK_PID)..."
kill $FLASK_PID
