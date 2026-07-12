output "vpc_id" {
  value = module.network.vpc_id
}

output "public_subnet_ids" {
  value = module.network.public_subnet_ids
}

output "ecr_repository_url" {
  value = module.ecr.repository_url
}

output "alb_dns_name" {
  value = module.alb.alb_dns_name
}

output "ecs_service_name" {
  value = module.ecs.service_name
}

output "task_definition_arn" {
  value = module.ecs.task_definition_arn
}
