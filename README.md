# Python Docker App

Aplicação web Python com Tornado, containerizada com Docker e pronta para deploy no Kubernetes via Azure Pipelines.

## Stack

| Tecnologia | Versão |
|------------|--------|
| Python | 3.12 |
| Tornado | 6.4.2 |
| Docker | — |
| Kubernetes | 1.28+ |
| Azure Pipelines | — |

## Endpoints

| Rota | Descrição |
|------|-----------|
| `GET /` | Página principal |
| `GET /health` | Health check — retorna `{"status": "ok"}` |

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `APP_NAME` | `Python Docker App` | Nome exibido na página |
| `APP_COLOR` | `#0d1117` | Cor de fundo em hex |
| `PORT` | `8888` | Porta do servidor |

## Rodar localmente

```bash
pip install -r requirements.txt
python server.py
# Acesse http://localhost:8888
```

## Docker

```bash
docker build -t python-docker-app .
docker run -p 8888:8888 -e APP_NAME="Minha App" python-docker-app
```

## Kubernetes

```bash
kubectl apply -f namespace.yaml
kubectl apply -f myapp-deployment.yaml
kubectl apply -f myapp-service.yaml
kubectl rollout status deployment/myapp -n myapp
```

## Manifests Kubernetes

| Arquivo | Descrição |
|---------|-----------|
| `namespace.yaml` | Namespace `myapp` |
| `myapp-deployment.yaml` | 3 réplicas, probes e resource limits |
| `myapp-service.yaml` | LoadBalancer na porta 80 |

## Pipeline CI/CD

`azure-pipelines.yml` — 3 estágios: **Lint → Build Docker → Deploy K8s**

## Estrutura

```
python-docker-app/
├── server.py
├── template.html
├── requirements.txt
├── Dockerfile
├── namespace.yaml
├── myapp-deployment.yaml
├── myapp-service.yaml
└── azure-pipelines.yml
```

## Desenvolvido por

**Leandro Oliveira Moraes**
