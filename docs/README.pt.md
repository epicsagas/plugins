# epicsagas plugins

> Coleção de plugins de alto nível para desenvolvimento assistido por IA profissional — agentes autônomos, compressão de contexto e ferramentas não invasivas.

<p align="center">
  <a href="https://github.com/epicsagas/plugins/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ffd700&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=2ecc71&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/issues"><img alt="Issues" src="https://img.shields.io/github/issues/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ff6b6b&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=58a6ff&logo=git&logoColor=white" /></a>
</p>
<p align="center">
  <a href="../LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-3fb950?style=for-the-badge&labelColor=0d1117" /></a>
  <a href="https://buymeacoffee.com/epicsaga"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/buy_me_a_coffee-FFDD00?style=for-the-badge&labelColor=0d1117&logo=buymeacoffee&logoColor=black" /></a>
</p>

**Translations:** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## Lista de Plugins

| Plugin | Descrição | Fonte |
|--------|-----------|-------|
| [epic-harness](#epic-harness) | Harness de agente autônomo — 8 comandos, habilidades autoevolutivas e hooks de sessão invisíveis. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Leitor de documentos otimizado para tokens — comprime `.md`, `.html`, `.txt` automaticamente, economizando até 40% de contexto. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor de documentação MCP — busca híbrida BM25+vetorial, linter e gerenciamento com launchd. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicação nativo de IA — fluxo multifásico autônomo desde a concepção até EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Navegador headless como ferramentas MCP — fetch, scrape, extração de markdown e JS eval sem configuração. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Grafo de conhecimento de engenharia de software — padrões de design, code smells, refatorações e revisão de código com IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gerenciamento de cofres Obsidian — classificação de caixa de entrada por IA, fortalecimento de grafo e sincronização. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Coleção de habilidades de agentes — descoberta de problemas (5 Whys, JTBD), autoanálise cognitiva e auditoria OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Assistente de pesquisa acadêmica — indexação de artigos (arXiv/Semantic Scholar/PDF), análise de lacunas e relatórios. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — extrai conhecimento tácito via entrevistas para compilar harnesses personalizados. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Linha de implementação autônoma multimotor — delegação em Git worktree com failover (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Instalação

### Claude Code (recomendado)

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic-harness@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install obscura-plugin@epicsagas
claude plugin install episteme@epicsagas
claude plugin install obsidian-forge@epicsagas
claude plugin install epicsagas@epicsagas
claude plugin install research@epicsagas
claude plugin install byoh@epicsagas
```

### Hermes Agent

```bash
hermes plugins install epicsagas/plugins --enable
hermes plugins enable kanban-dev-lane
```

---

## Detalhes do Plugin

### kanban-dev-lane

**Linha de implementação multimotor para Hermes Kanban**

Delega tarefas de desenvolvimento e refatoração para um Git worktree isolado com uma cadeia automática de **failover em 3 níveis** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) em caso de esgotamento de cotas ou erros 429.

**Recursos principais:**
- Detecção automática de 429 e cotas esgotadas com alternância fluida
- Gerenciamento de ciclo de vida do Git worktree isolado
- Controle estrito de Hermes sobre status do Kanban, diffs e testes
- Script de execução incluído: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Licença

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
