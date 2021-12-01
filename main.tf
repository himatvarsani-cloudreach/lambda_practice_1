# Generates an archive from content, a file, or a directory of files.

data "archive_file" "default" {
  type        = "zip"
  source_file = "${path.module}/files/pet_info.py"
  output_path = "${path.module}/files/pet_info.zip"
}

# Create a lambda function
# In terraform ${path.module} is the current directory.

resource "aws_lambda_function" "lambdafunc" {
  filename         = "${path.module}/files/pet_info.zip"
  function_name    = "My_Lambda_pet"
  role             = aws_iam_role.lambda_role.arn
  handler          = "pet_info.pet_info_handler"
  runtime          = "python3.8"
  source_code_hash = data.archive_file.default.output_base64sha256
  depends_on       = [aws_iam_role_policy_attachment.policy_attach]
}