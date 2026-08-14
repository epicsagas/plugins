# kanban-dev-lane installed

The `kanban-dev-lane` skill is now available.

## 1. Verify Engine CLIs

Check availability of delegation engines:

```bash
command -v claudy && claudy --version
command -v codex && codex --version
command -v agy && agy --version
```

- **Tier 1 (Primary)**: `claudy -p "<prompt>" --yolo`
- **Tier 2 (Fallback 1)**: `codex exec "<prompt>" < /dev/null --dangerously-bypass-approvals-and-sandbox --ephemeral` (or `codex --yolo`)
- **Tier 3 (Fallback 2)**: `agy --dangerously-skip-permissions -p "<prompt>"` (alias: `agyd`)
- **Tier 4 (Final)**: Hermes native direct execution.

## 2. Dev Profile Setup

Add this block to your dev profile's `SOUL.md` (e.g. `~/.hermes/profiles/dev-lead/SOUL.md`):

```markdown
## Implementation Delegation (kanban-dev-lane)
- 구현 태스크(DEV-*)는 직접 90 iteration을 전부 소모하기 전에 `kanban-dev-lane` 스킬로 위임을 우선 고려.
- **소유권**: Hermes(dev-lead)가 worktree 생성·검증·테스트 재실행·`kanban_complete` handoff를 소유. 외부 엔진은 구현 입력만 담당.
- **3단계 자동 폴백 체인**:
  1. **Tier 1 (기본)**: `claudy -p "<프롬프트>" --yolo`
  2. **Tier 2 (1차 폴백)**: `codex exec ...` (또는 `codex --yolo`)
  3. **Tier 3 (2차 폴백)**: `agyd` (`agy --dangerously-skip-permissions -p ...`)
  4. **Tier 4 (최종)**: Hermes 워커 직접 수정
- **러너 호출**: `python3 ~/.hermes/plugins/kanban-dev-lane/scripts/lane_runner.py --prompt-file <경로> --worktree <경로> --engines claudy,codex,agyd`
```
