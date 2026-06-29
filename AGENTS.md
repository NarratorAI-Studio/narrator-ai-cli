# GridLtd Organization Rules

This file is auto-synced to all repositories across the enterprise.
Do not edit directly — update the source at Gridltd-DevOps/.github/org-rules.md

## Team Directory

When you need to look up team members, fetch the current internal team
directory before acting:

```bash
gh api repos/Gridltd-DevOps/.github/contents/team/members.yml -q '.content' | base64 -d
```

Identity rules:

- `github` is the stable GitHub login. Use it for GitHub operations: assign issues/PRs, request reviews, mention users, CODEOWNERS, branch/commit attribution checks.
- `lark_open_id` is the stable Feishu/Lark user id. Use it for Feishu direct messages or user mentions.
- `email` is the stable email destination. Use it for mail only.
- `github_name` is GitHub display metadata and is not stable or guaranteed unique.
- `alias`, `name`, `role`, `responsibility`, and `profile` are human-readable metadata only; never use them directly as external action identifiers.

If the user gives only a name, alias, display name, role, or other ambiguous
human label, resolve it against `team/members.yml` first. If more than one
member matches, or if the match depends on memory rather than the current file,
pause and ask the user to confirm the exact `github`, `lark_open_id`, or
`email` before taking any external side effect.

Preferred deterministic resolver:

```bash
python .github/workflows/scripts/members/resolve_team_member.py --members-file team/members.yml --query "<name-or-alias-or-login>"
```

Use `--check` before changing the directory or agent identity rules:

```bash
python .github/workflows/scripts/members/resolve_team_member.py --members-file team/members.yml --check
```

## Organization Standards

### Communication

- Communicate in Chinese, keep technical terms in English
- Commit messages and PR descriptions must be in English

### Git Flow Branching Model

| Branch | Purpose | Merges to |
|--------|---------|-----------|
| `main` | Production-ready code, always stable | — |
| `develop` | Integration branch for features | `main` (via release) |
| `feature/<issue-id>-<short-desc>` | New features | `develop` |
| `release/<version>` | Release preparation & QA | `main` + `develop` |
| `hotfix/<issue-id>-<short-desc>` | Urgent production fixes | `main` + `develop` |

- Branch names use lowercase + hyphens, e.g. `feature/42-user-auth`
- Delete branches after merge

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code restructuring (no behavior change) |
| `docs` | Documentation only |
| `chore` | Build, CI, dependencies, tooling |
| `test` | Add or update tests |
| `style` | Formatting, whitespace (no logic change) |
| `perf` | Performance improvement |

- `scope` should reflect the module or area, e.g. `feat(auth): add SSO login`
- Breaking changes: add `BREAKING CHANGE:` in footer or `!` after type, e.g. `feat(api)!: remove v1 endpoints`

### Pull Requests

- PR title follows the same Conventional Commits format
- Current hard PR gate requires exact `## Related Issue`, non-empty
  `## Summary`, non-empty `## Test Plan`, and a valid issue link keyword.
- Use `Closes`, `Fixes`, or `Resolves` when the PR completes the issue. Use
  `Refs` only for epic, cross-cutting, ADR, roadmap, ledger, or advisory parent
  work that intentionally remains open.
- PR governance reads GitHub-native metadata first: title, base/head branch,
  draft state, labels, assignees, review requests, review decision, merge
  state, status checks, closing issues, parent/sub-issues, dependencies, and
  Project fields when scope is available. PR body is review evidence and
  fallback, not the sole source of truth.
- New PR metadata sections are advisory until explicitly promoted through the
  approval path: `## Native Metadata`, `## Change Scope`, `## Impact`,
  `## AC Verification`, `## Rollback`, `## Risk`, and
  `## Agent Exposure Block`.
- `## Agent Exposure Block` is required for Agent-authored, Agent-executed, or
  materially Agent-edited PRs once the repository validator requires it. Until
  then, Agents should add it whenever they touch a PR.
