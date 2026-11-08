"""External driver: hand each think step to an outside agent instead of the built-in LLM.

With `play.driver: external` the runner keeps everything it already does (wake policy, pausing for danger, watchers,
autosave, trends, the situation packet, improvement and reflection passes) but `think()` does not call a model.
It writes the prompt to `runtime/handoff/<n>-<stream>.md`, prints one line

    HANDOFF <stream> <path> | <trigger>

on stdout, and waits for `<path>.done.json`:

    {"notes": "...", "wake_in_hours": 8, "wake_on": ["letter"], "speed": 3, "end_episode": null}

The outside agent plays the step through the bridge directly (same RPCs the tools wrap), edits brain/ for
improvement/reflection steps, then writes the done file. `speed` (optional) is kept as the play speed after the step,
like a model calling game.speed; `end_episode` (optional) ends the colony.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .paths import ROOT

DIR = ROOT / "runtime" / "handoff"


def think(ctx, user_message: str, situation_hint: str = "", trigger: str = "scheduled", system: str | None = None):
    from .loop import StepResult
    ctx.reset_turn()
    DIR.mkdir(parents=True, exist_ok=True)
    n = time.strftime("%Y%m%d-%H%M%S") + f"-{int(time.time() * 1000) % 1000:03d}"   # unique: improve/watchdog streams run concurrently
    path = DIR / f"{n}-{ctx.stream}.md"
    done = Path(str(path) + ".done.json")
    head = f"# {ctx.stream} step {n} — {trigger}\n\nEpisode {ctx.episode}, seed {ctx.seed}.\n"
    if system:
        head += "\n## Instructions for this stream\n" + system + "\n"
    path.write_text(head + "\n" + user_message + "\n\nWhen done, write " + done.name + " (see agent/rimagent/handoff.py).\n", encoding="utf-8")
    print(f"HANDOFF {ctx.stream} {path} | {trigger}", flush=True)
    ctx.emit("think_start", {"trigger": trigger, "stream": ctx.stream, "handoff": str(path)})
    t0 = time.time()
    while not done.exists():
        time.sleep(1)
    try:
        reply: dict[str, Any] = json.loads(done.read_text(encoding="utf-8") or "{}")
    except json.JSONDecodeError as e:
        reply = {"notes": f"unreadable done file: {e}"}
    ctx.wake.notes = str(reply.get("notes", ""))
    ctx.wake.in_hours = reply.get("wake_in_hours")
    ctx.wake.on_kinds = list(reply.get("wake_on") or [])
    if reply.get("speed") is not None:
        ctx.extra["model_speed"] = int(reply["speed"])
    if reply.get("end_episode"):
        ctx.end_episode_reason = str(reply["end_episode"])
    ctx.stop_turn = True
    res = StepResult(notes=ctx.wake.notes, elapsed=time.time() - t0, ended_by_tool=True)
    ctx.emit("think_end", {"trigger": trigger, "stream": ctx.stream, "notes": res.notes, "elapsed": res.elapsed})
    return res
