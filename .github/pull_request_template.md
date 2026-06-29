## Related Issue

<!-- Required: Link the issue this PR addresses. CI will fail if no issue is linked. -->

Closes https://github.com/owner/repo/issues/123

<!-- Replace https://github.com/owner/repo/issues/123 with the actual governing issue, for example:
     Closes https://github.com/GridLtd-ProductDev/.github/issues/170 -->

## Native Metadata

<!-- Advisory: reviewers and Agents should check GitHub native fields first. Record exceptions only. -->

- Base / head branch reviewed: yes | exception: <reason>
- Labels reviewed: yes | exception: <reason>
- Assignees / reviewers reviewed: yes | exception: <reason>
- Linked issue intent reviewed: closes | refs | companion | exception: <reason>
- Checks / review state reviewed: yes | pending: <reason>

## Summary

<!-- Brief description of changes (1-3 bullet points) -->

- <briefly describe the change and why>

## Change Scope

- Type: docs | chore | bug | feature | workflow | ruleset | release | security
- Scope boundary:
- Out-of-scope:

## Impact

- User / repo impact:
- CI/CD impact:
- Open issue / PR impact:
- Agent collaboration impact:


## AC Verification

<!-- Required: Copy each Acceptance Criteria item from the linked Issue.
     Mark as [x] and note where it was implemented/tested.
     Existing repository-specific AC gates may inspect this section, but this
     template redesign does not promote any new hard-fail behavior without the
     separate #1819/#1829 approval path. -->

- [x] AC item 1 — implemented in src/xxx, tested in tests/test_xxx
- [x] AC item 2 — implemented in src/yyy

## Test Plan

<!-- How was this tested? Do not paste secrets, tokens, customer data, or sensitive logs. -->

- [ ] Unit tests pass
- [ ] Lint passes
- [ ] If `org-rules.md` changed, ran `make sync-rules` and committed the result (required for `AGENTS.md Drift Check` to pass — only applicable to PRs against `Gridltd-DevOps/.github`)

## Rollback

- Rollback command / PR / revert path:
- Post-check:

## Risk

- Risk level: low | medium | high | approval-gated
- Risk reason:
- Approval issue required: yes | no | link:

## Agent Exposure Block

<!-- Required when an Agent authored, materially edited, or executed the PR. -->

**Understood Goal**: <goal as interpreted by the Agent>
**Planned Scope**: <planned files/actions>
**Actual Changes**: <actual files/actions>
**Out-of-Scope**: <explicit boundaries>
**Test Evidence**: <commands/checks/manual review>
**Remaining Risk**: <known uncertainty>
**Confidence-of-Agreement**: <checked-with-owner | best-guess-needs-check | owner-blessed-plan>

## Notification Checklist

<!-- If this PR adds or modifies a service with user-facing async operations or
     multi-step pipelines, verify notifications are correctly wired.
     Otherwise, delete this section. -->

- [ ] Phase/step boundaries emit appropriate progress notifications
- [ ] External service waits have stuck-alert / timeout coverage
- [ ] New states are registered in the notification routing layer
- [ ] Polling loops report progress to prevent false stalled-job alerts