- Require at least 1 approval before merge
- Use **Squash Merge** for feature → develop; **Merge Commit** for release/hotfix → main
- Keep PRs focused — one concern per PR

### Issue Creation

When creating issues (via CLI, API, or any Agent tool), you MUST follow the
organization issue templates. The issue gate validates API/CLI-created bodies as
well as form-created bodies, adds `needs-template` or `needs-info` on failure,
and comments with deterministic remediation. Stale `needs-template` cleanup is a
separate conservative workflow and is not a substitute for creating compliant
issues.

Execution-ready issues must keep Discovery and Delivery separated. Raw
Research, Discussion, or RFC issues may contain rejected assumptions and must not
be used as the direct closing source for Delivery PRs. Delivery work must link
an accepted Requirement / PRD, Initiative, Bug, Regression, Incident, Test
failure, operational exception, or approval issue.

**Bug Report** — label: `bug`, required fields:
- `### Action Block` — goal, owner, next action, decision maker, by-when
- `### Upstream / Previous Step` — source report, incident, test failure, or previous issue
- `### Environment` — OS, runtime, browser
- `### Steps to Reproduce` — minimal reproduction steps
- `### Expected Behavior`
- `### Actual Behavior`
- `### Severity`
- `### Impact`
- `### Affected Scope`
- `### Original Requirement`
- `### Boundary / Non-goals`
- `### Fix Checklist`
- `### Acceptance Criteria`
- `### Verification / Regression`
- `### Next Step`
- `### Agent Execution Prompt` — final Agent handoff instructions

**Feature Request** — label: `feature`, required fields:
- `### Action Block` — goal, owner, next action, decision maker, by-when
- `### Lifecycle Phase` — Discovery / Definition / Delivery planning / Migration
- `### Source / Trigger` — customer, research, PMO, incident, or prior issue
- `### Description` — what you are proposing
- `### Use Case` — who benefits, in what scenario
- `### Expected Outcome` — measurable result
- `### Impact Scope`
- `### In Scope`
- `### Out of Scope`
- `### Decision Status`
- `### Decision Maker`
- `### Acceptance Criteria`
- `### Validation Plan`
- `### Next Step`
- `### Agent Execution Prompt` — final Agent handoff instructions

**Task** — label: `task`, required fields:
- `### Action Block` — goal, owner, next action, decision maker, by-when
- `### Upstream / Previous Step` — accepted source issue or explicit exception
- `### Work Type` — one of: Refactor, Chore, Docs, Perf, Test, Style
- `### Task Description` — what and why
- `### Impact`
- `### Affected Scope`
- `### Original Requirement`
- `### Boundary / Non-goals`
- `### Checklist`
- `### Acceptance Criteria` — checklist
- `### Verification / Regression`
- `### Next Step`
- `### Agent Execution Prompt` — final Agent handoff instructions

**Regression** — label: `regression`, required fields:
- `### Action Block` — goal, owner, next action, decision maker, by-when
- `### Upstream / Previous Step` — source report, test failure, release verification, or previous issue
- `### Description` — what regressed
- `### Original Issue` — link to the original fix
- `### Steps to Reproduce`
- `### Severity`
- `### Impact`
- `### Affected Scope`
- `### Original Requirement`
- `### Boundary / Non-goals`
- `### Fix Checklist`
- `### Acceptance Criteria`
- `### Verification / Regression`
- `### Next Step`
- `### Agent Execution Prompt` — final Agent handoff instructions

**RFC / Design Discussion** — label: `rfc`, required fields:
- `### Action Block` — goal, owner, next action, decision maker, by-when
- `### Source / Trigger` — issue, PR, incident, product request, or governance gap
- `### Context` — situation or prior discussion
- `### Problem` — decision or clarification needed
- `### Options Considered` — serious options and tradeoffs
- `### Decision Status`
- `### Decision Maker`
- `### Proposed Direction` — recommended first direction
- `### Acceptance Criteria` — success criteria for the decision or pilot
- `### Rejected Paths`
- `### Required Evidence Before Delivery`
- `### Next Step`
- `### Agent Execution Prompt` — final Agent handoff instructions

