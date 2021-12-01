import boto3

def pet_info_handler(event, content):
    #connected to the S3 service through API calls
    s3_client = boto3.client('s3')
    
    #Collect the bucket name from event
    target_bucket_name = event["S3Bucket"] 
    
    my_buckets_raw = s3_client.list_buckets()
    #print(my_buckets_raw["Buckets"])
    
    for b in my_buckets_raw ["Buckets"]:
        print ("Name of Bucket : " + b["Name"])
        if b["Name"] == target_bucket_name:
            print ("The bucket " + target_bucket_name + "exist")

# response = s3_client.get_object(Bucket='lambda-exercise-139446191400-tfstates', Key='sample-data.json')

# data = response['Body'].read()
# print(data)