#Importing JSON just so the JSON output from AWS is clean/readable
import boto3
import json

#Connected to the S3 service through API calls - entry point for code when lambda is run
def pet_info_handler(event, content):
    #connected to the S3 service through API calls
    
    #Opening a client for S3 using boto3 function to interact with s3 objects
   # Grabbing list of buckets in JSON format

    s3_client = boto3.client('s3')
    s3resource = boto3.resource('s3')
    
    #Collect the bucket name from event - Lambda console
    # {
        # "S3Bucket": "lambda-exercise-139446191400-tfstates",
        # "S3Prefix": "sprint2/week4/lambda/sample-data.json",
        # "PetName": "Meowsalot"
    # }
    bucket_name = event["S3Bucket"] 
    s3_key = event["S3Prefix"]
   
    
    response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
    print(response)
 #   print(response["Body"].decode('utf-8'))
    # content = response["Body"].read()
    # jsonObject = json.loads(content)
    
 
    #my_bucket = s3resource.Bucket(bucket_name)
    # obj = my_bucket.Object(s3_key)
    
    # List all the created buckets in the S3
    my_buckets_raw = s3_client.list_buckets()
     #Loops through all buckets
    for b in my_buckets_raw ["Buckets"]:
        if b["Name"] == bucket_name:
            print ("Name of Bucket : " + b["Name"])
            
            # .resource to access objects within bucket
            # mybucket is the object variable for the stored bucket - requesting the bucket
            myBucket = s3resource.Bucket(bucket_name)
            obj = myBucket.Object(s3_key) #Sampledata.json #requesting object(file) with ‘key’ taken from the event - full path
            pets_content = format(obj.get()["Body"].read().decode('utf-8'))
            jsonContent = json.loads(pets_content)
            pets_list = jsonContent["pets"]
            
    for pet in pets_list:
        if event['PetName'] == pet['name']:
            print('Pet Name: ' + pet['name'])
            print('Pet Favourite Food: ' + str(pet['favFoods']))
            return {
                'statusCode' : 200,
                'Pet Name' : json.dumps(pet['name']),
                'Pet Food' : json.dumps(pet['favFoods'])
                }
    print("No pet found")
    return{
        'statusCode' : 404,
        'body' : "No Pet Found"
        }