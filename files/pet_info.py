import boto3
import json

def pet_info_handler(event, content):
    #connected to the S3 service through API calls
    s3_client = boto3.client('s3')
    
    #Collect the bucket name from event - Lambda console
    # {
        # "S3Bucket": "lambda-exercise-139446191400-tfstates",
        # "S3Prefix": "sprint2/week4/lambda/sample-data.json",
        # "PetName": "Meowsalot"
    # }
    bucket_name = event["S3Bucket"] 
    s3_key = event ["S3Prefix"]
    
    response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
    content = response["Body"]
    jsonObject = json.load(content.read().decode('utf-8'))
    #my_bucket = s3resource.Bucket(bucket_name)
    # obj = my_bucket.Object(s3_key)
    
    # List all the created buckets in the S3
    my_buckets_raw = s3_client.list_buckets()
    for b in my_buckets_raw ["Buckets"]:
        if b["Name"] == bucket_name:
            print ("The bucket " + bucket_name + "exist")
            print ("Name of Bucket : " + b["Name"])
            
    for pet in jsonObject[‘pets’]:
        if event[‘PetName’] == pet[‘name’]:
            print(pet[‘favFoods’])
            else
            print(pet[‘favFoods’] + 'Not found')