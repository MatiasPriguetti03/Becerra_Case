# AGENTS

## Project shape (verified)
- This repository is a Ren'Py game project root (`game/` style contents live at repo root).
- Main story entrypoint is `label start` in `script.rpy`.
- Core engine/template files are `script.rpy`, `screens.rpy`, `gui.rpy`, and `options.rpy`.
- There are no repo-local build/test/lint/task configs (no `README*`, CI workflows, package manifests, or task runner files were found).

## High-risk files to avoid editing by default
- Do not edit compiled/generated files: `*.rpyc`, `cache/*.rpyb`, `cache/shaders.txt`, `tl/None/common.rpymc`.
- Do not edit runtime state files unless explicitly requested: everything under `saves/` (including `persistent`).
- Prefer editing source `.rpy` files and raw assets only.

## Asset and script conventions used here
- Script uses short Ren'Py names directly (examples: `play music sleep`, `play sound hard_knock`, `show cam`, `scene bg bedroom`).
- Asset filenames and directories include spaces and mixed case (for example under `images/` and `audio/`), so match names exactly when referencing or renaming files.
- `libs/libs.txt` is present; anything in `libs/` is loaded before normal `game` scripts by Ren'Py.

## Practical workflow for agents
- Before changing story/UI, read the relevant block in `script.rpy` or `screens.rpy` and keep indentation/style exactly (Ren'Py syntax is indentation-sensitive).
- Keep UI text and existing comments consistent with current language usage (Spanish in template files, Spanish narrative in `script.rpy`).
- After edits, at minimum run `git status --short` to confirm only intended source/assets changed and no generated/save files were touched.
