terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.27"
    }
  }
}

provider "kubernetes" {
  config_path = "./.kubeconfig"
}

resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "nginx-alpine-deployment"
    labels = {
      app = "nginx-app"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "nginx-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx-app"
        }
      }

      spec {
        container {
          name  = "nginx"
          image = "nginx:alpine"
          port {
            container_port = 80
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-clusterip-service"
  }

  spec {
    type = "ClusterIP"

    selector = {
      app = kubernetes_deployment.nginx.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 80
      target_port = 80
      protocol    = "TCP"
    }
  }
}
