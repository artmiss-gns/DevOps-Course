variable "nginx_image" {
  description = "The Docker image and tag to use for the Nginx container."
  type        = string
  default     = "nginx:alpine"
}

variable "container_name" {
  description = "The name for the running Docker container."
  type        = string
  default     = "mynginx02"
}

variable "internal_port" {
  description = "The internal port inside the container that the application listens on."
  type        = number
  default     = 80
}

variable "external_port" {
  description = "The external port on the host machine to map to the container's internal port."
  type        = number
  default     = 8091
}
