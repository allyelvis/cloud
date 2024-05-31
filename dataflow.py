import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import json

class ParsePubSubMessage(beam.DoFn):
    def process(self, message):
        record = json.loads(message.decode('utf-8'))
        yield {
            'timestamp': record['timestamp'],
            'data': record['data']
        }

def run():
    pipeline_options = PipelineOptions()
    pipeline_options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/YOUR_PROJECT_ID/topics/my-topic')
            | 'Parse Pub/Sub Message' >> beam.ParDo(ParsePubSubMessage())
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                'my_dataset.my_table',
                schema='timestamp:TIMESTAMP,data:STRING',
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == '__main__':
    run()
