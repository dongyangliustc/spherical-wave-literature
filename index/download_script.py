#!/usr/bin/env python3
"""
球面波基组与光电离截面论文批量下载脚本
使用方法: python download_script.py
部分论文需机构订阅，会提示手动下载。
"""

import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

BASE = os.path.join(os.path.dirname(__file__), '..', 'papers')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

papers = [
    # === GTO 连续态（Cacelli-Moccia-Rizzo 系列）===
    {
        'subdir': 'GTO_continuum',
        'filename': 'Cacelli_1993_H2_GTO_continuum_JCP.pdf',
        'url': 'https://doi.org/10.1063/1.464482',
        'note': '⚠ AIP 出版社，需机构订阅。可从 sci-hub 或机构 VPN 获取。'
    },
    {
        'subdir': 'GTO_continuum',
        'filename': 'Cacelli_1998_N2_GTO_differential_PRA.pdf',
        'url': 'https://doi.org/10.1103/physreva.57.1895',
        'note': '⚠ APS 出版社，需机构订阅。'
    },
    {
        'subdir': 'GTO_continuum',
        'filename': 'Cacelli_2000_C2H2_GTO_differential_CP.pdf',
        'url': 'https://doi.org/10.1016/s0301-0104(99)00325-0',
        'note': '⚠ Elsevier 出版社，需机构订阅。'
    },
    {
        'subdir': 'GTO_continuum',
        'filename': 'Carmona_Novillo_1996_LiH_GTO_STOCOS_CP.pdf',
        'url': 'https://doi.org/10.1016/0301-0104(96)00128-0',
        'note': '⚠ Elsevier 出版社，需机构订阅。'
    },
    {
        'subdir': 'GTO_continuum',
        'filename': 'Moccia_Montuoro_2003_Li2_STO_BSpline_CPL.pdf',
        'url': 'https://doi.org/10.1016/s0009-2614(02)01765-7',
        'note': '⚠ Elsevier 出版社，需机构订阅。'
    },
    # === B-spline 连续态 ===
    {
        'subdir': 'B_spline_continuum',
        'filename': 'Decleva_2022_Tiresia_Molecules.pdf',
        'url': 'https://www.mdpi.com/1420-3049/27/6/2026/pdf',
        'note': '➜ MDPI 开放获取（OA），URL 或有反爬。可在浏览器中打开后手动保存。'
    },
    {
        'subdir': 'B_spline_continuum',
        'filename': 'Tenorio_2022_Dyson_BSpline_Molecules.pdf',
        'url': 'https://www.mdpi.com/1420-3049/27/4/1203/pdf',
        'note': '➜ MDPI 开放获取（OA）'
    },
    {
        'subdir': 'B_spline_continuum',
        'filename': 'Stener_2005_TDDFT_BSpline_JCP.pdf',
        'url': 'https://doi.org/10.1063/1.1937367',
        'note': '⚠ AIP 出版社，需机构订阅。'
    },
    {
        'subdir': 'B_spline_continuum',
        'filename': 'Brosolo_Decleva_1992_H2plus_BSpline_CP.pdf',
        'url': 'https://doi.org/10.1016/0301-0104(92)80069-8',
        'note': '⚠ Elsevier 出版社。'
    },
    # === 球面波 / Lobatto ===
    {
        'subdir': 'spherical_wave',
        'filename': 'Wilhelmy_1994_Lobatto_photoionization_JCP.pdf',
        'url': 'https://doi.org/10.1063/1.466475',
        'note': '⚠ AIP 出版社，需机构订阅。'
    },
    # === 复缩放 ===
    {
        'subdir': 'complex_scaling',
        'filename': 'McCurdy_Martin_2004_ECS_BSpline_JPB.pdf',
        'url': 'https://doi.org/10.1088/0953-4075/37/4/017',
        'note': '➜ IOP Science，开放获取（OA）。部分镜像可访问。'
    },
    # === 综述 ===
    {
        'subdir': 'general_review',
        'filename': 'Nisoli_2017_attosecond_chem_rev.pdf',
        'url': 'https://doi.org/10.1021/acs.chemrev.6b00453',
        'note': '➜ ACS 出版社，但 DESY 仓库镜像可获取。'
    },
]


def download_paper(p):
    subdir = os.path.join(BASE, p['subdir'])
    os.makedirs(subdir, exist_ok=True)
    path = os.path.join(subdir, p['filename'])
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print(f'[SKIP] {p["filename"]} — 已存在')
        return

    print(f'[TRY]  {p["filename"]}')
    try:
        req = urllib.request.Request(p['url'], headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            if len(data) > 10000 and not data.startswith(b'<'):
                with open(path, 'wb') as f:
                    f.write(data)
                print(f'[OK]   {p["filename"]} ({len(data)//1024} KB)')
            else:
                print(f'[FAIL] {p["filename"]}: 返回内容非 PDF ({len(data)} bytes)')
                print(f'       {p["note"]}')
    except Exception as e:
        print(f'[FAIL] {p["filename"]}: {e.__class__.__name__}')
        print(f'       {p["note"]}')


if __name__ == '__main__':
    print('=' * 60)
    print('球面波基组与光电离截面文献自动下载')
    print('=' * 60)
    print()
    for p in papers:
        download_paper(p)
    print()
    print('=' * 60)
    print('需要手动下载的论文请通过机构 VPN 或 sci-hub 获取。')
    print('所有论文的 DOI 均已在索引文件中列出。')
    print('=' * 60)