`### Agent Execution Prompt` must be the final section on the main lifecycle
issue templates above and must include:

```md
- Execution mode:
- Agent should:
- Agent must not:
- Required context to read:
- Expected output:
- Stop conditions:
```

The prompt cannot override `Boundary / Non-goals`, rejected paths, required
evidence, approval gates, repository rules, security boundaries,
deploy/release restrictions, or live governance restrictions. If `Original
Requirement`, `Boundary / Non-goals`, or `Agent Execution Prompt` is missing on
execution-ready work, Agents must stop before implementation and ask the owner
or decision maker.

### GitHub-Native Workflow

GitHub is the canonical workspace for technical context. Email is an attention
routing channel only: link the canonical Issue / PR / Project, summarize owner
and next action, and copy any new technical input back to GitHub.

Use the v0.1 workflow baseline at
`https://github.com/Gridltd-DevOps/.github/blob/main/docs/github-native-workflow-v0.1.md`
for Issue lifecycle, PR linked-issue policy, closure outcomes, and pilot
rulesets.

Execution-ready work must make the owner, next action, decision status,
acceptance criteria, and verification or closure outcome discoverable without
reading multiple email chains.

### Agent CI/CD Flow Rules

Agents must classify the change type from the diff before applying the rules in
this section. Apply only the matching scoped sections so ordinary code PRs do
not inherit workflow-only or ruleset-only requirements.

Change type heuristic:

- **Workflow change**: diff touches `.github/workflows/**`,
  `.github/actions/**`, workflow scripts/helpers, or
  `.github/workflows/config/**`.
- **Ruleset / required-check change**: diff touches `.github/rulesets/**`,
  branch protection config, required-check/ruleset enforcement config, or
  workflows intended to become required checks.
- **Agent identity / config change**: diff touches `agents/**`, `.claude/**`,
  `AGENTS.md`, or agent runtime configuration.
- **Org-rules change**: diff touches `org-rules.md`.
- **Shared org-infra blocker**: an agent-authored PR is blocked by shared org
  infrastructure, ruleset, workflow, token scope, sync, or required-check
  behavior that is not caused by the PR's own code.
- **Ordinary code PR**: only the repo-start, branch, PR body, PR completion,
  and `main` / `master` target sections apply unless the diff also matches
  another category above.

#### At Repo Start / Before Work

**Applies when**: An agent starts work that may create commits, branches, or
PRs in a repository.

**Skip if**: The task is read-only inspection and will not create or update
branch, commit, or PR state.

- Agents must check whether repo-local hooks are enabled, for example whether
  `core.hooksPath` points at `.githooks`.
- Agents should use available repo hooks so local sync/security checks catch
  issues before PR CI.
- If hooks are not enabled, cannot be enabled, or were bypassed during the
  work, the agent must explicitly note that in the PR Summary or Test Plan.
  It must not silently skip this check.
- Repo-local hook enforcement should preferably be backed by CI-side hook
  bypass detection, starting warn-only before any hard-fail rollout. Do not
  require or modify global Git hook configuration.

#### When Creating a Work Branch

**Applies when**: An agent creates or switches to a work branch for edits.

**Skip if**: The task is read-only inspection only.

- Before creating a work branch, the agent must check whether the target
  repository has a `develop` branch.
- If `develop` exists, create feature/chore/refactor/test work branches from
  the latest `develop` and target PRs to `develop`.
- If `develop` does not exist, create the work branch from the repository
  default branch (`main` or `master`) and target PRs to that default branch.
- Agents must not work directly from protected/base branches such as `main`,
  `master`, or `develop`; create a purpose-specific work branch instead.
- Agents must not directly push commits to `main`, `master`, `develop`,
  `release/*`, or `hotfix/*`. Changes to those branches must go through the
  approved PR flow from a separate work branch.

#### When Preparing Any Agent-Authored PR

**Applies when**: An agent opens, updates, or hands off a PR.

