# Ground Water Quality Toolkit

ארגז כלים וכישורים לניתוח איכות מי תהום ואפיון אזורים מוקדי זיהום מים.

**Comprehensive toolkit for groundwater quality assessment, trend detection, contamination attribution, and risk classification.**

---

## שלוש שכבות (Three Tiers)

### **Tier B: Python Library (signalkit)**
ספריית Python לניתוח נתונים:
- **Mann-Kendall trend analysis** — זיהוי מגמות בסדרות זמן עם SNR gating
- **Severity bucket classification** — סיווג חומרה (0–8) ביחס לתקנים
- **Contamination forensics** — זיהוי דפוסי זיהום ויחוס למקורות
- **Data pipeline** — קבלה, נרמול, ולידציה של נתונים מדידה

```bash
pip install -e .
```

```python
from signalkit.trend_analysis import calculate_mann_kendall
from signalkit.severity_calculator import calculate_bucket
from signalkit.forensics_engine import build_decay_chains, match_source_signatures

# Trend detection
measurements = [5, 8, 12, 18, 25, 31, 35]
result = calculate_mann_kendall(measurements)
print(result)  # {'trend': 'ALERT', 'slope': 4.29, 'p_value': 0.014, ...}

# Severity index
bucket = calculate_bucket(c_max_5y=350, dws=10)
print(bucket)  # 5 (Very High)

# Forensics: VOC dechlorination chains
vocs_detected = ['TCE', 'DCE', 'VC']
chains = build_decay_chains(vocs_detected)
print(chains)  # {'PCE_chain': {'detected': ['TCE', 'DCE', 'VC'], ...}}
```

### **Tier A: Claude Code Skills**
שלוש interactive notebooks (עבור Claude Code):

1. **severity-calculator** — חישוב דרגת סיכון מריכוז ותקן
   ```
   /<severity-calculator> --c_max 3456 --dws 10 --parameter TCE --borehole nt_01
   ```

2. **trend-detective** — זיהוי מגמות בנתונים היסטוריים
   ```
   /<trend-detective> --borehole nt_01 --parameter TCE --data measurements.csv
   ```

3. **forensics-analyzer** — ייחוס זיהום למקורות (סימנים כימיים)

### **Tier C: Playbooks & Workflows**
תבניות ותרגול עבודה:

- **zone_report_v5_process.md** — זרימת הדוח המלא (7 שלבים)
- **zone_diagnosis_template.md** — שאלות אבחוניות (8 קבוצות)
- **forensics_attribution_guide.md** — ייחוס זיהום עם רמות ביטחון (A–E)
- **monitoring_gaps_checklist.md** — זיהוי פערי ניטור
- **data_pipeline_spec.md** — סכמת 6 ה-CSVs

---

## Installation

### Requirements
- Python 3.8+
- numpy, scipy, pandas

### Local Development
```bash
git clone https://github.com/haimk-max/ground-water-quality-toolkit.git
cd ground-water-quality-toolkit
pip install -e .
```

---

## Quick Start

### 1. Analyze a Trend
```python
from signalkit.trend_analysis import calculate_mann_kendall

measurements = [5.2, 6.8, 7.2, 9.5, 12.3, 15.1, 18.9, 22.5]
result = calculate_mann_kendall(measurements)

print(f"Trend: {result['trend']}")           # ALERT
print(f"P-value: {result['p_value']}")       # 0.014
```

### 2. Calculate Severity
```python
from signalkit.severity_calculator import calculate_bucket, classify_severity

bucket = calculate_bucket(c_max_5y=350, dws=10)
severity = classify_severity(bucket)

print(f"Bucket: {bucket}")                     # 5
print(f"Risk Level: {severity['risk_level']}")  # HIGH
```

### 3. Identify Contamination Patterns
```python
from signalkit.forensics_engine import build_decay_chains, match_source_signatures

detected = ['TCE', 'DCE', 'VC', 'Cr', 'Ni']
chains = build_decay_chains(['TCE', 'DCE', 'VC'])
signatures = match_source_signatures(detected)
```

---

## Methodology

### Mann-Kendall Trend Test
Non-parametric trend detection:
- Tie-corrected variance
- Continuity-corrected Z-statistic
- SNR gating (Signal-to-Noise Ratio ≥ 0.3)
- Soft trigger: 2+ consecutive rising values

**Classifications:**
- **ALERT**: p < 0.05 + slope > 0 (statistically significant rise)
- **WATCH**: Soft trigger detected
- **STABLE**: No significant trend
- **DECREASING**: p < 0.05 + slope < 0
- **NONE**: SNR < threshold (noisy data)

### Severity Index (Bucket 0–8)
Based on concentration / DWS ratio:

| Bucket | % DWS | Risk Level |
|--------|-------|------------|
| 0–1 | 0–25% | CLEAN |
| 2–3 | 25–100% | LOW |
| 4–5 | 100–500% | ELEVATED |
| 6–7 | 500–1,000% | CRITICAL |
| 8 | >1,000% | SEVERE |

### Contamination Forensics
**Evidence Classification (A–E):**
- A: Raw report verified
- B: AI-extracted with page reference
- C: Web-verified current activity
- D: Inferred candidate
- E: Weak mention

**Attribution Confidence (HIGH/MEDIUM/LOW):**
- Address verified + matching contaminant <500m + operational years overlap

---

## Documentation

See `docs/` folder:
- **ZONE_REPORT_PROCESS_GUIDE.md** — Full pipeline
- **zone_diagnosis_template.md** — Diagnostic workflow
- **forensics_attribution_guide.md** — Contamination attribution
- **monitoring_gaps_checklist.md** — Gap detection
- **DATA_PIPELINE_SPEC.md** — 6-CSV data structure
- **DATA_DICTIONARY.md** — Term definitions

---

## Contributing

Issues & PRs welcome on GitHub.

---

## License

MIT License

---

**Version**: 0.1.0 (Alpha)  
**Last Updated**: 2026-05-27
