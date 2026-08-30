# -*- coding: utf-8 -*-
"""
Fetch citation network (referenced works + citing works) for library review papers.
Tier-1 source: OpenAlex (free, no key). Output: JSON per review + a combined summary.
"""
import json, time, urllib.request, urllib.parse, os, sys

MAILTO = 'dynamic.huang.research@gmail.com'
BASE = 'https://api.openalex.org/'

# ---- library review inventory (with DOI) ----
REVIEWS = [
    {
        "key": "lucchese1986_schwinger_review",
        "title": "Schwinger variational principle review (electron-molecule & photoionization)",
        "doi": "10.1016/0370-1573(86)90147-X",
        "pdf": "papers/Schwinger_L2/Lucchese_Takatsuka_McKoy_1986_Schwinger_review_PhysRep.pdf",
        "topic": "Schwinger变分/L2方法 — 方法开发与原理",
    },
    {
        "key": "zatsarinny2013_bspline_rmatrix_review",
        "title": "B-spline R-matrix method for atomic processes (topical review)",
        "doi": "10.1088/0953-4075/46/11/112001",
        "pdf": "papers/B_spline_continuum/Zatsarinny_Bartschat_2013_Bspline_Rmatrix_JPB.pdf",
        "topic": "B-spline R-matrix — 方法开发与原理",
    },
    {
        "key": "jagau2017_electronic_resonances_review",
        "title": "Extending Quantum Chemistry of Bound States to Electronic Resonances",
        "doi": "10.1146/annurev-physchem-052516-050622",
        "pdf": "papers/general_review/Jagau_2017_electronic_resonances_ARPC.pdf",
        "topic": "电子共振 L2方法 — 原理发展",
    },
    {
        "key": "decleva2022_tiresia_review",
        "title": "Continuum Electronic States: The Tiresia Code",
        "doi": "10.3390/molecules27062026",
        "pdf": "papers/B_spline_continuum/Decleva_2022_Tiresia_continuum_Molecules.pdf",
        "topic": "连续态基组方法（B-spline/GTO/DFT）— 方法开发",
    },
    {
        "key": "bachau2001_bspline_review",
        "title": "Applications of B-splines in atomic and molecular physics",
        "doi": "10.1088/0034-4885/64/12/205",
        "pdf": "papers/B_spline_continuum/Bachau-2001-Applications of B-splines in atomi.pdf",
        "topic": "B-spline 连续态 — 方法开发与原理",
    },
    {
        "key": "nisoli2017_attosecond_review",
        "title": "Attosecond Electron Dynamics in Molecules",
        "doi": "10.1021/acs.chemrev.6b00453",
        "pdf": "papers/general_review/Nisoli_2017_attosecond_electron_dynamics_ChemRev.pdf",
        "topic": "阿秒电子动力学 — 原理发展（前沿）",
    },
    {
        "key": "hrodmarsson2023_astro_vuv_review",
        "title": "Photodissociation and photoionization of molecules of astronomical interest (VUV database update)",
        "doi": "10.1051/0004-6361/202346645",
        "pdf": "papers/general_review/Hrodmarsson_2023_VUV_database_AA.pdf",
        "topic": "天体化学 VUV 光致离解/电离 — 应用综述",
    },
    {
        "key": "calegari2016_charge_migration_review",
        "title": "Charge migration induced by attosecond pulses in bio-relevant molecules",
        "doi": "10.1088/0953-4075/49/14/142001",
        "pdf": "papers/general_review/Calegari_2016_charge_migration_attosecond_JPB.pdf",
        "topic": "电荷迁移动力学 — 原理发展（前沿）",
    },
    {
        "key": "eyert_asw_review",
        "title": "Basic notions and applications of the augmented spherical wave method",
        "doi": "10.1002/(sici)1097-461x(2000)77:6<1007::aid-qua8>3.0.co;2-u",
        "pdf": "papers/spherical_wave/Eyert_ASW_review.pdf",
        "topic": "球面波展开/APW — 方法开发与原理",
    },
    {
        "key": "gonis_butler2000_multiple_scattering_book",
        "title": "Multiple Scattering in Solids (Springer book)",
        "doi": "10.1007/978-1-4612-1290-4",
        "pdf": "papers/spherical_wave/Gonis_Butler_1999_multiple_scattering_Springer.pdf",
        "topic": "多重散射理论 — 方法专著",
    },
]

def get_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:' + MAILTO})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.load(r)

def resolve_doi(doi):
    """Get OpenAlex Work id + metadata from DOI (tolerant to prefix forms)."""
    doi = doi.replace('https://doi.org/', '').strip().lower()
    url = BASE + 'works/https://doi.org/' + urllib.parse.quote(doi) + '?mailto=' + MAILTO
    try:
        return get_json(url)
    except Exception as e:
        print('  resolve DOI failed:', repr(e)); return None