**Skip if**: No PR is created or modified.

- Agent-authored PRs must satisfy the repository PR gate before handoff.
- PR bodies must satisfy the org PR gate enforced by
  `check-pr-template.yml`: `## Related Issue`, non-empty `## Summary`,
  non-empty `## Test Plan`, and a valid issue link keyword.
- PR metadata findings such as `PR-NATIVE-METADATA-MISSING`,
  `PR-CHANGE-SCOPE-MISSING`, `PR-IMPACT-MISSING`, `PR-ROLLBACK-MISSING`,
  `PR-RISK-MISSING`, and `PR-EXPOSURE-BLOCK-MISSING` are advisory in the
  current rollout. Agents should fix them when the facts are known, but must not
  treat them as permission to change live rulesets, required checks, branch
  protection, workflow dispatch, sync, permissions, secrets, deploys, releases,
  or downstream repositories.
- Use `Closes`, `Fixes`, or `Resolves` by default. Use `Refs` only for
  epic/cross-cutting/ADR/roadmap work that intentionally does not close the
  canonical issue.
- Agent-authored or materially Agent-edited PRs should include
  `## Agent Exposure Block` with Understood Goal, Planned Scope, Actual
  Changes, Out-of-Scope, Test Evidence, Remaining Risk, and
  Confidence-of-Agreement.
- Enforcement specifics such as `needs-template`, assignee requirements,
  `Closes #issue`, human approval, and required checks should reference the
  relevant repository ruleset source of truth, including
  `GridLtd-ProductDev/narrator-ai-web-backend#117`, instead of being
  duplicated in `org-rules.md`.
- Before handing off a PR as complete, the agent must inspect required PR
  checks. If required checks are pending or failing, the agent must either fix
  failures caused by its change or explicitly report the blocker with check
  names and links. It must not call the PR complete while required checks are
  unresolved.

#### When Targeting `main` or `master`

**Applies when**: An agent-authored PR targets `main` or `master`.

**Skip if**: The PR targets `develop` or another integration branch.

- For same-repo closing issue references on PRs targeting `main` or `master`,
  agents must make sure the linked issue is ready for closure at the high-level
  expectation required by the repository PR gate.
- Detailed per-repo enforcement specifics should remain in the normative
  repository ruleset source, including
  `GridLtd-ProductDev/narrator-ai-web-backend#117`, and should be referenced
  rather than duplicated in `org-rules.md`.

#### When Editing GitHub Actions Workflows

**Applies when**: Diff touches `.github/workflows/**`, `.github/actions/**`,
workflow scripts/helpers, or `.github/workflows/config/**`.

**Skip if**: Only application code, tests, docs, or non-workflow config are
touched.

- When adding or changing GitHub Actions workflow `uses:` references,
  third-party actions must be pinned to a full 40-character commit SHA, not a
  mutable tag like `@v4`, `@v6`, or `@main`.
- When adding or changing a workflow and its required resources, such as
  scripts, config files, templates, or helper modules, agents must determine
  the intended sync surface before the PR is considered ready.
- Agents must check whether the workflow/resource change should sync to other
  org-level `.github` repositories via `sync-github-repo` config, and whether
  it should sync to downstream repositories via `sync-org-rules` config.
- Common workflows and other common files that are synced from
  `Gridltd-DevOps/.github` must be changed at the source repository. Agents
  must not directly edit synced common files in downstream repositories or in
  target org `.github` repositories; if a downstream/org repo needs different
  behavior, use the supported local config/overlay/caller path or open the
  change against `Gridltd-DevOps/.github`.
- Agents must inspect the relevant sync config and exclusion rules, including
  `.github/workflows/config/sync-github-repo/*.json`,
  `.github/workflows/config/sync-org-rules/*.json`, `sync_paths`,
  `sync_files`, `sync_exclude_paths`, and org-specific overrides, so required
  companion files are not stranded only in the source repo.
- If adding a new synced source path or required companion path, agents must
  also check and update the relevant sync workflow trigger filters
  (`on.push.paths`) so the sync workflow actually runs when only that path
  changes.
