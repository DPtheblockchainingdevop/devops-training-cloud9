import boto3

client = boto3.client('translate', region_name="us-east-2")
text = "Hello World"
result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="es")
print(result['TranslatedText'])