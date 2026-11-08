"""A downed colonist nobody feeds or tends. With the steward off, vanilla only feeds
patients when a doctor's Doctor work comes up; during a fire (Firefighter 1) two
downed colonists sat at Food 0 for hours and one got malnutrition. Checks every
~30 s real time, only while someone is downed.
"""
import time

_LAST = {"t": 0.0}


def watch(ctx, events):
    if time.time() - _LAST["t"] < 30:
        return []
    _LAST["t"] = time.time()
    try:
        downed = [p for p in (ctx.bridge.call("state.pawns", filter="colonists") or []) if p.get("downed")]
    except Exception as e:
        return [{"type": "alert", "text": "downed_care: read failed: %s" % e, "wake": False}]
    out = []
    for p in downed:
        try:
            c = ctx.bridge.call("state.pawn_context", pawn=p["id"]) or {}
        except Exception:
            continue
        food = (c.get("needs") or {}).get("Food")
        if food is not None and food < 25:
            out.append({"type": "alert", "text": "DOWNED %s hungry (Food %.0f): order 優先餵食" % (p["name"], food), "wake": True})
        if c.get("needs_tending") and (c.get("ticks_to_bleed_out") or 1e9) < 6 * 2500:
            out.append({"type": "alert", "text": "DOWNED %s bleeding out in %.1fh, untended" % (p["name"], c["ticks_to_bleed_out"] / 2500), "wake": True})
    return out