- Synced workflows must not introduce source-only private secret or variable
  dependencies unless the workflow is guarded, excluded from the affected sync
  surface, or the PR documents why the dependency is safe for every target.
- Workflow/script/config behavior changes must include or run matching
  validation, such as relevant workflow script tests, shell tests, config
  validation, or workflow trigger/sync alignment tests.
- If the change is intentionally source-only or intentionally excluded for an
  org/downstream repositories, the PR should document that decision in the
  Summary or Test Plan.

#### When Editing Required Workflows or Rulesets

**Applies when**: Diff touches `.github/rulesets/**`, branch protection config,
required-check config, or workflows intended to become required checks.

**Skip if**: Workflow/ruleset files are not touched and the change is not part
of required-check/ruleset enforcement.

- `org-rules.md` defines only the agent runtime default: when an agent touches
  workflow/ruleset files, it must check that the change is compatible with the
  repository's required-check model and reference the authoritative policy.
- Required-workflow trigger compatibility and ruleset enforcement details live
  in
  `https://github.com/Gridltd-DevOps/.github/blob/main/docs/required-workflow-rules.md`.
  Link that policy from PRs that add, remove, or change required-workflow or
  ruleset behavior instead of duplicating the policy matrix in `org-rules.md`.

#### When an Agent PR Is Blocked by Org-Level Infrastructure

**Applies when**: An agent-authored PR is blocked by shared org infrastructure,
ruleset, workflow, token scope, sync, or required-check behavior, and the
blocker is not caused by the PR's own code.

**Skip if**: The failing check is caused by the agent's own code change and can
be fixed inside the same PR.

- Agents must open or update a canonical issue in `Gridltd-DevOps/.github`
  with the failure log, affected PR count or examples, suspected shared cause,
  and suggested patch path before waiting passively on human review.
- If the agent is assigned or has write access to the canonical infra repo, it
  should prepare the infra fix PR instead of only reporting the blocker.
- The original PR handoff must link the canonical infra issue and list
  unresolved required checks.

#### When Editing Org Rules

**Applies when**: Diff touches `org-rules.md`.

**Skip if**: Only generated synced copies are touched; update `org-rules.md`
source instead.

- Changes to `org-rules.md` must be synchronized to `AGENTS.md` and
  `.claude/rules/org.md` through the repo sync path, not edited independently
  in the synced copies.
- Drift checks for `org-rules.md`, `AGENTS.md`, and `.claude/rules/org.md`
  must pass before the PR is considered ready.
- Agent CI/CD rule PRs must keep the Action Block current: in-scope work,
  out-of-scope follow-ups, owner, next action, decision status, acceptance
  criteria, and verification must be discoverable in the issue or PR.

#### Examples / Failure Modes

- Wrong-base PRs: agents must check whether `develop` exists before branch
  creation; repos without `develop`, including `Gridltd-DevOps/.github`, fall
  back to the default branch.
- Issue-link hygiene: use `Closes`, `Fixes`, or `Resolves` for
  issue-completing PRs and `Refs` for epic/cross-cutting work; see
  `Gridltd-DevOps/.github#647`.
- Source-owned workflow changes: synced common workflow fixes must be made in
  `Gridltd-DevOps/.github`, not patched directly in downstream copies; see
  `Gridltd-DevOps/.github#661`.
- Synced secret/variable safety: common workflows must not depend on
  source-only private repo access or secrets when running downstream; see
  `Gridltd-DevOps/.github#655`.
- SHA pinning: third-party GitHub Actions must use full 40-character commit
  SHA refs, not mutable tags.

### Synced Workflow Customization

Before editing GitHub Actions workflow YAML or companion resources, classify the
workflow category and use only the matching customization mechanism. Do not
treat every synced workflow as the same kind of common workflow.

Use this fast path:

1. **Governance gates** — workflows that enforce org policy, PR/issue hygiene,
   security, branch policy, SHA pinning, AI review, canonical links, action
   blocks, or required PR metadata. These are source-owned in
   `Gridltd-DevOps/.github`. Downstream repos must not weaken or directly edit
   synced copies.
