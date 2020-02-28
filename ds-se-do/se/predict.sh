ENV_VAR=${MY_ENV_VAR:="NOT SET"}
echo "Training models right now! Typically these would be pre-trained and loaded into memory ..."
python3 /usr/local/lib/python3.6/site-packages/class_demo/train.py
echo "Starting Prediction Mode ..."
echo "Typically this would be a worker of some kind getting invoked with a task ..."
echo "You nearly always use environment variables to set configurable aspects of your application and/or secrets ..."
echo "Environment variable: $ENV_VAR"

while true; do
  OUTPUT=$(python3 /usr/local/lib/python3.6/site-packages/class_demo/predict.py)
  echo "In Predict ... $OUTPUT"
  sleep 5
done
