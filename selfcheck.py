"""Self-check for STAT163 practice notebooks.

Shows what your answer holds and confirms it is the right kind of thing. It does
NOT compare your answer with ours, so a ✅ never means the number is right.
You do not need to edit this file.
"""
import numpy as np
import pandas as pd


def _filled(v):
    return not (v is ... or (isinstance(v, str) and v.strip() in ("", "?", "...")))


def _show(v):
    """One short line saying what is saved."""
    if isinstance(v, pd.DataFrame):
        return f"a DataFrame of {v.shape[0]:,} rows and {v.shape[1]} columns"
    if isinstance(v, pd.Series):
        return f"a Series of {len(v):,} values, dtype {v.dtype}"
    if isinstance(v, str):
        s = v.strip()
        return f'"{s[:60]}…"' if len(s) > 60 else f'"{s}"'
    if isinstance(v, (int, np.integer)) and not isinstance(v, (bool, np.bool_)):
        return f"{int(v):,}"
    return f"{v}"


_KINDS = {
    "integer":   (lambda v: isinstance(v, (int, np.integer)) and not isinstance(v, (bool, np.bool_)), "a whole number"),
    "number":    (lambda v: isinstance(v, (int, float, np.integer, np.floating)) and not isinstance(v, (bool, np.bool_)), "a number"),
    "text":      (lambda v: isinstance(v, str), "text"),
    "Series":    (lambda v: isinstance(v, pd.Series), "a Series"),
    "DataFrame": (lambda v: isinstance(v, pd.DataFrame), "a DataFrame"),
}


def check(name, value, kind):
    if not _filled(value):
        print(f"⏳ {name}: not filled in yet"); return
    ok, label = _KINDS[kind]
    if ok(value):
        print(f"✅ {name} = {_show(value)}")
    else:
        print(f"⚠️ {name}: expected {label}, got {_show(value)}")


def check_col(df, col):
    if not isinstance(df, pd.DataFrame) or col not in df.columns:
        print(f'⏳ column "{col}" not created yet'); return
    try:
        if df[col].map(lambda v: v is ...).all():
            print(f'⏳ column "{col}" not filled in yet'); return
    except Exception:
        pass
    first = df[col].iloc[0]
    if callable(first):
        print(f'⚠️ ["{col}"]: the column holds a method, not its result. '
              "Add the missing () after the method name and run the cell again."); return
    print(f'✅ ["{col}"] created — {len(df):,} values, dtype {df[col].dtype}, '
          f"first one is {first}")


def check_choice(name, value, allowed):
    if not _filled(value):
        print(f"⏳ {name}: not filled in yet"); return
    if str(value).strip().upper() in allowed:
        print(f"✅ {name} = {_show(value)}")
    else:
        print(f"⚠️ {name}: expected one of {sorted(allowed)}, got {_show(value)}")


_PLACEHOLDER_NAMES = {"", "...", "name surname", "your name"}


def _norm_name(s):
    return s.strip().lower().replace("ʼ", "'").replace("`", "'").replace("’", "'")


def check_identity(name):
    """Confirms the name is filled in and differs from the placeholder (not graded)."""
    if not isinstance(name, str) or _norm_name(name) in _PLACEHOLDER_NAMES:
        print("⏳ student_name: replace the placeholder with your real name"); return
    print(f'✅ student_name = "{name.strip()}"')