2. **Lifecycle / sync control-plane** — release, issue ops, sync, ruleset, and
   org lifecycle workflows. These are source-owned; org/repo differences must
   live in source-owned sync config or documented overrides.
3. **Notification / monitor workflows** — scanners, failure notifications, SLA
   trackers, and service monitors. Delivery routing may use documented
   non-secret config, but detection, severity, required-check failure, P0,
   security, incident, and central-monitor behavior must not be disabled by
   downstream config.
4. **Central governance / audit / drift workflows** — team membership, identity,
   ruleset, audit, synthetic monitor, and drift workflows. These have no
   downstream customization. If distributed broadly, mutating or alerting jobs
   must be guarded to the intended central repository or excluded from sync.
5. **Reusable workflow engines** — workflows with `on: workflow_call`, such as
   shared test engines. Customize through documented `workflow_call` inputs,
   secrets, and outputs. Repo-specific callers pass `with:` and `secrets:`;
   secrets must not be passed as normal inputs.
6. **Generic baseline tooling / docs** — shared label, lint, test, or docs
   workflows. Prefer repo-root `Makefile` targets as the repo-owned executable
   contract. If no supported target or project indicator exists, report clearly;
   required checks must not silently green-pass empty validation. Follow
   `docs/workflows/generic-baseline-config.md` before changing `labeler.yml`,
   `lint.yml`, `test.yml`, or `docs.yml`.
7. **Repo-specific caller workflows** — downstream workflows that call common
   reusable engines via `uses: Gridltd-DevOps/.github/.github/workflows/*`.
   The caller workflow is downstream-owned and may set triggers, `with:`,
   `secrets:`, environments, guards, and repo-specific IDs/paths permitted by
   the reusable engine contract.
8. **Deploy workflows** — `test-deploy.yml`, `release-deploy.yml`,
   `rollback.yml`, or equivalent stack/provider deployment logic. In the
   current phase these remain repo-owned. Do not commonize deploy workflows or
   sync them as universal common workflows without a separate reusable deploy
   engine RFC/design approval.
9. **Language CI workflows** — Python, Node, Go, Rust, or other stack-specific
   CI. In the current phase these are repo-owned unless an explicit reusable
   language engine exists. Generic `lint.yml` / `test.yml` remain baseline
   validation and are not language CI engines.

Config ownership must be explicit:

- `.github/gridltd/` is the downstream-owned config namespace. It may contain
  non-secret repo-owned config only when a source workflow contract documents
  the exact path, schema, parser, validation, and tests.
- Workflow-consumed config under `.github/gridltd/` is owned by the source
  workflow contract in `.github/workflow-customization.yml`, including final
  config path, key, fields, secrets, parser, and static/runtime validation.
- Generic extension inputs under `.github/gridltd/extensions/**` are owned by
  the #376 extension schema and effective-config renderer. They are not
  workflow-consumed config and must not redefine workflow final paths, keys,
  fields, secrets, or validation already owned by
  `.github/workflow-customization.yml`.
- `.github/workflows/config/` is the source-owned sync control-plane namespace
  for sync, ruleset, central governance, and source-owned exception config.
- The two namespaces must not overwrite each other. Agents must identify path
  ownership before editing workflow config.
- Secrets, webhook URLs, open IDs, app secrets, cloud credentials, kubeconfig,
  and tokens must stay in GitHub secrets or approved private systems, not in
  workflow config files.

Governance and required-check boundaries:

- Downstream config alone is not a supported governance surface. A governance
  customization is supported only after the source workflow documents it,
  parses it, validates it, and tests non-weakening behavior.
- Any policy-weakening exception must be source-owned, justified, auditable, and
  time-bounded where practical.
- Governance workflows intended to become required checks must trigger on PR
  events that rulesets can observe and must leave a stable check context for
  branch protection.
