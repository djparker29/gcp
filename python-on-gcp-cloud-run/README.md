# Python Flask application on Google Cloud with Cloud Run

This is a simple Cloud Run service using a Python Flask application.
It converts Euros to USD.

Build and deploy this service by running the following commands:

```
$ gcloud builds submit --tag gcr.io/PROJECT_ID/euro-to-usd

$ gcloud run deploy --image gcr.io/PROJECT_ID/euro-to-usd --platform managed
```

For more info, check out the video that this service is based off of at [Serverless Expeditions video](https://www.youtube.com/watch?v=s2TIWIzCftM).
