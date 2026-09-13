# -*- coding: utf-8 -*-
"""笔记层引用标签清洗：把错下载时代留下的错误署名/年份对齐到核实后的元数据。
仅处理 notes/*.md；outputs/ 审计报告作为历史记录不改。
"""
import os, re, io

ROOT = r"D:\WORK\workbuddy\spherical_wave_literature"
NOTES = os.path.join(ROOT, "notes")

# (旧, 新, 说明)  —— 顺序敏感：长串在前，避免子串误伤
RULES = [
    ("Fruhnert_2024_Tmatrix_data_format_arXiv.pdf", "Asadova_2025_Tmatrix_data_format_JQSRT.pdf", "Fruhnert→Asadova 文件名"),
    ("Fruhnert_2024_Tmatrix_data_format_arXiv", "Asadova_2025_Tmatrix_data_format_JQSRT", "Fruhnert→Asadova 文件名(无后缀)"),
    ("Fruhnert et al. — 2024", "Asadova et al. — 2025", "Fruhnert→Asadova 节标题"),
    ("Fruhnert et al.—2024", "Asadova et al.—2025", "Fruhnert→Asadova 节标题(无空格)"),
    ("Fruhnert 2024", "Asadova 2025", "Fruhnert→Asadova 引用标签"),
    ("Fruhnert", "Asadova", "Fruhnert→Asadova 兜底"),

    ("Weinberg_1994_spinor_spherical_wave_JMP.pdf", "Hughes_1994_spherical_wave_expansion_any_spin_JMP.pdf", "Weinberg→Hughes 文件名"),
    ("Weinberg — 1994", "Hughes — 1994", "Weinberg→Hughes 节标题"),
    ("Weinberg 1994", "Hughes 1994", "Weinberg→Hughes 引用标签"),
    ("温伯格（Steven Weinberg）", "J. Hughes", "幻觉署名更正"),

    ("RuizSerrano_2012_linear_scaling_HF_ONETEP.pdf", "Dziedzic_Hill_Skylaris_2013_linear_scaling_HF_Wannier_JCP.pdf", "RuizSerrano→Dziedzic 文件名"),
    ("Ruiz-Serrano et al. — 2012", "Dziedzic, Hill, Skylaris — 2013", "RuizSerrano→Dziedzic 节标题"),
    ("Ruiz-Serrano 2012", "Dziedzic 2013", "RuizSerrano→Dziedzic 引用标签"),
    ("Ruiz-Serrano", "Dziedzic", "RuizSerrano→Dziedzic 兜底"),

    ("Egel_2024_MLFMA_metasurfaces_arXiv.pdf", "Corsaro_2026_MLFMA_metasurfaces_IEEE_TAP.pdf", "Egel→Corsaro 文件名"),
    ("Egel et al. — 2024", "Corsaro et al. — 2026", "Egel→Corsaro 节标题"),
    ("Egel 2024", "Corsaro 2026", "Egel→Corsaro 引用标签"),

    ("Qian_2002_NAO_Hubbard_arXiv.pdf", "Djajaputra_Cooper_2003_tight_binding_LMTO_NiAl_pssb.pdf", "Qian→Djajaputra 文件名"),
    ("Qian et al. — 2002", "Djajaputra & Cooper — 2003", "Qian→Djajaputra 节标题"),
    ("Qian 2002", "Djajaputra & Cooper 2003", "Qian→Djajaputra 引用标签"),
    ("Qian", "Djajaputra", "Qian→Djajaputra 兜底"),

    ("Toffoli 2023", "Toffoli 2024", "年份更正"),
    ("Gonis 1999", "Gonis 2000", "年份更正"),
]

# 白名单：这些行内命中不得替换（真实存在的文献 / 历史叙述）
WHITELIST_PATTERNS = [
    r"semanticscholar\.org",          # Egel & Eremin 真实 T-matrix 论文链接
]

total = {}
report = []
for fn in sorted(os.listdir(NOTES)):
    if not fn.endswith(".md"):
        continue
    path = os.path.join(NOTES, fn)
    orig = io.open(path, encoding="utf-8").read()
    lines = orig.split("\n")
    counts = {}
    for i, line in enumerate(lines):
        if any(re.search(p, line) for p in WHITELIST_PATTERNS):
            continue
        for old, new, desc in RULES:
            if old in line:
                n = line.count(old)
                line = line.replace(old, new)
                counts[desc] = counts.get(desc, 0) + n
        lines[i] = line
    new_text = "\n".join(lines)
    if counts:
        io.open(path, "w", encoding="utf-8", newline="").write(new_text)
        report.append((fn, counts))
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v

print("=== 替换汇总 ===")
for k, v in sorted(total.items(), key=lambda x: -x[1]):
    print(f"  {k:32s} {v} 处")
print(f"  合计 {sum(total.values())} 处\n")
print("=== 分文件 ===")
for fn, counts in report:
    print(f"  {fn}")
    for k, v in counts.items():
        print(f"      {k}: {v}")
print(f"\n改动文件数: {len(report)}")
