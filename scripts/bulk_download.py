#!/usr/bin/env python3
"""按探测结果批量下载 PDF：arXiv/Springer 直链可靠；ScienceDirect 快速失败不重试。"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from smart_pdf import try_download  # noqa: E402

JOBS = [
    # (pdf 探测 URL, 输出文件名, 来源标签)
    ("https://arxiv.org/pdf/2503.11572", "papers/NMI_2026_ImplicitBias.pdf", "arxiv"),
    ("https://arxiv.org/pdf/2603.03412v1", "papers/TAI_2026_PrivateEdit.pdf", "arxiv"),
    ("https://link.springer.com/content/pdf/10.1007/s10994-026-07147-2.pdf", "papers/ML_2026_Multilabel.pdf", "springer"),
    ("https://link.springer.com/content/pdf/10.1007/s10994-026-07126-7.pdf", "papers/ML_2026_ITRM.pdf", "springer"),
    ("https://link.springer.com/content/pdf/10.1007/s10207-026-01318-x.pdf", "papers/IJIS_2026_CAM_LDS.pdf", "springer"),
    ("https://link.springer.com/content/pdf/10.1007/s10994-026-07132-9.pdf", "papers/ML_2026_Morphing.pdf", "springer"),
    ("https://www.nature.com/articles/s42256-026-01299-5.pdf", "papers/NMI_2026_Repro.pdf", "nature"),
    ("https://www.sciencedirect.com/science/article/pii/S0004370226001335/pdfft?isDTMRedir=true&download=true", "papers/AI_2026_FedRec.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0893608026010221/pdfft?isDTMRedir=true&download=true", "papers/NN_2026_HypergraphVRP.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0167404826003093/pdfft?isDTMRedir=true&download=true", "papers/COSE_2026_MSTE_CAN.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0893608026009962/pdfft?isDTMRedir=true&download=true", "papers/NN_2026_SeizureSOZ.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S000437022600130X/pdfft?isDTMRedir=true&download=true", "papers/AI_2026_ParaKplex.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0893608026009834/pdfft?isDTMRedir=true&download=true", "papers/NN_2026_EventTriggered.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0167404826003081/pdfft?isDTMRedir=true&download=true", "papers/COSE_2026_DynamicDefense.pdf", "sd"),
    ("https://www.sciencedirect.com/science/article/pii/S0004370226001293/pdfft?isDTMRedir=true&download=true", "papers/AI_2026_DiaCoG.pdf", "sd"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ok = []
    fail = []
    for url, out, tag in JOBS:
        outfile = ROOT / out
        if outfile.exists():
            print(f"[skip exists] {out}")
            ok.append(out)
            continue
        status = try_download(url, outfile, timeout=120)
        if status == "ok":
            print(f"[OK   {tag}] {out}")
            ok.append(out)
        else:
            print(f"[FAIL {tag}] {status}  {out}")
            fail.append(out)
    print(f"\n成功 {len(ok)} / 尝试 {len(JOBS)}；失败 {len(fail)}")
    for f in fail:
        print("  -", f)


if __name__ == "__main__":
    main()
