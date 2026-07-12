data "aws_iam_role" "ecs_task_execution" {
  name = "ecsTaskExecutionRole"
}

module "network" {
  source = "./modules/network"

  environment = var.environment

  project_name = var.project_name
}

module "ecr" {
  source = "./modules/ecr"

  repository_name = "${var.project_name}-inference"
  environment     = var.environment
}

module "alb" {
  source = "./modules/alb"

  project_name      = var.project_name
  vpc_id            = module.network.vpc_id
  public_subnet_ids = module.network.public_subnet_ids
  container_port    = 5000
}

module "ecs" {
  source = "./modules/ecs"

  project_name          = var.project_name
  subnet_ids            = module.network.public_subnet_ids
  vpc_id                = module.network.vpc_id
  image_uri             = "${module.ecr.repository_url}:latest"
  alb_security_group_id = module.alb.security_group_id
  target_group_arn      = module.alb.target_group_arn
  execution_role_arn    = "arn:aws:iam::739340816202:role/ecsTaskExecutionRole"
}
