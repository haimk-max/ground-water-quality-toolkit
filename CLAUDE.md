# CLAUDE.md — ground-water-quality-toolkit

ארגז-כלים **להפצה** לניתוח איכות מי-תהום: ספריית `signalkit` (‏Mann-Kendall עם SNR gating, ‏severity buckets, ‏forensics/decay chains, ‏data pipeline), סקילים ומדריכי תהליך.

## אילוצי סביבה וקונבנציות
- עבודה דרך Claude Code on the web; `~/.claude/` אינו שורד — כל שינוי בר-קיימא committed.
- קוד, שמות ו-docstrings: **אנגלית**; מסמכי הסבר: **עברית**; commits: **אנגלית**.
- זהו מוצר-הפצה: שינוי התנהגות ציבורית (API, ספים, סכמות) מחייב עדכון בדיקות ו-`README.md`/`INSTALLATION.md` באותו סבב.
- מקור-האמת ההיסטורי של המתודולוגיה ויחסו לריפו זה — באינדקס הדומייני: `sessions-archive/toolkit/domain/README.md`.

## מפת הריפו
- `pylib/signalkit/` — ספריית הניתוח (עם בדיקות — הרץ אותן לפני push של שינוי קוד).
- `skills/` — סקילים בפורמט תיעודי (`agent-rag`, `severity-calculator`, `trend-detective`).
- `docs/ZONE_REPORT_PROCESS_GUIDE.md` — מתודולוגיית דוח אזורי, כולל 6 ערוצי איתור-מפעלים ממקורות ממשלתיים.

## פערים ידועים (לא לתקן כבדרך-אגב; לפתוח כמשימה)
1. הסקילים ב-`skills/` הם **ללא YAML frontmatter** ומחוץ ל-`.claude/skills/` — ולכן **אינם נטענים** כסקילים בסשן. הפיכתם לנטענים = הוספת frontmatter (‏name/description) + עותק/פריסה ב-`.claude/skills/`.
2. סקיל `facility-discovery` (אוטומציית 6 הערוצים) מתוכנן במדריך ("Phase 2") וטרם מומש; בסיס CKAN מוכן בסקיל `israel-gov-api` (ראו האינדקס הדומייני).
