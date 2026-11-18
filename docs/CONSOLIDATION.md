# Consolidação do portfólio

O `Analytics_portfolio` passa a concentrar os projetos de Matheus Marcondes, cofundador da GovernandoAI. Os estudos em `ML/` mantêm seus caminhos originais; as plataformas completas ficam em `projects/`. Cada projeto conserva seu ambiente, seus dados, sua licença e sua documentação.

## Origem e preservação

| Origem | Revisão importada | Destino |
| --- | --- | --- |
| `matheusandrean/credit-intelligence-ai` | `589740f3a3674f08f91990234a6b3e21683cf399` | `projects/credit-intelligence-ai/` |
| `matheusandrean/credit-risk-intelligence-web` | `b4d6e69b6fc69631c9f26295fc6934a01efeb800` | `projects/credit-risk-intelligence-web/` |

As revisões de origem incluem as propostas de identidade visual da Fase 1. Os repositórios anteriores permanecem preservados. O histórico Git anterior continua consultável neles; esta importação não reescreve esse histórico nem replica suas branches no portfólio.

O [manifesto de importação](import-manifest.json) registra a revisão e o SHA-256 original de cada arquivo. Código, notebooks, dados, licenças e testes foram copiados sem alteração adicional. Somente os READMEs dos projetos receberam ajustes nos caminhos de clonagem, CI, navegação e execução. O workflow original dentro do projeto Python permanece como registro da origem, mas o GitHub executa apenas a versão adaptada na raiz do portfólio.

## Execução e CI

Execute os comandos Python a partir de `projects/credit-intelligence-ai/`; `src`, `api` e `app` continuam pertencendo àquele projeto. Seu `PROJECT_ROOT` permanece relativo à localização do módulo. Não há instalação global que misture suas dependências com os estudos de `ML/`.

A [CI do projeto Python](../.github/workflows/credit-intelligence-ai.yml) roda a partir da subpasta correta, preserva lint, testes, auditorias e build Docker, e publica a cobertura a partir do novo caminho. O cache aponta para o `pyproject.toml` importado. Mudanças nesse projeto ou no workflow acionam a CI. A configuração de pre-commit da raiz é restrita ao projeto Python; seu baseline de detecção de segredos tem os caminhos prefixados para o monorepositório.

Para o dashboard, sirva `projects/credit-risk-intelligence-web/` por HTTP, conforme o README principal. O dataset e os caminhos relativos dos assets continuam juntos. Nenhuma hospedagem nova foi publicada nesta consolidação.

## Perfil e próxima fase

`profile/README.md` e seu banner são a fonte do perfil profissional. A cópia no repositório especial `matheusandrean/matheusandrean` é necessária para o GitHub mostrá-la na página do usuário. Os links com `main` funcionarão após o merge da consolidação; valide e faça o merge do portfólio antes do PR do perfil.

O Sentinel será implementado em `projects/sentinel/` na Fase 2. Sua menção no README é planejamento, sem métricas ou funcionalidades antifraude reivindicadas.
