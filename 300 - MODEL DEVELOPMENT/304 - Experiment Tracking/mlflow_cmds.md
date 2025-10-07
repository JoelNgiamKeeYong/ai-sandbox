# **MLflow Commands**

## 🏁 Verify MLflow Installation

- Check MLflow version:

  ```bash
  mlflow --version                               :: Verify MLflow is installed
  ```

- Show MLflow help:

  ```bash
  mlflow --help                                  :: View all available commands
  ```

## 🚀 Run MLflow UI / Server

- Start MLflow UI (default port 5000):

  ```bash
  mlflow ui                                       :: Launch MLflow tracking UI
  ```

- Start MLflow UI on a custom port:

  ```bash
  mlflow ui --port 5001                           :: Launch UI on port 5001
  ```

- Start MLflow UI with a custom backend store:

  ```bash
  mlflow ui --backend-store-uri ./mlruns --port 5000   :: Use local mlruns directory as backend and start UI on port 5000
  ```

- Run full MLflow server with custom backend & artifact store:

  ```bash
  mlflow server \
   --backend-store-uri sqlite:///mlflow.db \
   --default-artifact-root ./mlruns \
   --host 0.0.0.0 \
   --port 5000                                 :: Full server with database & artifact storage
  ```

## 📊 Experiments & Runs

1. Create or set an experiment:

   ```python
   import mlflow

   mlflow.set_experiment("my_experiment")         :: Create or set experiment
   ```

2. Start a new run:

   ```python
   with mlflow.start_run() as run:
        print(run.info.run_id)                       :: Start tracking a run
   ```

3. Resume an existing run:

   ```python
   mlflow.start_run(run_id="existing_run_id")      :: Resume tracking for a specific run
   ```

## 📈 Logging Parameters, Metrics, and Artifacts

1. Log hyperparameters:

   ```python
   mlflow.log_param("learning_rate", 0.01)        :: Log a single parameter
   mlflow.log_params({"lr": 0.01, "batch_size": 32})  :: Log multiple parameters
   ```

2. Log metrics:

   ```python
   mlflow.log_metric("accuracy", 0.95)            :: Log a single metric
   mlflow.log_metrics({"accuracy": 0.95, "loss": 0.1})  :: Log multiple metrics
   ```

3. Log artifacts:

   ```python
   mlflow.log_artifact("model.pt")                 :: Log a single file
   mlflow.log_artifacts("logs/")                   :: Log a directory of artifacts
   ```

## 🧠 MLflow Models

1. Log a PyTorch model:

   ```python
   import mlflow.pytorch

   mlflow.pytorch.log_model(model, artifact_path="models")       :: Log model for tracking
   mlflow.pytorch.save_model(model, path="models/model_dir")     :: Save model locally
   mlflow.pytorch.load_model("models/model_dir")                :: Load a model
   ```

2. Register a model for serving:

   ```python
   mlflow.pytorch.log_model(
        model,
        artifact_path="models",
        registered_model_name="mnist_model"
    )                                                               :: Register model
   ```

3. Load a registered model:

   ```python
   model = mlflow.pytorch.load_model("models:/mnist_model/1")     :: Load registered model version
   ```

## 🔍 Inspect Experiments & Runs

1. Load experiments:

   ```python
   mlflow experiments list                          :: List all experiments
   ```

2. Show runs in an experiment:

   ```python
   mlflow runs list --experiment-id 1               :: Show all runs in experiment
   ```

3. View MLflow artifact URI:

   ```python
   mlflow.get_artifact_uri()                        :: Returns base artifact storage path
   ```

## ⚡ Manage MLflow UI / Server

1. Check MLflow processes

   ```python
   ps aux | grep mlflow
   ```

2. Stop MLflow UI (if running in background):

   ```python
   pkill -f mlflow                                  :: Kill all MLflow processes
   ```

3. View logs when UI is running:

   ```python
   tail -f mlruns/mlflow.log                        :: Tail logs (Linux/Mac)
   ```

## 📦 Autologging (Optional)

1. Enable automatic logging for PyTorch, sklearn, TensorFlow, etc.:

   ```python
   mlflow.pytorch.autolog()                          :: Autolog metrics, params, and model
   mlflow.sklearn.autolog()
   mlflow.tensorflow.autolog()
   ```
