# Download Manifest: 多中心连续态 × 交换K/Feshbach 候选追加

- 生成：2026-08-29
- 来源批次：`outputs/literature_search_multicenter_feshbach_2026-08-29.md`（6 组 OpenAlex 检索命中）
- 注册表：`index/registry/candidates.yaml`（10 条已追加，state: discovered）
- 获取通道：USTC WebVPN / 机构订阅（AIP / APS / IOP / ACS / Annual Reviews）

## 待下载队列（按优先级）

| 优先级 | id | 标题（缩写） | DOI | 出版社 | 下载点 |
|---|---|---|---|---|---|
| P0 | lit-gharibnejad-2021-multicenter-quadrature | Multi-center quadrature scheme for the molecular continuum | 10.1016/j.cpc.2021.107889 | Elsevier (CPC) | ScienceDirect via WebVPN |
| P0 | lit-gil-1990-feshbach-fano-mulliken | Feshbach-Fano methods for Mulliken orbital analysis ... | 10.1088/0031-8949/1990/t31/025 | IOP (Phys. Scr.) | IOPscience via WebVPN |
| P0 | lit-jagau-2017-electronic-resonances | Extending QChem of Bound States to Electronic Resonances | 10.1146/annurev-physchem-052516-050622 | Annual Reviews | annualreviews.org via WebVPN |
| P1 | lit-borras-2021-xchem-mfpad-feshbach | MFPAD of CO near Feshbach Resonances: XCHEM | 10.1021/acs.jctc.1c00480 | ACS | ACS Publications via WebVPN |
| P1 | lit-marante-2014-hybrid-gaussian-bspline | Hybrid Gaussian-B-spline basis for the electronic continuum | 10.1103/physreva.90.012506 | APS | APS journals via WebVPN |
| P1 | lit-zatsarinny-bartschat-2013-bspline-rmatrix | The B-spline R-matrix method for atomic processes | 10.1088/0953-4075/46/11/112001 | IOP (JPB) | IOPscience via WebVPN |
| P2 | lit-borras-2023-xchem2 | Photoionization cross sections and PAD with XCHEM-2.0 | 10.1016/j.cpc.2023.109033 | Elsevier (CPC) | ScienceDirect via WebVPN |
| P2 | lit-ota-2020-full-potential-mfpad | Full-potential method for core-level MFPAD | 10.1088/1361-6455/abd06d | IOP (JPB) | IOPscience via WebVPN |
| P2 | lit-decleva-2022-tiresia-review | Continuum Electronic States: The Tiresia Code | 10.3390/molecules27062026 | MDPI | MDPI (开放获取) |
| P2 | lit-hazi-1978-l2-resonance-widths | A purely L2 method for calculating resonance widths | 10.1088/0022-3700/11/8/001 | IOP (JPB) | IOPscience via WebVPN |

## 下载后验收标准

1. PDF 落盘至对应目录（见 registry paths.pdf 约定）：
   - 多中心/XCHEM/混合基 → `papers/spherical_wave/`
   - Feshbach/交换/L2/谐振 → `papers/Schwinger_L2/` 或 `papers/R_matrix/`
   - 综述类 → `papers/general_review/`
2. 下载后用 pypdf 提取首页核对标题/作者/DOI（防错误 PDF 指向），状态 → `fulltext_available` + `machine_screened`。
3. `publisher_verification.tsv` 同步登记（downloaded / verified）。

## 备注

- MDPI 条目（Tiresia review）开放获取可直接下载，优先级最高但标记 P2 因为属于综述、不阻塞实现。
- 3 条 P0 + 2 条 P1（Borràs/Marante）为本次定向检索的核心抓手，建议先行。

---

## 下载执行记录（2026-08-29 18:xx GMT+8）

**6/6 全部下载成功并通过 pypdf 首页验证**（无错误 PDF 指向）：

| id | PDF 落盘 | 页数 | 来源通道 |
|---|---|---|---|
| lit-gharibnejad-2021-multicenter-quadrature | papers/spherical_wave/Gharibnejad_2021_multicenter_quadrature_CPC.pdf | 24 | Unpaywall OA (Semantic Scholar 镜像) |
| lit-gil-1990-feshbach-fano-mulliken | papers/Schwinger_L2/Gil_1990_FeshbachFano_Mulliken_PhysScr.pdf | 10 | Sci-Hub browser (Phys. Scr. T31:179-188) |
| lit-jagau-2017-electronic-resonances | papers/general_review/Jagau_2017_electronic_resonances_ARPC.pdf | 31 | Sci-Hub browser |
| lit-borras-2021-xchem-mfpad-feshbach | papers/spherical_wave/Borras_2021_MFPAD_Feshbach_XCHEM_JCTC.pdf | 10 | Sci-Hub browser (JCTC 17:6330-6339) |
| lit-marante-2014-hybrid-gaussian-bspline | papers/GTO_continuum/Marante_2014_hybrid_GTO_BSpline_PRA.pdf | 20 | Sci-Hub browser (PRA 90:012506) |
| lit-zatsarinny-bartschat-2013-bspline-rmatrix | papers/B_spline_continuum/Zatsarinny_Bartschat_2013_Bspline_Rmatrix_JPB.pdf | 40 | Sci-Hub browser (IOP full text) |

