# pj_copilot — Portal de formulário RPA

## Objetivo

Página web simples com **quatro campos de formulário** pensada como **portal** para fluxos de **automação RPA** em loop: o robô pode localizar campos por IDs estáveis, preencher valores a cada iteração e submeter ou limpar conforme o fluxo.

## Tecnologias

- HTML5 semântico
- CSS3 (layout responsivo, tema escuro)
- Sem dependências de build ou framework

## Estrutura de pastas

```
pj_copilot/
├── index.html      # Página principal e formulário
├── css/
│   └── styles.css  # Estilos
├── README.md
└── .gitignore
```

## Como rodar em localhost

1. Abra o arquivo `index.html` no navegador (duplo clique ou arrastar para o Chrome/Edge), **ou**
2. Sirva a pasta com um servidor HTTP local, por exemplo:
   - `npx --yes serve .` (na pasta do projeto)
   - Ou extensão “Live Server” no VS Code/Cursor apontando para esta pasta.

## Deploy em produção

- Publique os arquivos estáticos (`index.html` e `css/`) em qualquer hospedagem de site estático (GitHub Pages, Azure Static Web Apps, S3 + CloudFront, Nginx, etc.).
- Configure HTTPS e cabeçalhos de segurança no servidor (CSP, HSTS, `X-Frame-Options`, etc.). Para dúvidas sobre políticas de segurança, a equipe pode consultar **si@befly.com.br**.

## Automação RPA — seletores

| Elemento        | ID / atributo |
|----------------|---------------|
| Formulário     | `#rpa-loop-form` |
| Item 1         | `#rpa-item-1`, `[data-rpa-field="item-1"]` |
| Item 2         | `#rpa-item-2`, `[data-rpa-field="item-2"]` |
| Item 3         | `#rpa-item-3`, `[data-rpa-field="item-3"]` |
| Item 4         | `#rpa-item-4`, `[data-rpa-field="item-4"]` |
| Enviar         | `#rpa-submit` |
| Limpar         | `#rpa-reset` |

O formulário usa `method="get"` e `action="#"` apenas como exemplo; ajuste `action` e `method` se o fluxo precisar enviar dados a um backend.