def batch_works(ids, chunk=40):
    """Resolve a list of OpenAlex IDs to metadata in chunks."""
    out = {}
    ids = [i for i in ids if i]
    for k in range(0, len(ids), chunk):
        batch = ids[k:k+chunk]
        flt = '|'.join(batch)
        url = BASE + 'works?filter=ids.openalex:' + flt + '&per-page=40&mailto=' + MAILTO
        try:
            d = get_json(url)
            for w in d.get('results', []):
                if w.get('id'): out[w['id']] = w
        except Exception as e:
            print('  batch failed:', repr(e))
        time.sleep(0.2)
    return out

def kth_citing(work_id, per_page=200, max_pages=3):
    """citing works sorted by cited_by_count desc."""
    out = []
    cursor = '*'
    for _ in range(max_pages):
        url = (BASE + 'works?filter=cites:' + work_id.split('/')[-1]
               + '&sort=cited_by_count:desc&per-page=' + str(per_page)
               + '&cursor=' + cursor + '&mailto=' + MAILTO)
        try:
            d = get_json(url)
        except Exception as e:
            print('  citing failed:', repr(e)); break
        out.extend(d.get('results', []))
        nxt = d.get('meta', {}).get('next_cursor')
        if not nxt: break
        cursor = nxt
        time.sleep(0.2)
    return out

def summarize(refs_raw):
    """Build compact records from OpenAlex works."""
    def one(w):
        if not w: return None
        auth = [a.get('author', {}).get('display_name', '') for a in (w.get('authorships') or [])][:4]
        return {
            "title": w.get('display_name'),
            "year": w.get('publication_year'),
            "authors": auth,
            "venue": (w.get('primary_location') or {}).get('source', {}).get('display_name') if (w.get('primary_location') or {}).get('source') else None,
            "cited_by": w.get('cited_by_count'),
            "type": w.get('type'),
            "doi": (w.get('doi') or '').replace('https://doi.org/', ''),
            "concepts": [c.get('display_name') for c in (w.get('concepts') or [])][:3],
        }
    return [one(w) for w in refs_raw if one(w)]

def main():
    outdir = 'outputs/citation_network'
    os.makedirs(outdir, exist_ok=True)
    all_reviews = []
    for rv in REVIEWS:
        print('=' * 70)
        print('PROCESS:', rv['key'])
        w0 = resolve_doi(rv['doi'])
        if not w0:
            print('  !! unresolved, skip'); continue
        wid = w0['id']
        # referenced works
        ref_ids = w0.get('referenced_works', [])
        print('  references count:', len(ref_ids))
        ref_meta = batch_works(ref_ids)
        refs_raw = [ref_meta[i] for i in ref_ids if i in ref_meta]
        refs_sorted = sorted([r for r in refs_raw if r], key=lambda x: -(x.get('cited_by_count') or 0))
        refs_top = summarize(refs_sorted[:25])
        # citing works
        citing_raw = kth_citing(wid)
        print('  citing works fetched:', len(citing_raw))
        citing_sorted = sorted([c for c in citing_raw if c], key=lambda x: -(x.get('cited_by_count') or 0))
        citing_top = summarize(citing_sorted[:25])
        # recent citing (>=2021) for frontier direction
        recent = summarize([c for c in citing_sorted if (c.get('publication_year') or 0) >= 2021][:25])

        node = {
            "key": rv['key'],
            "title": rv['title'],
            "topic": rv['topic'],
            "pdf": rv['pdf'],
            "doi": rv['doi'],
            "work_id": wid,
            "meta": {
                "openalex_title": w0.get('display_name'),
                "year": w0.get('publication_year'),
                "cited_by_total": w0.get('cited_by_count'),
                "references_total": len(ref_ids),
                "type": w0.get('type'),
                "venue": (w0.get('primary_location') or {}).get('source', {}).get('display_name') if (w0.get('primary_location') or {}).get('source') else None,
                "concepts": [c.get('display_name') for c in (w0.get('concepts') or [])][:4],
            },
            "referenced_top25": refs_top,
            "citing_top25": citing_top,
            "citing_recent_top25": recent,
        }
        all_reviews.append(node)
        fn = os.path.join(outdir, rv['key'] + '.json')
        with open(fn, 'w', encoding='utf-8') as f:
            json.dump(node, f, ensure_ascii=False, indent=2)
        print('  saved ->', fn)
        time.sleep(0.4)

    with open(os.path.join(outdir, '_ALL.json'), 'w', encoding='utf-8') as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)
    print('\nDONE. reviews processed:', len(all_reviews))

if __name__ == '__main__':
    main()
