terraform {
	required_providers {
		docker = {
		      source  = "kreuzwerker/docker"
		      version = "~> 3.6.2"
		}
	}
}

provider "docker" {
}

resource "docker_image" "nginx-image" {
	name = "nginx:alpine"
}

resource "docker_container" "nginx-container" {
	name  = "nginx-container"
	image = docker_image.nginx-image.image_id
	ports {
		internal = 80
		external = 8090
	}
}