- 注册表 6 条状态：`discovered` → `fulltext_available` / `machine_screened`，pdf 路径已回填，YAML 校验通过。
- 顺带修复既有引用错误：lit-toffoli-coriani-stener-decleva-2024-tiresia-code 的 pdf 路径 `B_spline_continuum/` → `GTO_continuum/`（实际文件位置）。
- 剩余 P2 4 条（borras-2023-xchem2 / ota-2020 / decleva-2022-tiresia-review / hazi-1978）仍为 discovered，待后续批次。

---

## 下载执行记录（2026-08-29 18:xx GMT+8）

**6/6 全部下载成功并通过 pypdf 首页验证**（无错误 PDF 指向）：

| id | PDF 落盘 | 页数 | 来源通道 |
|---|---|---|---|
| lit-gharibnejad-2021-multicenter-quadrature | papers/spherical_wave/Gharibnejad_2021_multicenter_quadrature_CPC.pdf | 24 | Unpaywall OA (Semantic Scholar 镜像) |
| lit-gil-1990-feshbach-fano-mulliken | papers/Schwinger_L2/Gil_1990_FeshbachFano_Mulliken_PhysScr.pdf | 10 | Sci-Hub browser (Phys. Scr. T31:179-188) |
| lit-jagau-2017-electronic-resonances | papers/general_review/Jagau_2017_electronic_resonances_ARPC.pdf | 31 | Sci-Hub browser |
| lit-borras-2021-xchem-mfpad-feshbach | papers/spherical_wave/Borras_2021_MFPAD_Feshbach_XCHEM_JCTC.pdf | 10 | Sci-Hub browser (JCTC 17:6330-6339) |
| lit-marante-2014-hybrid-gaussian-bspline | papers/GTO_continuum/Marante_2014_hybrid_GTO_BSpline_PRA.pdf | 20 | Sci-Hub browser (PRA 90:012506) |
| lit-zatsarinny-bartschat-2013-bspline-rmatrix | papers/B_spline_continuum/Zatsarinny_Bartschat_2013_Bspline_Rmatrix_JPB.pdf | 40 | Sci-Hub browser (IOP full text) |

- 注册表 6 条状态：`discovered` → `fulltext_available` / `machine_screened`，pdf 路径已回填，YAML 校验通过。
- 顺带修复既有引用错误：lit-toffoli-coriani-stener-decleva-2024-tiresia-code 的 pdf 路径 `B_spline_continuum/` → `GTO_continuum/`（实际文件位置）。
- 剩余 P2 4 条（borras-2023-xchem2 / ota-2020 / decleva-2022-tiresia-review / hazi-1978）仍为 discovered，待后续批次。

---

## P2 批次处理记录（2026-08-29 19:xx GMT+8，含前置查重）

**前置查重**：对 P2 4 条对全库 53 个 PDF 做内容级比对（DOI/标题/作者三个指纹）。
- 🔴 **lit-decleva-2022-tiresia-review** → **真重复**：库中已有 `papers/B_spline_continuum/Decleva_2022_Tiresia_continuum_Molecules.pdf`（同 DOI 10.3390/molecules27062026、同标题、同作者、同期刊），**未重新下载**，直接标 fulltext。
- Ota 2020 初筛 10 个命中均为误报（首屏泛词 "molecular-frame"），无真重复。

**P2 下载结果**：
| id | 结果 | 通道 |
|---|---|---|
| lit-borras-2023-xchem2 | ✅ 落盘 papers/spherical_wave/Borras_2023_XCHEM2_CPC.pdf (12页, 2.3MB) | **UAM 机构仓库 OA**（repositorio.uam.es, CC BY-NC-ND）——SCI-Hub 失败后转 OA 仓库直链成功 |
| lit-decleva-2022-tiresia-review | ✅ 已有库文件（查重确认同篇），未重复下载 | — |
| lit-ota-2020-full-potential-mfpad | ⛔ download_blocked | IOP bronze OA 被 Radware Bot Manager 拦截；Sci-Hub 域名全失败；HAL 存目无文件 |
| lit-hazi-1978-l2-resonance-widths | ⛔ download_blocked | 同上（IOP 1978 老文献） |

**Ota/Hazi 人工下载指引（WebVPN）**：
1. 浏览器登录 https://wvpn.ustc.edu.cn（USTC CAS）
2. 访问：
   - Ota 2020: https://iopscience.iop.org/article/10.1088/1361-6455/abd06d/pdf
   - Hazi 1978: https://iopscience.iop.org/article/10.1088/0022-3700/11/8/001/pdf
3. PDF 落地后放 `papers/spherical_wave/`（Ota）与 `papers/Schwinger_L2/`（Hazi），随后我更新注册表状态。

**总计**：本批次查重拦截 1 条重复（省 1 次下载），成功下载 1 条（XCHEM-2.0），2 条转人工。
**当前注册表终态**：30 条 = 28 fulltext_available + 2 download_blocked。
