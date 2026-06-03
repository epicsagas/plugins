# epicsagas plugins

> Plugins artesanais para desenvolvimento sério assistido por IA — agentes autônomos, compressão de contexto e ferramentas que não atrapalham seu fluxo.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-6-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**Traduções:** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## Plugins

| Plugin | Descrição | Fonte |
|--------|-----------|-------|
| [epic-harness](#epic-harness) | Harness de agente autônomo — 6 comandos poderosos, habilidades auto-evolutivas e hooks invisíveis que protegem, refinam e refletem em cada sessão. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Leitor de documentos otimizado em tokens — comprime silenciosamente arquivos `.md`, `.html` e `.txt`, reduzindo o uso de contexto em até 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor MCP de documentação — busca híbrida BM25+vetorial, lint e gerenciamento de ciclo de vida launchd para documentos de projeto. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicação nativo de IA — fluxos de trabalho autônomos multifase da ideação ao EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Navegador headless como ferramentas MCP — fetch, scrape, extração de markdown, eval JS. Zero configuração, instalação automática. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Grafo de conhecimento de engenharia de software — padroes de projeto, code smells, refatoracoes e analise de arquitetura com revisao de codigo via IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |

---

## Instalação

### Via Claude Code (recomendado)

Adicione o marketplace e instale os plugins:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic-harness@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install obscura-plugin@epicsagas
claude plugin install episteme@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

Todos os plugins prontos para usar — sem configuração adicional.

### epic-harness — instalação independente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (binário pré-compilado):
```bash
cargo binstall epic-harness
```

**Cargo** (compilar do fonte):
```bash
cargo install epic-harness
```

### llm-transpile — instalação independente

**cargo-binstall** (binário pré-compilado):
```bash
cargo binstall llm-transpile
```

**Cargo** (compilar do fonte):
```bash
cargo install llm-transpile
```

### alcove — instalação independente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (binário pré-compilado):
```bash
cargo binstall alcove
```

**Cargo** (compilar do fonte):
```bash
cargo install alcove
```

### episteme — instalação independente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/episteme
```

**cargo-binstall** (binário pré-compilado):
```bash
cargo binstall episteme
```

**Cargo** (compilar do fonte):
```bash
cargo install episteme
```

---

## Detalhes dos plugins

### epic-harness

**Harness de Agente Autônomo**

Construa workflows de agentes que lidam com tarefas complexas e de múltiplas etapas de forma independente. Equipado com 6 comandos poderosos integrados, as habilidades evoluem com o uso. Os hooks de sessão executam automaticamente para proteger seu código, refinar a saída e refletir sobre cada sessão.

**Quando usar:**
- Automatizar ciclos repetitivos de revisão de código, commits e testes
- Definir workflows personalizados por projeto
- Aplicar padrões de comportamento consistentes nas sessões do Claude

**Funcionalidades principais:**
- 6 comandos poderosos integrados (commit, review, test, deploy e mais)
- Sistema de habilidades auto-evolutivas — aprende com padrões de uso e melhora continuamente
- Hooks de guarda de sessão — previne erros e mantém qualidade automaticamente

→ [Fonte & Documentação](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Leitor de Documentos Otimizado em Tokens**

Comprime automaticamente arquivos `.md`, `.html` e `.txt` em cada chamada da ferramenta Read, reduzindo o uso de tokens de contexto em até 40%. Efeito imediato sem alterações no fluxo de trabalho.

**Quando usar:**
- Projetos que referenciam frequentemente documentos grandes ou especificações
- Quando você atinge regularmente os limites da janela de contexto
- Para reduzir custos de tokens em sessões longas

**Funcionalidades principais:**
- Compressão silenciosa — mesma saída, até 40% menos tokens
- Detecta automaticamente formatos `.md` / `.html` / `.txt`
- Totalmente compatível com workflows existentes da ferramenta Read

→ [Fonte & Documentação](https://github.com/epicsagas/llm-transpile)

---

### alcove

**Servidor MCP de Documentação**

Oferece aos agentes de codificação IA acesso sob demanda aos seus documentos de projeto privados via MCP. Busca híbrida BM25+vetorial, lint semântico, validação de documentos e servidor HTTP em segundo plano com modo proxy para resposta instantânea.

**Quando usar:**
- Gerenciar documentação de projeto privada em múltiplos agentes IA
- Buscar decisões de arquitetura, PRDs e runbooks de qualquer agente compatível com MCP
- Aplicar padrões de documentação com validação de políticas e lint semântico

**Funcionalidades principais:**
- Busca híbrida — BM25 + similaridade vetorial com Reciprocal Rank Fusion
- Um doc-repo, qualquer agente — Claude Code, Cursor, Gemini CLI, Codex e mais de 5 outros
- Servidor em segundo plano com modo proxy — elimina a latência de cold-start em novas sessões
- Lint semântico — links quebrados, arquivos órfãos, marcadores obsoletos, datas desatualizadas
- Integração macOS launchd — comandos de ciclo de vida enable/disable/start/stop/restart

→ [Fonte & Documentação](https://github.com/epicsagas/alcove)

---

### velith

**AI-Native Publishing System**

Build books like software. Autonomous multi-phase workflows from blank page to publishable EPUB/PDF.

**Key features:**
- 6-phase pipeline: Onboarding → Ideation → Outlining → Drafting → Editing → Publishing
- 7 genre templates (fiction, non-fiction, technical, screenplay, poetry, game, academic)
- 5-stage editing pipeline with AI-slop detection
- EPUB, PDF, MOBI, TXT, Markdown output

→ [Source & Docs](https://github.com/epicsagas/Velith)

---

### obscura-plugin

**Headless Browser as MCP Tools**

Gives AI agents direct access to the web via five MCP tools. Auto-installs required binaries on first load.

**Key features:**
- Zero config — plugin auto-installs all required binaries
- `obscura_scrape` with configurable concurrency via `obscura-worker`
- `obscura_serve` exposes a CDP WebSocket server for Playwright/Puppeteer
- Stealth mode for anti-detection

→ [Source & Docs](https://github.com/epicsagas/obscura-plugin)

---

### episteme

**Grafo de Conhecimento de Engenharia de Software**

Um grafo de conhecimento consultavel de padroes de projeto, code smells, refatoracoes e leis de arquitetura. A analise de codigo via IA detecta problemas de qualidade, sugere melhorias e fundamenta cada recomendacao em principios de engenharia estabelecidos.

**Quando usar:**
- Revisao de codigo para uso incorreto de padroes, code smells ou violacoes de arquitetura
- Escolha de estrategias de refatoracao com analise de trade-offs baseada em principios
- Aprendizado e aplicacao de leis de engenharia de software (Lei de Conway, Lei de Amdahl, Lei de Gall)

**Recursos principais:**
- Grafo de conhecimento com travessia entre padroes, smells, refatoracoes e leis
- Analise de codigo via IA com deteccao de smells e sugestoes de refatoracao priorizadas
- Multiplas personas de agentes — revisor de codigo, analista de arquitetura, consultor de engenharia

→ [Codigo-fonte e documentacao](https://github.com/epicsagas/Episteme)

---

## Contribuindo

Para enviar um plugin ou sugerir melhorias:

1. Faça um fork deste repositório
2. Adicione sua entrada de plugin em `.claude-plugin/marketplace.json`
3. Abra um Pull Request

Os plugins são mantidos como repositórios GitHub independentes. Este marketplace contém apenas metadados.

---

## Licença

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
