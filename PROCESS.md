# PROCESS.md — ground-water-quality-toolkit

SSOT לדרישות פתוחות וסגורות. עדכן **לפני** תחילת עבודה על דרישה חדשה, והעבר ל-Closed עם commit hash ושיטת אימות בסיום.

> **מקור הזריעה (2026-10-12)**: שני "הפערים הידועים" שב-`CLAUDE.md`, שם הוגדרו כמשימות לפתיחה. תיוג מוצא: מודל, באישור המשתמש.

## דרישות פתוחות (Open)

| # | בעיה | תיאור | סטטוס | ממתין ל | תאריך | קבצים |
|---|------|-------|-------|---------|-------|-------|
| 1 | הסקילים אינם נטענים | הסקילים ב-skills/ ללא YAML frontmatter ומחוץ ל-.claude/skills/; נדרש frontmatter (name/description) ועותק או פריסה ב-.claude/skills/ | פתוח | אני | 2026-08-25 | skills/ |
| 2 | סקיל facility-discovery | אוטומציית 6 ערוצי איתור-המפעלים (מתוכנן במדריך כ-"Phase 2"); בסיס CKAN קיים בסקיל israel-gov-api | עתידי | אני | 2026-08-25 | docs/ZONE_REPORT_PROCESS_GUIDE.md |
| 3 | בית קנוני לפרמטרים ולקבוצות | העלאת טבלת הפרמטרים, הסיווג לקבוצות, ערכי התקן וההמרה בין משרד הבריאות לרשות המים ל-parameters/, ואחר כך הנחיות סנכרון בפרויקטים הצרכנים | קבצים הועלו וסודרו; README והפניות בתיעוד עודכנו; הנחיות סנכרון מוזגו ב-IAR, ‏pfas-forensics, ‏effluent-marks, ‏water-knowledge-system, ‏LIMS ו-sessions-archive | הכרעות בעלי מילון הקודים (פערים ב-PACKAGE_GUIDE) | 2026-11-09 | parameters/ |
| 4 | signalkit אינו שואב מ-parameters/ | `classify_contamination_family` ומילוני המשפחות ב-`forensics_engine.py` מסווגים לפי מילות מפתח ורשימות מקומיות; נדרש לחבר אותם לטבלה הקנונית (שינוי API ובדיקות) | פתוח | הכרעת המשתמש על היקף | 2026-11-09 | pylib/signalkit/forensics_engine.py |

## דרישות סגורות (Closed) — Audit Trail

| # | בעיה | תאריך סגירה | commit | אימות |
|---|------|-------------|--------|-------|