- Workflows that only run on `push`, `schedule`, `workflow_dispatch`, or
  `pull_request.closed` must not be added as PR required workflow rules.
- If a governance workflow is distributed but not required everywhere, use
  source-owned ruleset exclusions or sync exclusions rather than downstream
  workflow edits.

When changing synced workflows or companion resources, update the matching sync
surface and trigger paths as needed. Companion scripts, config files, tests,
templates, fixtures, and helper modules must follow the same intended sync
surface as the workflow or be documented as intentionally excluded. PRs that
change workflow sync behavior must state whether each touched file is synced,
source-only, guarded, or intentionally excluded, and must include matching
validation or tests.

### Issue Migration

When an Issue is moved across repos / orgs (e.g. as part of an org restructure or repo split), the **target Issue** MUST preserve traceability — otherwise the next person to touch the work has to rebuild context from scratch. Required steps:

1. **Write the full migration chain at the top of the new Issue body**, not just the immediate predecessor. Use blockquote to make it scannable:

   ```
   > Migration chain:
   > - Narrator-AI/Narrator-AI-Master-Coze#1 (origin)
   > - GridLtd-ProductDev/narrator-ai-py#263 (closed 2026-05-06)
   > - NarratorAI-Studio/cross-department-tasks#1 (this issue)
   ```

2. **Copy assignees and labels from the source Issue.** A migrated Issue with no owner is a silent backlog leak. If the assignee is no longer correct, explicitly reassign — don't leave empty.

3. **Leave a forward-pointing comment on the source Issue, not just a bare status like "Moved".** Include a clickable link to the new location, e.g.:

   ```
   📦 Migrated to {org}/{repo}#{N} — please track / comment there.
   Migration chain: A → B → C (this) → D
   ```

