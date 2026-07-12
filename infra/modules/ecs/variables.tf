variable "project_name" {
  type = string
}

variable "image_uri" {
  type = string
}

variable "execution_role_arn" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
}

variable "vpc_id" {
  type = string
}

variable "alb_security_group_id" {
  type = string
}

variable "target_group_arn" {
  type = string
}

variable "container_port" {
  type    = number
  default = 5000
}

variable "task_cpu" {
  type    = number
  default = 1024
}

variable "task_memory" {
  type    = number
  default = 3072
}

variable "desired_count" {
  type    = number
  default = 1
}
