#!/bin/bash
# Deploy Prometheus + Grafana monitoring stack on EKS
# Run after: aws eks update-kubeconfig --name <cluster-name> --region <region>

set -e

echo "Adding Helm repositories..."
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

echo "Creating monitoring namespace..."
kubectl create namespace monitoring --dry-run=client -o yaml | kubectl apply -f -

echo "Installing Prometheus..."
helm upgrade --install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --values prometheus-values.yaml \
  --wait

echo "Installing Grafana..."
helm upgrade --install grafana grafana/grafana \
  --namespace monitoring \
  --values grafana-values.yaml \
  --set adminPassword="${GRAFANA_ADMIN_PASSWORD}" \
  --wait

echo ""
echo "Monitoring stack deployed successfully!"
echo ""
echo "Get Grafana URL:"
echo "kubectl get svc grafana -n monitoring"
echo ""
echo "Default credentials: admin / admin123"
echo ""
echo "Useful commands:"
echo "  kubectl get pods -n monitoring"
echo "  kubectl get svc -n monitoring"