4. **Cross-check against the PMO tracker** ([GridLtd-PMO/sprint-board](https://github.com/GridLtd-PMO/sprint-board)) before opening the new Issue. If the same scope is already tracked there, prefer adding criteria to the existing PMO Issue and skip creating a new tracker — duplicate trackers cause conflicting source-of-truth.

5. **Link migrations bidirectionally in the body**, not only in comments — body links survive comment expand/collapse and Issue listings.

These steps are required for any new migration. Historical Issues are not retroactively required to comply, but cleaning them up is welcome via a follow-up PR.

### Product Naming Pre-Launch Review

Any new product / sub-brand / major product rename across the GridLtd enterprise MUST clear a 4-item pre-launch naming review. The review's evidence (screenshots / search exports) lives in the launch's intake Issue, filled out via the `New product launch` form (`.github/ISSUE_TEMPLATE/new-product-launch.yml`) at Issue creation time. PMO refuses to schedule any launch whose intake Issue carries `needs-naming-review`. Governed by [ADR-014](https://github.com/Gridltd-DevOps/architecture-decisions/blob/main/ADR-014.md).

The 4 checks are:

1. **Same-name / near-name competitor search** — Google + Bing/Baidu front-page screenshot evidence. **Red line**: same-industry same-function competitor in front-10 results → rename strongly recommended.
2. **Brand-word originality** — decompose into root words; flag if ≥50% of constituent words are industry-generic (e.g., `Video`, `AI`, `Smart`, `Quick`, `Pro`). Generic-word brands carry SEO-dilution and SEM-cost risk.
3. **Domain + trademark registrability** — `.com` (gTLD) and target ccTLD WHOIS + China Trademark Office search portal (`sbj.cnipa.gov.cn`) classes 9/35/42 + USPTO TESS / EUIPO eSearch. **Red line**: core TLD already held by same-industry party → rename required.
4. **China major-platform account pre-screening** — name de-duplication check on WeChat Official Account / 视频号 / 小红书 / 抖音 / B站. **Red line**: ≥2 mainstream platforms reject the name (including license-required rejections) → rename required.

PMO (`@Ashley881345`) one-click bounces any launch Issue missing the evidence and requests it before scheduling. Evidence is attached to the Issue and serves as the audit trail for any future rename / marketing decision.

Trigger case for this policy: VividDub/project-hub#23 — see ADR-014 for the trade-off analysis and rejected alternatives.

### Code Quality

- No `TODO` or `FIXME` without a linked issue
- No commented-out code in production branches
- Prefer readability over cleverness

### Security

- Never commit secrets, credentials, API keys, or `.env` files
- Use `.gitignore` to exclude sensitive and generated files
- Report security issues via private channel, not public issues

### Repository Setup Detection

When entering a new repository, detect the project environment before writing or running code.
Follow this detection order and use the first match:

| Indicator | Language | Package Manager | Install | Test | Lint |
|-----------|----------|-----------------|---------|------|------|
| `pyproject.toml` | Python | uv (prefer) / pip | `uv sync` or `pip install -e .` | `uv run pytest` or `pytest` | `uv run ruff check` |
| `package.json` | Node.js | npm / pnpm / yarn | `npm install` | `npm test` | `npm run lint` |
| `go.mod` | Go | go modules | `go mod download` | `go test ./...` | `golangci-lint run` |
| `Cargo.toml` | Rust | cargo | `cargo build` | `cargo test` | `cargo clippy` |
| `Makefile` | Any | make | `make install` | `make test` | `make lint` |

**Rules:**
- If a `Makefile` exists with `test`/`lint` targets, prefer `make` over language-specific commands
- Never assume — check the files before running commands
- For Python projects, prefer `uv` if `pyproject.toml` has `[tool.uv]` or a `.venv` managed by uv exists

### Repo-Level Override

Each repo may provide a `### Setup` section that overrides the org-level detection table:

- **Codex**: checks repo-level `AGENTS.md` for the `### Setup` section
- **Claude Code**: checks repo-level `.claude/rules/org.md` for the `### Setup` section

Only file paths the specific agent actually reads are checked — each agent should look in its own instruction file, not a copy intended for another agent.

### Agent-Specific Notes

This organization supports two AI coding agents. Each reads a different file, synced from the same source (`org-rules.md`).

| | Claude Code | Codex |
|---|-------------|-------|
| **Rule file** | `.claude/rules/org.md` | `AGENTS.md` |
| **Permission model** | `.claude/settings.local.json` (Bash/MCP/WebFetch allowlist) | TOML-based prefix-rule approval (user-level config) |
| **Override entry** | repo-level `.claude/rules/org.md` → `### Setup` | repo-level `AGENTS.md` → `### Setup` |
| **Default config dir** | `.claude/` | N/A (repo-level `AGENTS.md` only) |

**When using Codex**:
- Codex reads `AGENTS.md` only — no `.claude/` files are consumed
- Permission rules are managed via Codex's TOML / prefix-rule config, not via repo-level JSON
- The `### Setup` override in repo-level `AGENTS.md` takes precedence over the org-level detection table

**When using Claude Code**:
- Claude Code reads `.claude/rules/org.md` only — `AGENTS.md` is not consumed
- Permission rules are managed via `.claude/settings.local.json` (machine-specific)
- The `### Setup` override in repo-level `.claude/rules/org.md` takes precedence over the org-level detection table

**Cross-agent workflow**:
- `org-rules.md` is the single source of truth for both agents
- `sync-org-rules.yml` keeps `.claude/rules/org.md` and `AGENTS.md` byte-identical to `org-rules.md`
- When adding a rule that is agent-specific, prefer agent-neutral language
- When an agent requires unique configuration (e.g., permissions), use that agent's native config mechanism rather than polluting the shared rules file

**Repo-level overrides and sync**:
- `sync-org-rules.yml` overwrites `AGENTS.md` and `.claude/rules/org.md` in target repos with the org source. If a repo maintains a custom `### Setup` section in either file, it will be replaced on the next sync run.
- To add repo-specific setup instructions, use a separate file that the agent reads (e.g., `.claude/rules/custom.md` for Claude Code).
- For repo-specific Dependabot config, use `.github/dependabot.local.yml` — the sync workflow merges it with the org baseline.
