gcloud functions deploy publishMessage \
  --runtime nodejs14 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point publishMessage
