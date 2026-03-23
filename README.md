# OpenCode Test Repo

Testing the side-by-side workflow between OpenCode (GitHub Actions) and Rog (OpenClaw local agent).

## The Setup

**OpenCode** runs in GitHub Actions:
- Trigger: Comment \oc or \opencode on issues/PRs
- Auto-reviews PRs when opened
- Can fix issues and open PRs

**Rog** (OpenClaw) runs locally:
- Prototypes code, explains architecture
- Handles git operations, commits, branches
- Works from Telegram/chat

## Workflow

1. **Brainstorm with Rog** locally
2. **Rog pushes code** to GitHub
3. **OpenCode reviews** the PR via /oc or automatically
4. **Discuss findings** with Rog
5. Iterate

## Test It

- Open an issue and comment: /opencode explain this
- Create a PR and OpenCode will auto-review
- Comment on PR lines: /oc add error handling here

## Setup Required

To activate OpenCode, add your ANTHROPIC_API_KEY to the repo secrets.