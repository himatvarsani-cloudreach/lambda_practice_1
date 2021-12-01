terraform {
  backend "s3" {
    #copy the url from the aws cli - bucket
    bucket         = "lambda-exercise-139446191400-tfstates"
    key            = "sprint2/week4/lambda/terraform.tfstates"
    dynamodb_table = "terraform-lock"
  }
}