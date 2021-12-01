
# Creating IAM role so that Lambda service to assume the role and access other AWS services. 



resource "aws_iam_role" "lambda_role" {
  name = "assume_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = <<EOF
{
      "Version" : "2012-10-17",
      "Statement" : [
          {
            "Action" : [
                "sts:AssumeRole"
            ],
            "Principal" : {
                "Service" : "lambda.amazonaws.com"
            },
            "Effect" : "Allow",
            "Sid" : "LambdaRole2"
          }
      ]
}
EOF
  tags = {
    tag-key = "assume-role"
  }
}


# IAM policy for logging from a lambda

resource "aws_iam_policy" "lambda_logging" {

  name        = "iam_policy_lambda_logging_function"
  description = "IAM policy for logging from a lambda"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement" : [
          {
            "Action" : [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*",
            "Effect" : "Allow",
            "Sid" : "cloudwatchLambda"
          },
          {
            "Action" : [
                "s3:GetObject",
                "s3:List*",
                "s3:PutObject"
            ],
            "Effect" : "Allow",
            "Sid" : "S3ObjectActions",
            "Resource" : ["arn:aws:s3:::*"]
            }
      ]

}
EOF
}

# Policy Attachment on the role.

resource "aws_iam_role_policy_attachment" "policy_attach" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}