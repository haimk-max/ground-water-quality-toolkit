# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/haimk-max/ground-water-quality-toolkit.git
cd ground-water-quality-toolkit
```

### 2. Install in Development Mode
```bash
pip install -e .
```

This installs `signalkit` package with all dependencies (numpy, scipy, pandas).

### 3. Verify Installation
```python
python -c "from signalkit.trend_analysis import calculate_mann_kendall; print('✓ signalkit installed')"
```

---

## Using Claude Code Skills

1. Copy `skills/` folder to `~/.claude/skills/`
   ```bash
   cp -r skills/* ~/.claude/skills/
   ```

2. Restart Claude Code

3. Use skills:
   ```
   /<severity-calculator> --c_max 350 --dws 10 --parameter TCE
   /<trend-detective> --borehole nt_01 --parameter TCE --data measurements.csv
   /<forensics-analyzer> --zone holon
   ```

---

## Development Setup

If you want to develop or run tests:

```bash
pip install -e ".[dev]"
pytest
```

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'signalkit'`
Make sure you've run `pip install -e .` from the toolkit directory.

### `ImportError: No module named 'numpy'`
Install dependencies:
```bash
pip install numpy scipy pandas
```

### Skills not appearing in Claude Code
- Make sure files are in `~/.claude/skills/`
- Restart Claude Code application
- Check file permissions (should be readable)

---

## Next Steps

1. Read `docs/ZONE_REPORT_PROCESS_GUIDE.md` for methodology overview
2. Try the quick start examples in README.md
3. Explore playbooks in `docs/` folder
4. For Claude Code skills, see `skills/*/SKILL.md`

---

**Version**: 0.1.0  
**Last Updated**: 2026-05-27
