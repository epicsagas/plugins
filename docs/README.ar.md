# إضافات epicsagas

> إضافات مصنوعة بعناية للتطوير الجاد بمساعدة الذكاء الاصطناعي — وكلاء مستقلون، وضغط السياق، وأدوات لا تعترض طريقك.

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

## الإضافات

يحمل المركز التشكيلة الأساسية من epiccounty فقط. كل ما عدا ذلك يعيش في مستودعه الخاص مع سوق مستقل بالاسم نفسه (راجع [الإضافات المفردة](#الإضافات-المفردة)).

| الإضافة | الوصف | المصدر |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | هارنس وكلاء مستقل — 8 أوامر ومهارات ذاتية التطور وخطاطيف خفية تحمي كل جلسة وتصقلها وتراجعها. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | قارئ مستندات محسّن للتوكنز — يضغط `.md` و`.html` و`.txt` بصمت عند القراءة فيقلل استهلاك السياق حتى 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | خادم توثيق MCP — بحث هجين BM25+متجهي وفحص lint وإدارة دورة حياة launchd لوثائق المشاريع. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | كتب بمستوى بشري — خط نشر من 6 مراحل، 12 وكيلًا، بوابة الجاهزية، نظام بصري. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | شبكة معرفية لهندسة البرمجيات — أنماط تصميم وروائح كود وإعادة هيكلة وتحليل معماري مع مراجعة كود بالذكاء الاصطناعي. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | إدارة دورة حياة خزنات Obsidian — تصنيف صادر بالذكاء الاصطناعي وتقوية الشبكة وتجديد MOC ومزامنة متعددة الخزنات كمهارات وكيل. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | مجموعة مهارات وكيل شخصية — اكتشاف المشكلات (5 Whys, JTBD, Fishbone) وتحليل ذاتي معرفي وجاهزية نشر OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## التثبيت

### Claude Code (موصى به)

سجّل السوق مرة واحدة ثم ثبّت أي إضافة:

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

كل الإضافات متاحة فورًا.

### Hermes Agent

أمر واحد يثبّت حزمة epiccounty كاملة — 6 إضافات و32 أداة:

```bash
hermes plugins install epicsagas/plugins --enable
```

أو ثبّت الإضافات فرادى وفعّلها:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` حصري لـ Hermes — مضمّن في `.hermes/` بهذا المستودع ولا يُنشر في أسواق Claude/Codex.

**المتطلبات المسبقة:** كل إضافة تغلّف ثنائي CLI بلغة Rust. ثبّت ما تحتاجه فقط:

```bash
brew install epicsagas/tap/alcove          # إضافة alcove
brew install epicsagas/tap/episteme        # إضافة episteme (تحتاج `epis serve` قيد التشغيل)
brew install epicsagas/tap/epic-harness    # إضافة epic-harness
brew install epicsagas/tap/llm-transpile   # إضافة llm-transpile
brew install epicsagas/tap/obsidian-forge  # إضافة obsidian-forge
```

**بداية سريعة — تثبيت كل شيء دفعة واحدة:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## تثبيت مستقل

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # ثنائي مُجهز مسبقًا
cargo install epic-harness    # بناء من المصدر
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

## الإضافات المفردة

هذه الإضافات غادرت المركز. كل مستودع يحمل سوقه الخاص باسم الإضافة نفسها فيثبت بشكل مستقل:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| الإضافة | المستودع | ماذا تفعل |
|--------|------------|-----------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | متصفح بلا واجهة كأدوات MCP — جلب وكشط واستخراج markdown وتقييم JS. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | يجمع ويطوّر هارنس وكيل ذكي مخصصًا من مقابلة. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | مدير إضافات متعدد المضيفين — هيكلة وفحص والتحقق من التثبيت والنشر. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | يحوّل GeekMagic SmallTV إلى شاشة حالة وكيل حية. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | حاصد محتوى خلف تسجيل الدخول — استطلاع API مخفي وجمع بإيقاع بشري. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | محلل استثمار عملات Upbit — مسار مناظرة صعود/هبوط مع بوابات مخاطر. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | محلل استثمار أسهم KRX — مناظرة صعود/هبوط بأدلة تدفقات المستثمرين والبيع على المكشوف وقواعد KRX عبر Toss Securities Open API. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | استخبارات فعاليات الذكاء الاصطناعي/التقنية — مجمّع حتمي من 9 مصادر. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | تصحيح TOEFL iBT بلا اتصال في الأقسام الأربعة باستخدام LLM محلي. |
| wishket-radar | [epicsagas/wishket-radar](https://github.com/epicsagas/wishket-radar) | رادار مشاريع Wishket — بحث وتحليل عميق ومطابقة تقنية لمشاريع الاستعانة بمصادر خارجية. |

---

## تفاصيل الإضافات

### epic-harness

**هارنس وكلاء مستقل**

ابنِ مسارات وكلاء تعالج مهام معقدة متعددة الخطوات باستقلالية. مدعوم بـ 8 أوامر قوية مدمجة ومسار `/orbit` مستقل. المهارات تتطور كلما استخدمتها أكثر. خطاطيف الجلسة تعمل تلقائيًا لحماية الكود وصقل المخرجات ومراجعة كل جلسة.

**متى تستخدمه:**
- أتمتة دورات مراجعة الكود والالتزام والاختبار المتكررة
- تعريف مسارات عمل مخصصة لكل مشروع
- فرض أنماط سلوك متسقة عبر جلسات Claude

**الميزات الرئيسية:**
- 8 أوامر قوية مدمجة تشمل `/orbit` (مسار مستقل بالكامل)
- نظام مهارات ذاتي التطور — يتعلم من أنماط الاستخدام ويتحسن بمرور الوقت
- خطاطيف حماية الجلسة — تمنع الأخطاء وتحافظ على الجودة تلقائيًا

→ [المصدر والتوثيق](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**قارئ مستندات محسّن للتوكنز**

يضغط تلقائيًا ملفات `.md` و`.html` و`.txt` عند كل استدعاء لأداة Read فيقلل استهلاك توكنز السياق حتى 40%. يسري فورًا دون أي تغيير في سير العمل.

**متى تستخدمه:**
- المشاريع التي ترجع كثيرًا إلى مستندات أو مواصفات كبيرة
- عندما تصل بانتظام إلى حدود نافذة السياق
- تقليل تكلفة التوكنز في الجلسات الطويلة

**الميزات الرئيسية:**
- ضغط صامت — المخرجات نفسها بتوكنز أقل حتى 40%
- كشف تلقائي لصيغ `.md` / `.html` / `.txt`
- توافق كامل مع مسارات عمل أداة Read القائمة

→ [المصدر والتوثيق](https://github.com/epicsagas/llm-transpile)

---

### alcove

**خادم توثيق MCP**

يمنح وكلاء البرمجة بالذكاء الاصطناعي وصولًا عند الطلب إلى وثائق مشروعك الخاصة عبر MCP. بحث هجين BM25+متجهي وفحص lint دلالي والتحقق من المستندات وخادم HTTP خلفي بوضع الوكيل لاستجابة فورية.

**متى تستخدمه:**
- إدارة وثائق المشروع الخاصة عبر عدة وكلاء ذكاء اصطناعي
- البحث في قرارات المعمارية وPRDs وأدلة التشغيل من أي وكيل متوافق مع MCP
- فرض معايير التوثيق بالتحقق من السياسات والفحص الدلالي

**الميزات الرئيسية:**
- بحث هجين — BM25 + تشابه متجهي مع Reciprocal Rank Fusion
- مستودع وثائق واحد لأي وكيل — Claude Code وCursor وGemini CLI وCodex وأكثر من 5 آخرين
- خادم خلفي بوضع الوكيل — يزيل زمن البدء البارد في الجلسات الجديدة
- فحص دلالي — روابط مكسورة وملفات يتيمة وعلامات متقادمة وتواريخ منتهية
- تكامل launchd في macOS — أوامر دورة الحياة enable/disable/start/stop/restart

→ [المصدر والتوثيق](https://github.com/epicsagas/alcove)

---

### velith

**نظام نشر أصيل بالذكاء الاصطناعي**

ابنِ الكتب كالبرمجيات. مسارات مستقلة متعددة المراحل من الصفحة البيضاء إلى EPUB/PDF قابل للنشر. سبعة وكلاء متخصصون يتولون البنية والمسودات والاتساق والأسلوب وتصميم الغلاف والتسويق.

**متى تستخدمه:**
- كتابة محتوى طويل مهيكل (رواية، غير روائي، تقني، أكاديمي)
- الحفاظ على اتساق الفصول وصوتها عبر كتاب كامل
- النشر إلى EPUB أو PDF أو MOBI أو Markdown

**الميزات الرئيسية:**
- مسار من 6 مراحل: تهيئة → أفكار → مخطط → مسودة → تحرير → نشر
- 7 قوالب أنواع (رواية، غير روائي، تقني، سيناريو، شعر، لعبة، أكاديمي)
- مسار تحرير من 5 مراحل مع كشف ركاكة الذكاء الاصطناعي
- مخرجات EPUB وPDF وMOBI وTXT وMarkdown عبر Pandoc + Calibre

→ [المصدر والتوثيق](https://github.com/epicsagas/Velith)

---

### episteme

**شبكة معرفية لهندسة البرمجيات**

شبكة معرفية قابلة للاستعلام من أنماط التصميم وروائح الكود وإعادة الهيكلة وقوانين المعمارية. تحليل الكود بالذكاء الاصطناعي يكشف مشكلات الجودة ويقترح تحسينات ويرسّخ كل توصية في مبادئ هندسية راسخة.

**متى تستخدمه:**
- مراجعة الكود لكشف سوء استخدام الأنماط أو روائح الكود أو انتهاكات المعمارية
- اختيار استراتيجيات إعادة الهيكلة بتحليل مقايضات مبادئي
- تعلم قوانين هندسة البرمجيات وتطبيقها (كونواي، أمدال، غال)

**الميزات الرئيسية:**
- شبكة معرفية بجَوَلان عبر الأنماط والروائح وإعادة الهيكلة والقوانين
- تحليل كود بالذكاء الاصطناعي مع كشف الروائح واقتراحات إعادة هيكلة مرتبة
- عدة شخصيات وكيل — مراجع كود ومحلل معماري ومستشار هندسي

→ [المصدر والتوثيق](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**إدارة دورة حياة خزنات Obsidian**

يمنح وكلاء الذكاء الاصطناعي وصولًا قائمًا على المهارات لعمليات خزنات Obsidian — تصنيف صادر بالذكاء الاصطناعي مع توجيه PARA، وتقوية الشبكة المعرفية (روابط خلفية وملاحظات جسور ووسوم تلقائية)، وتجديد MOC، وإصلاح الوسوم/الروابط/frontmatter، ودورات مزامنة كاملة. ثنائي Rust واحد وخزنات متعددة وصفر إعدادات للبدء.

**متى تستخدمه:**
- إدارة خزنة Obsidian (الدماغ الثاني، Zettelkasten، PARA) من جلسات وكلاء الذكاء الاصطناعي
- معالجة ملاحظات الصادر بتصنيف ذكي وتوجيه تلقائي
- تقوية روابط الشبكة المعرفية بين المشاريع والمفاهيم

**الميزات الرئيسية:**
- 5 مهارات وكيل — vault-health وvault-sync وgraph-strengthen وinbox-process وvault-fix
- تصنيف صادر بالذكاء الاصطناعي مع حقن frontmatter وتوجيه PARA
- تقوية الشبكة المعرفية مع تقرير مقاييس قبل/بعد
- دعم خزنات متعددة بإعدادات مشتركة وبرنامج خلفي (macOS)

→ [المصدر والتوثيق](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**مهارات وكيل شخصية**

مجموعة منتقاة من مهارات الوكيل للاستخدام الشخصي والجماعي — اكتشاف المشكلات والتحليل الذاتي المعرفي وجاهزية نشر OSS. لا حاجة لثنائي؛ المهارات تحمّل مباشرة من ملفات markdown.

**متى تستخدمه:**
- اكتشاف المشكلات الحقيقية وتعريفها قبل البناء (أفراد وفرق وشركات ناشئة)
- تحليل أنماط تفكيرك وانحيازاتك المعرفية من سجل المحادثات
- تدقيق جاهزية مشروع OSS للنشر عبر المجتمع وREADME والتوزيع والأمان

**الميزات الرئيسية:**
- `discover` — 5 Whys وJTBD وFishbone والأسئلة السقراطية وخريطة الافتراضات
- `cognitive-audit` — كشف انحيازات قائم على الأدلة وتحليل القرارات و10 روتينات قابلة للتنفيذ
- `oss-dist` — دورة نشر كاملة: معايير المجتمع وREADME واستراتيجية الإطلاق وi18n والأمان

→ [المصدر والتوثيق](https://github.com/epicsagas/epicsagas)

---


## المساهمة

لإرسال إضافة أو اقتراح تحسينات:

1. اعمل fork لهذا المستودع
2. أضف مدخل إضافتك إلى `.claude-plugin/marketplace.json` و`.agents/plugins/marketplace.json`
3. افتح Pull Request

الإضافات تُصان كمستودعات GitHub مستقلة. هذا السوق يحتوي على بيانات وصفية فقط.

---

## الترخيص

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
