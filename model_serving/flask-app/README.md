# Flask ML API Example

This project demonstrates how to serve a machine learning model using Flask.

## Structure

- `train_model.py`: Trains and saves a model to disk.d
- `/predict`: Accepts POST requests with feature data in JSON.

## Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
