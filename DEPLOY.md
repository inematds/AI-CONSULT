# Guia de Deploy - AI Consult

Instruções completas para deploy da aplicação em VPS com Docker.

## 1️⃣ Requisitos da VPS

### Especificações Mínimas:
- **CPU**: 1 vCPU (2 vCPUs recomendado)
- **RAM**: 2GB mínimo (4GB recomendado)
- **Disco**: 10GB SSD
- **OS**: Ubuntu 20.04+ ou Debian 11+
- **Porta**: 8888 liberada no firewall

### Provedores Recomendados:
- **DigitalOcean** - Droplet $6/mês (1GB RAM)
- **Vultr** - $6/mês
- **Linode** - $5/mês
- **AWS Lightsail** - $5/mês
- **Hetzner** - €4.5/mês (melhor custo-benefício)
- **Contabo** - €4/mês

## 2️⃣ Instalação na VPS (Passo a Passo)

### Conectar na VPS:
```bash
ssh root@seu-ip-vps
```

### Instalar Docker:
```bash
# Atualizar sistema
apt update && apt upgrade -y

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Instalar Docker Compose
apt install docker-compose-plugin -y

# Verificar instalação
docker --version
docker compose version
```

### Clonar o repositório:
```bash
# Ir para diretório home
cd ~

# Clonar projeto
git clone https://github.com/inematds/AI-CONSULT.git
cd AI-CONSULT
```

### Configurar variáveis de ambiente:
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com suas chaves de API
nano .env
```

Dentro do `.env`, adicione:
```env
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxxxx
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxx
```

Salve com `Ctrl+O`, `Enter`, `Ctrl+X`

### Rodar a aplicação:
```bash
# Iniciar em background
docker compose up -d

# Ver logs (opcional)
docker compose logs -f
```

### Acessar a aplicação:
```
http://SEU-IP-VPS:8888
```

## 3️⃣ Configurar Firewall (Segurança)

```bash
# Instalar UFW
apt install ufw -y

# Permitir SSH
ufw allow 22/tcp

# Permitir porta da aplicação
ufw allow 8888/tcp

# Ativar firewall
ufw enable

# Verificar status
ufw status
```

## 4️⃣ Configurar Domínio (Opcional mas Recomendado)

Se você tem um domínio (ex: `estrategia-ia.com.br`):

### Instalar Nginx como proxy reverso:
```bash
apt install nginx -y
```

### Configurar Nginx:
```bash
nano /etc/nginx/sites-available/ai-consult
```

Adicione:
```nginx
server {
    listen 80;
    server_name estrategia-ia.com.br www.estrategia-ia.com.br;

    location / {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Ativar configuração:
```bash
ln -s /etc/nginx/sites-available/ai-consult /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

### Adicionar HTTPS (SSL gratuito):
```bash
# Instalar Certbot
apt install certbot python3-certbot-nginx -y

# Obter certificado SSL
certbot --nginx -d estrategia-ia.com.br -d www.estrategia-ia.com.br
```

Agora acesse via: `https://estrategia-ia.com.br`

## 5️⃣ Comandos Úteis

```bash
# Ver logs em tempo real
docker compose logs -f

# Parar aplicação
docker compose down

# Reiniciar aplicação
docker compose restart

# Atualizar código (quando fizer mudanças)
git pull
docker compose up -d --build

# Ver uso de recursos
docker stats

# Acessar container
docker compose exec ai-consult bash

# Ver arquivos gerados
ls -lh output/
```

## 6️⃣ Monitoramento (Opcional)

```bash
# Instalar htop para monitorar recursos
apt install htop -y
htop

# Ver espaço em disco
df -h

# Ver uso de memória
free -h
```

## 7️⃣ Backup Automático (Recomendado)

```bash
# Criar script de backup
nano /root/backup-ai-consult.sh
```

Adicione:
```bash
#!/bin/bash
tar -czf /root/backups/ai-consult-$(date +%Y%m%d).tar.gz -C /root AI-CONSULT/output
find /root/backups -name "ai-consult-*.tar.gz" -mtime +7 -delete
```

```bash
# Tornar executável
chmod +x /root/backup-ai-consult.sh

# Criar diretório de backups
mkdir -p /root/backups

# Adicionar ao cron (rodar todo dia às 2am)
crontab -e
```

Adicione:
```
0 2 * * * /root/backup-ai-consult.sh
```

## 8️⃣ Troubleshooting

### Aplicação não inicia:
```bash
# Ver logs de erro
docker compose logs

# Verificar se a porta está em uso
netstat -tulpn | grep 8888

# Reiniciar Docker
systemctl restart docker
docker compose up -d
```

### Erro de API Keys:
```bash
# Verificar variáveis de ambiente
docker compose exec ai-consult env | grep API

# Recriar .env e reiniciar
nano .env
docker compose down
docker compose up -d
```

### Sem espaço em disco:
```bash
# Limpar containers antigos
docker system prune -a

# Limpar arquivos de output antigos
cd ~/AI-CONSULT/output
rm -rf empresa-antiga/
```

### Performance lenta:
```bash
# Verificar recursos
htop
docker stats

# Aumentar RAM da VPS se necessário
# Ou limitar uso do container no docker-compose.yml
```

## 🎯 Checklist Final

- [ ] VPS com Ubuntu/Debian instalado
- [ ] Docker e Docker Compose instalados
- [ ] Projeto clonado do GitHub
- [ ] Arquivo `.env` configurado com API keys
- [ ] Aplicação rodando via `docker compose up -d`
- [ ] Firewall configurado (portas 22 e 8888)
- [ ] Nginx configurado (se usar domínio)
- [ ] SSL configurado (se usar domínio)
- [ ] Backup configurado

## 🔐 Segurança Adicional

### Desabilitar login root via SSH:
```bash
nano /etc/ssh/sshd_config
```

Altere:
```
PermitRootLogin no
```

```bash
systemctl restart sshd
```

### Criar usuário não-root:
```bash
adduser deploy
usermod -aG sudo deploy
usermod -aG docker deploy
```

### Configurar fail2ban:
```bash
apt install fail2ban -y
systemctl enable fail2ban
systemctl start fail2ban
```

## 📊 Monitoramento de Custos

### Custos estimados por análise:
- **Modo Rápido**: ~$0.05 por empresa
- **Modo Completo**: ~$0.50 por empresa

### Custos mensais de infraestrutura:
- **VPS**: $5-10/mês
- **Domínio**: $10-15/ano
- **SSL**: Grátis (Let's Encrypt)

**Total estimado**: ~$6-11/mês + custos de API por uso

## 📞 Suporte

Em caso de problemas:
1. Verificar logs: `docker compose logs -f`
2. Consultar issues no GitHub: https://github.com/inematds/AI-CONSULT/issues
3. Revisar documentação: README.md e CLAUDE.md
