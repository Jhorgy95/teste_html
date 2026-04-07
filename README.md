# Formulário de cadastro (HTML)

Página estática de demonstração com formulário simples (nome, sobrenome, idade) e feedback visual ao enviar.

## Objetivo

Servir como base para testes (por exemplo, automação/RPA) ou como exemplo mínimo de formulário em HTML, CSS e JavaScript puro.

## Tecnologias

- HTML5
- CSS (inline na página)
- JavaScript (vanilla, sem frameworks)

## Estrutura do projeto

```
.
├── index.html    # Página única com formulário e script
├── .gitignore    # Ignora .env, ficheiros de sistema e IDE
└── README.md
```

## Como executar em localhost

1. Clone o repositório ou abra a pasta do projeto.
2. Abra `index.html` no navegador (duplo clique ou arrastar para o Chrome/Edge/Firefox).

Opcional com servidor local (evita algumas restrições de ficheiros locais):

```bash
# Python 3
python -m http.server 8080
```

Depois aceda a `http://localhost:8080`.

## Publicação em produção (GitHub Pages)

1. No GitHub: **Settings** → **Pages**.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Branch: `main` ou `master`, pasta **/ (root)**.
4. Guarde; o site ficará em `https://<seu-usuario>.github.io/<nome-do-repo>/` (URL exata aparece na própria página de Settings → Pages).

Após cada `git push`, o GitHub Pages atualiza em poucos minutos.

## Segurança (recomendações para ambientes reais)

Em hospedagem própria ou atrás de um proxy, considere cabeçalhos HTTP como **Content-Security-Policy**, **X-Frame-Options**, **X-Content-Type-Options**, **Strict-Transport-Security**, **Referrer-Policy** e **Permissions-Policy**. Dúvidas sobre política de segurança: **si@befly.com.br**.
