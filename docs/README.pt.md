# plugins epicsagas

> Plugins artesanais para desenvolvimento sério assistido por IA — agentes autônomos, compressão de contexto e ferramentas que não atrapalham.

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

## Plugins

O hub carrega apenas o lineup principal da epiccounty. Todo o resto vive no próprio repositório com um marketplace independente de mesmo nome (veja [Plugins individualizados](#plugins-individualizados)).

| Plugin | Descrição | Fonte |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Harness de agentes autônomos — 8 comandos, habilidades autoevolutivas e hooks invisíveis que guardam, polem e refletem cada sessão. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Leitor de documentos otimizado para tokens — comprime silenciosamente `.md`, `.html` e `.txt` na leitura, cortando o contexto em até 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor MCP de documentação — busca híbrida BM25+vetorial, lint e gerenciamento de ciclo de vida launchd para docs de projeto. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicação nativo de IA — fluxos autônomos multifase da ideação ao EPUB/PDF. Construa livros como software. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Grafo de conhecimento de engenharia de software — padrões, code smells, refactorings e análise de arquitetura com revisão de código por IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gestão de ciclo de vida de cofres Obsidian — classificação de caixa de entrada com IA, reforço do grafo, regeneração de MOCs e sincronização multico_fre como skills de agente. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Coleção de skills de agente pessoais — descoberta de problemas (5 Whys, JTBD, Fishbone), introspecção e prontidão de publicação OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## Instalação

### Claude Code (recomendado)

Registre o marketplace uma vez e instale qualquer plugin:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install episteme@epicsagas
claude plugin install obsidian-forge@epicsagas
claude plugin install epicsagas@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

Todos os plugins ficam disponíveis imediatamente.

### Hermes Agent

Um comando instala o suite epiccounty completo — 6 plugins, 32 ferramentas:

```bash
hermes plugins install epicsagas/plugins --enable
```

Ou instale e ative plugins individuais:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` é exclusivo do Hermes — empacotado em `.hermes/` deste repo, não publicado nos marketplaces Claude/Codex.

**Pré-requisitos:** Cada plugin envolve um binário CLI Rust. Instale os que precisar:

```bash
brew install epicsagas/tap/alcove          # plugin alcove
brew install epicsagas/tap/episteme        # plugin episteme (requer `epis serve` em execução)
brew install epicsagas/tap/epic-harness    # plugin epic-harness
brew install epicsagas/tap/llm-transpile   # plugin llm-transpile
brew install epicsagas/tap/obsidian-forge  # plugin obsidian-forge
```

**Início rápido — instalar tudo de uma vez:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Instalação autônoma

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # binário pré-compilado
cargo install epic-harness    # compilar da fonte
```

### transpile

```bash
brew install epicsagas/tap/llm-transpile
cargo binstall llm-transpile
cargo install llm-transpile
```

### alcove

```bash
brew install epicsagas/tap/alcove
cargo binstall alcove
cargo install alcove
```

### episteme

```bash
brew install epicsagas/tap/episteme
cargo binstall episteme
cargo install episteme
```

### obsidian-forge

```bash
brew install epicsagas/tap/obsidian-forge
cargo binstall obsidian-forge
cargo install obsidian-forge
```

---

## Plugins individualizados

Estes plugins saíram do hub. Cada repositório traz seu próprio marketplace com o nome do plugin, então instalam de forma autônoma:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| Plugin | Repositório | O que faz |
|--------|------------|-----------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Navegador headless como ferramentas MCP — fetch, scrape, extração markdown, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Compila e evolui um harness de agente IA personalizado a partir de uma entrevista. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Gerenciador de plugins multihospedeiro — scaffold, doctor, validação de instalação, publicação. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | Transforma uma GeekMagic SmallTV em display de estado de agente ao vivo. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Colheitador de conteúdo atrás de login — reconhecimento de API oculta, coleta em ritmo humano. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Analista de investimento em cripto da Upbit — pipeline de debate alta/baixa com portões de risco. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | Analista de ações da KRX — debate alta/baixa com evidência de fluxos e vendas a descoberto e regras KRX, via Open API da Toss Securities. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | Inteligência de eventos IA/tech — agregador determinístico de 9 fontes. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Correção offline do TOEFL iBT nas 4 seções com um LLM local. |

---

## Detalhes dos plugins

### epic-harness

**Harness de agentes autônomos**

Construa fluxos de agente que tratam tarefas complexas de múltiplas etapas de forma independente. Alimentado por 8 comandos power integrados e um pipeline `/orbit` autônomo. Habilidades evoluem quanto mais você usa. Hooks de sessão rodam automaticamente para guardar seu código, polir a saída e refletir sobre cada sessão.

**Quando usar:**
- Automatizar ciclos repetitivos de revisão, commit e testes
- Definir fluxos de trabalho customizados por projeto
- Impor padrões de comportamento consistentes entre sessões Claude

**Recursos-chave:**
- 8 comandos power integrados incluindo `/orbit` (pipeline totalmente autônomo)
- Sistema de habilidades autoevolutivas — aprende com padrões de uso e melhora com o tempo
- Hooks de guarda de sessão — previne erros e mantém a qualidade automaticamente

→ [Fonte e documentação](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Leitor de documentos otimizado para tokens**

Comprime automaticamente arquivos `.md`, `.html` e `.txt` a cada chamada da ferramenta Read, cortando o uso de tokens de contexto em até 40%. Surte efeito imediato, sem mudanças no fluxo de trabalho.

**Quando usar:**
- Projetos que referenciam com frequência documentos ou especificações grandes
- Quando você atinge limites de janela de contexto com regularidade
- Reduzir custos de tokens em sessões longas

**Recursos-chave:**
- Compressão silenciosa — mesma saída, até 40% menos tokens
- Detecção automática dos formatos `.md` / `.html` / `.txt`
- Totalmente compatível com os fluxos existentes da ferramenta Read

→ [Fonte e documentação](https://github.com/epicsagas/llm-transpile)

---

### alcove

**Servidor MCP de documentação**

Dá a agentes de codificação IA acesso sob demanda à sua documentação privada de projeto via MCP. Busca híbrida BM25+vetorial, lint semântico, validação de documentos e servidor HTTP em segundo plano com modo proxy para resposta instantânea.

**Quando usar:**
- Gerenciar documentação privada de projeto entre múltiplos agentes IA
- Buscar decisões de arquitetura, PRDs e runbooks a partir de qualquer agente compatível com MCP
- Impor padrões de documentação com validação de políticas e lint semântico

**Recursos-chave:**
- Busca híbrida — BM25 + similaridade vetorial com Reciprocal Rank Fusion
- Um repositório de docs, qualquer agente — Claude Code, Cursor, Gemini CLI, Codex e 5+ outros
- Servidor em segundo plano com modo proxy — elimina latência de inicialização em sessões novas
- Lint semântico — links quebrados, arquivos órfãos, marcadores desatualizados, datas vencidas
- Integração launchd do macOS — comandos de ciclo de vida enable/disable/start/stop/restart

→ [Fonte e documentação](https://github.com/epicsagas/alcove)

---

### velith

**Sistema de publicação nativo de IA**

Construa livros como software. Fluxos autônomos multifase da página em branco ao EPUB/PDF publicável. Sete agentes especializados cuidam de estrutura, redação, continuidade, estilo, capa e marketing.

**Quando usar:**
- Escrever conteúdo longo estruturado (ficção, não-ficção, técnico, acadêmico)
- Manter consistência e voz entre capítulos em um livro inteiro
- Publicar em EPUB, PDF, MOBI ou Markdown

**Recursos-chave:**
- Pipeline de 6 fases: Onboarding → Ideação → Esboço → Redação → Edição → Publicação
- 7 modelos por gênero (ficção, não-ficção, técnico, roteiro, poesia, jogo, acadêmico)
- Pipeline de edição de 5 estágios com detecção de AI-slop
- Saída EPUB, PDF, MOBI, TXT, Markdown via Pandoc + Calibre

→ [Fonte e documentação](https://github.com/epicsagas/Velith)

---

### episteme

**Grafo de conhecimento de engenharia de software**

Um grafo de conhecimento consultável de padrões de projeto, code smells, refactorings e leis de arquitetura. A análise de código por IA detecta problemas de qualidade, sugere melhorias e fundamenta cada recomendação em princípios de engenharia estabelecidos.

**Quando usar:**
- Revisar código por uso indevido de padrões, code smells ou violações de arquitetura
- Escolher estratégias de refactoring com análise de trade-offs principiada
- Aprender e aplicar leis da engenharia de software (Conway, Amdahl, Gall)

**Recursos-chave:**
- Grafo de conhecimento com travessia entre padrões, smells, refactorings e leis
- Análise de código por IA com detecção de smells e sugestões de refactoring ranqueadas
- Múltiplas personas de agente — revisor de código, analista de arquitetura, conselheiro de engenharia

→ [Fonte e documentação](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Gestão de ciclo de vida de cofres Obsidian**

Dá a agentes IA acesso por habilidades a operações de cofres Obsidian — classificação de caixa de entrada por IA com roteamento PARA, reforço do grafo de conhecimento (backlinks, notas-ponte, tags automáticas), regeneração de MOCs, reparo de tags/links/frontmatter e ciclos completos de sincronização. Binário Rust único, multico_fre, configuração zero para começar.

**Quando usar:**
- Gerenciar um cofre Obsidian (Second Brain, Zettelkasten, PARA) a partir de sessões de agentes IA
- Processar notas da caixa de entrada com classificação IA e roteamento automático
- Reforçar conexões do grafo de conhecimento entre projetos e conceitos

**Recursos-chave:**
- 5 skills de agente — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- Classificação de caixa de entrada por IA com injeção de frontmatter e roteamento PARA
- Reforço do grafo de conhecimento com relatório de métricas antes/depois
- Suporte multico_fre com configurações compartilhadas e daemon em segundo plano (macOS)

→ [Fonte e documentação](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Skills de agente pessoais**

Um conjunto curado de skills de agente para uso pessoal e em equipe — descoberta de problemas, autoanálise cognitiva e prontidão de publicação OSS. Sem binário necessário; skills carregam diretamente de arquivos markdown.

**Quando usar:**
- Descobrir e definir problemas reais antes de construir (indivíduos, equipes, startups)
- Analisar seus próprios padrões de pensamento e vieses cognitivos a partir do histórico de conversa
- Auditar a prontidão de publicação de um projeto OSS em comunidade, README, distribuição e segurança

**Recursos-chave:**
- `discover` — 5 Whys, JTBD, Fishbone, questionamento socrático, mapeamento de suposições
- `cognitive-audit` — detecção de vieses baseada em evidências, análise de decisões, 10 rotinas acionáveis
- `oss-dist` — ciclo completo de publicação: padrões de comunidade, README, estratégia de lançamento, i18n, segurança

→ [Fonte e documentação](https://github.com/epicsagas/epicsagas)

---


## Contribuindo

Para enviar um plugin ou sugerir melhorias:

1. Faça fork deste repositório
2. Adicione sua entrada de plugin a `.claude-plugin/marketplace.json` e `.agents/plugins/marketplace.json`
3. Abra um Pull Request

Plugins são mantidos como repositórios GitHub independentes. Este marketplace contém apenas metadados.

---

## Licença

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
