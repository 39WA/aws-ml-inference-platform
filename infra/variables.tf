variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "eu-west-2"
}

variable "project_name" {
  description = "Project resource prefix"
  type        = string
  default     = "aws-ml"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}
