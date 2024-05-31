gcloud scheduler jobs create http my-job \
  --schedule="* * * * *" \
  --uri=https://REGION-PROJECT_ID.cloudfunctions.net/publishMessage \
  --http-method=POST \
  --message-body='{"timestamp": "2023-05-30T00:00:00Z", "data": "sample data"}'
