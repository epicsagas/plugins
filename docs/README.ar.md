# إضافات epicsagas

> مجموعة إضافات متميزة للتطوير الاحترافي المدعوم بالذكاء الاصطناعي — وكلاء مستقلون، ضغط السياق، وأدوات تعمل بسلاسة دون مقاطعة.

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

## قائمة الإضافات

| الإضافة | الوصف | المصدر |
|--------|-------|--------|
| [epic-harness](#epic-harness) | إطار الوكلاء المستقلين — 8 أوامر قوية، مهارات تتطور ذاتياً، وخطافات جلسة غير مرئية. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | قارئ مستندات محسن للرموز — يضغط `.md` و `.html` و `.txt` تلقائياً لتوفير حتى 40% من السياق. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | خادم توثيق MCP — بحث هجين BM25+متجه، تدقيق لغوي، وإدارة دورة الحياة عبر launchd. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | نظام نشر أصيل للذكاء الاصطناعي — سير عمل مستقل متعدد المراحل من الفكرة حتى EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | متصفح خفي كأدوات MCP — جلب، كشط، استخراج markdown، وتشغيل JS بدون إعداد مسبق. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | رسم بياني للمعرفة الهندسية — أنماط التصميم، عيوب الشيفرة، إعادة الهيكلة ومراجعة الكود بالذكاء الاصطناعي. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | إدارة خزائن Obsidian — تصنيف الوارد بالذكاء الاصطناعي، تعزيز الرسم البياني، ومزامنة الخزائن. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | مجموعة مهارات الوكيل الشخصي — اكتشاف المشكلات (5 Whys, JTBD)، التحليل المعرفي الذاتي، وتدقيق إطلاق OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | مساعد البحث الأكاديمي — فهرسة الأوراق العلمية (arXiv/Semantic Scholar/PDF)، تحليل الفجوات، وإعداد التقارير. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — جمع المعرفة الضمنية عبر المقابلات لتجميع وتطوير أطر وكلاء مخصصة. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | مسار تطوير مستقل متعدد المحركات — تفويض العمل في Git worktree مع تجاوز الفشل التلقائي (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## التثبيت

### Claude Code (موصى به)

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

## تفاصيل الإضافة

### kanban-dev-lane

**مسار تنفيذ متعدد المحركات لـ Hermes Kanban**

يقوم بتفويض مهام التطوير وإعادة الهيكلة إلى شجرة عمل Git معزولة مع سلسلة **تجاوز فشل تلقائية من 3 مستويات** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) عند نفاد الحصص أو أخطاء 429.

**الميزات الرئيسية:**
- اكتشاف تلقائي لأخطاء 429 ونفاد الحصص مع تبديل سلس للمحركات
- إدارة كاملة لدورة حياة Git worktree المعزولة
- تحكم صارم من Hermes في حالة Kanban والفروقات والاختبارات
- مشغل مدمج: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## الترخيص

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
