TEXT_TO_CLASSIFY=${TEXT_TO_CLASSIFY:="NOT SET"}
echo "Training models right now!"
printf "Typically these would be pre-trained and loaded into memory ...\n\n"

# Invoke the training script - again, this is NOT how to do it in production
python3 /usr/local/lib/python3.6/site-packages/ds/train.py

echo "Starting Prediction Mode ..."
echo ""
echo "Often, this would be a worker of some kind getting invoked with a task ..."
echo "Environment variables are frequently used to set configurable aspects"
echo "of your application and/or secrets ..."
echo ""
echo "Environment variable: $TEXT_TO_CLASSIFY"
echo ""

while true; do
  OUTPUT=$(python3 /usr/local/lib/python3.6/site-packages/ds/predict.py "$TEXT_TO_CLASSIFY"; echo x)
  OUTPUT=${OUTPUT%x}
  printf "$OUTPUT"

  sleep 5
done
