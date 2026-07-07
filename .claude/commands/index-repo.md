Index this repository into the `codebase-memory-mcp` knowledge graph so future code-exploration
questions (find a function, trace a call chain, get exact source for a symbol, map the
architecture) can use `search_graph` / `trace_path` / `get_code_snippet` / `get_architecture`
instead of ad-hoc grep, per the Code Discovery Protocol.

Arguments (`$ARGUMENTS`, all optional, space-separated, any order):
- a repo path — defaults to the current working directory (repo root)
- a mode — one of `full` (default; all files + similarity/semantic edges), `moderate`
  (filtered files + similarity/semantic), `fast` (filtered files, no similarity/semantic)

## Steps

1. **Resolve inputs.** Parse `$ARGUMENTS` for an optional path and an optional mode keyword
   (`full`/`moderate`/`fast`). Default path = repo root (current working directory), default
   mode = `full`. This repo is mostly Markdown research notes with a handful of Python numerics
   scripts (`victor/prime-zeros.py`, `victor/adele/*.py`, `victor/research/numerics/*.py`,
   `sympy/mcp_server.py`) — `full` is cheap here and gives the richest graph, so don't downgrade
   to `fast`/`moderate` unless the user asked for it or the repo is large.

2. **Check current state** with `list_projects`. If a project already covers this path, call
   `index_status` on it and report what's there (file/node/edge counts, last indexed time) before
   re-indexing.

3. **Index** by calling `index_repository` with the resolved `repo_path` and `mode`. Leave
   `persistence` off unless the user asked to write a shareable `.codebase-memory/graph.db.zst`
   artifact.

4. **Verify** by calling `index_status` again (or `get_architecture` with a light aspect) to
   confirm the run completed and pull summary counts.

5. **Report** a short summary: project name, mode used, files/nodes/edges indexed, elapsed time,
   and one example `search_graph` or `get_architecture` call the user can try next. Do not dump
   the full graph or file list.
