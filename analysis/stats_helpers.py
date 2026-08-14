"""Small statistics + formatting helpers shared by the report generator."""
import numpy as np
import pandas as pd
import pingouin as pg
from config import SUPPRESS_N, NONRESPONSE


def fmt_eps2(v):
    """Display-format epsilon-squared: the bias-corrected formula can return
    small negative values at a null/near-null effect. Truncated to 0.00 for
    display (marked with dagger) rather than shown negative, applied
    uniformly everywhere eps2 is reported in this project."""
    return f"{v:.2f}" if v >= 0 else "0.00^{\\dagger}"


def mask(n):
    """Apply n<SUPPRESS_N cell suppression to a displayed count."""
    return f"<{SUPPRESS_N}" if 0 < n < SUPPRESS_N else str(int(n))


def freq_table(series, labels=None, dropna_label="(structural skip)"):
    """Frequency table retaining pna/not_sure as categories; NaN -> skip row.
    Returns list of (category, n, pct_of_answered) with n<5 suppression on n.
    pct is over the 'answered' base (excludes structural skip / NaN)."""
    s = series.copy()
    vc = s.value_counts(dropna=False)
    answered = int(s.notna().sum())
    rows = []
    for cat, n in vc.items():
        if pd.isna(cat):
            rows.append((dropna_label, int(n), None))
        else:
            lab = labels.get(cat, cat) if labels else cat
            pct = 100 * n / answered if answered else np.nan
            rows.append((str(lab), int(n), pct))
    # sort: real categories by n desc, skip last
    rows.sort(key=lambda r: (r[2] is None, -(r[1])))
    return rows, answered


def onehot_freq(df, prefix, labels, base_mask):
    """Frequency table for a select-multiple field stored as one-hot
    `prefix/option` columns. `base_mask` selects the respondents eligible
    to answer (e.g. the branch, not just non-null rows). Returns rows in the
    same (category, n, pct) shape as freq_table, sorted by n desc."""
    cols = [c for c in df.columns if c.startswith(prefix + "/")]
    base = int(base_mask.sum())
    rows = []
    for c in cols:
        opt = c.split("/", 1)[1]
        n = int(pd.to_numeric(df.loc[base_mask, c], errors="coerce").fillna(0).sum())
        lab = labels.get(opt, opt)
        pct = 100 * n / base if base else np.nan
        rows.append((str(lab), n, pct))
    rows.sort(key=lambda r: -r[1])
    return rows, base


def desc_numeric(x, label, unit=""):
    """Mean/median/SD/range/IQR markdown line for a continuous/count variable
    (same treatment as `age` in section_univariate)."""
    x = pd.to_numeric(x, errors="coerce").dropna()
    if len(x) == 0:
        return f"- **{label}** (n=0): no answered responses.\n"
    return (f"- **{label}** (n={len(x)}): median $\\tilde{{x}}={x.median():.0f}${unit}, "
            f"mean $\\bar{{x}}={x.mean():.1f}${unit}, SD $s={x.std():.1f}$, "
            f"range {int(x.min())}–{int(x.max())}{unit}, "
            f"IQR {x.quantile(.25):.0f}–{x.quantile(.75):.0f}{unit}.\n")


def desc_ordinal(x):
    """Median, IQR, n for an ordinal/numeric series (NA dropped)."""
    x = pd.to_numeric(x, errors="coerce").dropna()
    if len(x) == 0:
        return dict(n=0, median=np.nan, q1=np.nan, q3=np.nan)
    return dict(n=int(len(x)), median=float(np.median(x)),
                q1=float(np.percentile(x, 25)), q3=float(np.percentile(x, 75)))


def mann_whitney(a, b):
    """Mann-Whitney U with rank-biserial effect size (pingouin)."""
    a = pd.to_numeric(a, errors="coerce").dropna()
    b = pd.to_numeric(b, errors="coerce").dropna()
    if len(a) < 1 or len(b) < 1:
        return None
    res = pg.mwu(a, b, alternative="two-sided").iloc[0]
    ucol = "U_val" if "U_val" in res.index else "U-val"
    pcol = "p_val" if "p_val" in res.index else "p-val"
    return dict(U=float(res[ucol]), p=float(res[pcol]),
                rbc=float(res["RBC"]), cles=float(res["CLES"]),
                n1=len(a), n2=len(b))


def mann_whitney_perm(a, b, n_perm=10000, seed=None):
    """Tie-aware exact/permutation check for mann_whitney(), same Monte Carlo
    convention as chi2_perm() (label-permutation, +1 bias correction). Exists
    because scipy's own method='exact' for mannwhitneyu applies NO tie
    correction to the null U-distribution, which is invalid for an ordinal
    0-6 outcome with heavy ties (this dataset: n2=5, ceiling-weighted). This
    permutation instead resamples the tied ranks directly, so it stays valid
    under ties, unlike scipy's combinatorial exact method or the normal
    approximation used in mann_whitney() above. Returns dict(U, p, n1, n2) or
    None if either group is empty."""
    from scipy.stats import rankdata
    a = pd.to_numeric(a, errors="coerce").dropna().to_numpy()
    b = pd.to_numeric(b, errors="coerce").dropna().to_numpy()
    n1, n2 = len(a), len(b)
    if n1 < 1 or n2 < 1:
        return None
    pooled = np.concatenate([a, b])
    ranks = rankdata(pooled)
    obs_U1 = ranks[:n1].sum() - n1 * (n1 + 1) / 2
    obs_U = min(obs_U1, n1 * n2 - obs_U1)
    rng = np.random.default_rng(seed)
    ge = 1  # +1 to observed: standard Monte Carlo p-value bias correction
    for _ in range(n_perm):
        r = rng.permutation(ranks)
        U1 = r[:n1].sum() - n1 * (n1 + 1) / 2
        Umin = min(U1, n1 * n2 - U1)
        if Umin <= obs_U + 1e-9:
            ge += 1
    p = ge / (n_perm + 1)
    return dict(U=float(obs_U1), p=float(p), n1=n1, n2=n2)


def kruskal(groups):
    """Kruskal-Wallis across a dict {label: series}. Returns H, p, eps2."""
    arrs = {k: pd.to_numeric(v, errors="coerce").dropna() for k, v in groups.items()}
    arrs = {k: v for k, v in arrs.items() if len(v) > 0}
    if len(arrs) < 2:
        return None
    from scipy.stats import kruskal as _k
    H, p = _k(*arrs.values())
    N = sum(len(v) for v in arrs.values())
    k = len(arrs)
    eps2 = (H - k + 1) / (N - k) if N > k else np.nan   # epsilon-squared
    return dict(H=float(H), p=float(p), eps2=float(eps2),
                ns={k_: len(v) for k_, v in arrs.items()})


def prevalence(series, positive="si", answered_values=None):
    """Prevalence of `positive` over the answered base (retaining pna/not_sure
    as answered, per policy). Returns (k, base, pct, ci_low, ci_high) with
    Wilson 95% CI; suppressed if k<5."""
    s = series.dropna()
    base = int(len(s))
    k = int((s == positive).sum())
    if base == 0:
        return dict(k=k, base=base, pct=np.nan, lo=np.nan, hi=np.nan)
    p = k / base
    # Wilson score interval
    z = 1.959963985
    denom = 1 + z**2 / base
    center = (p + z**2 / (2 * base)) / denom
    half = (z * np.sqrt(p * (1 - p) / base + z**2 / (4 * base**2))) / denom
    return dict(k=k, base=base, pct=100 * p,
                lo=100 * max(0, center - half), hi=100 * min(1, center + half))


def fisher_or(a, b):
    """Exact Fisher's test for a 2x2 table of two paired categorical arrays.
    Returns dict(table, odds_ratio, p, n) or None if the pairwise-complete
    table isn't exactly 2x2 (e.g. one level never co-occurs)."""
    from scipy.stats import fisher_exact
    a = pd.Series(a); b = pd.Series(b)
    ok = a.notna() & b.notna()
    a, b = a[ok], b[ok]
    table = pd.crosstab(a, b)
    if table.shape != (2, 2):
        return None
    odds_ratio, p = fisher_exact(table.to_numpy())
    return dict(table=table, odds_ratio=float(odds_ratio), p=float(p), n=int(len(a)))


def chi2_perm(a, b, n_perm=10000, seed=None):
    """Association test for two paired nominal categorical arrays (>2
    levels), via label-permutation on Pearson's chi-square statistic - a
    Monte Carlo substitute for the Fisher-Freeman-Halton exact test (same
    idea as R's fisher.test(simulate.p.value=TRUE)). Avoids the
    expected-count>=5 assumption that chi2_contingency's asymptotic p-value
    needs, which the sparse tables here routinely violate. Returns
    dict(table, chi2, p, cramers_v, n) or None if degenerate (<2 levels on
    either side after dropping missing)."""
    from scipy.stats import chi2_contingency
    a = pd.Series(a); b = pd.Series(b)
    ok = a.notna() & b.notna()
    a_codes, a_cats = pd.factorize(a[ok])
    b_codes, b_cats = pd.factorize(b[ok])
    n = len(a_codes)
    nr, nc = len(a_cats), len(b_cats)
    if nr < 2 or nc < 2 or n < 2:
        return None

    def build(ac, bc):
        t = np.zeros((nr, nc))
        np.add.at(t, (ac, bc), 1)
        return t

    obs_table = build(a_codes, b_codes)
    obs_chi2 = chi2_contingency(obs_table, correction=False)[0]
    rng = np.random.default_rng(seed)
    ge = 1  # +1 to observed: standard Monte Carlo p-value bias correction
    for _ in range(n_perm):
        stat = chi2_contingency(build(a_codes, rng.permutation(b_codes)),
                                 correction=False)[0]
        if stat >= obs_chi2 - 1e-9:
            ge += 1
    p = ge / (n_perm + 1)
    k = min(nr, nc)
    cramers_v = float(np.sqrt(obs_chi2 / (n * (k - 1))))
    table = pd.DataFrame(obs_table, index=a_cats, columns=b_cats)
    return dict(table=table, chi2=float(obs_chi2), p=float(p),
                cramers_v=cramers_v, n=n)


def ordinal_logit(y, X):
    """Proportional-odds (ordinal logistic) regression via statsmodels
    `OrderedModel`. `y` is an ordered outcome as int codes (low->high, no
    gaps); `X` is a predictor DataFrame (numeric/binary columns, no
    intercept — OrderedModel estimates cutpoints instead). Returns
    dict(rows=[{predictor, coef, se, OR, lo, hi, p}, ...], n, k_params,
    llr, llr_p, prsquared, converged) or None if the fit fails to converge."""
    from statsmodels.miscmodels.ordinal_model import OrderedModel
    mod = OrderedModel(y, X, distr="logit")
    try:
        res = mod.fit(method="bfgs", disp=False, maxiter=300)
    except Exception:
        return None
    if not res.mle_retvals.get("converged", False):
        return None
    z = 1.959963985
    rows = []
    for name in X.columns:
        b, se, p = float(res.params[name]), float(res.bse[name]), float(res.pvalues[name])
        rows.append(dict(predictor=name, coef=b, se=se, OR=float(np.exp(b)),
                          lo=float(np.exp(b - z * se)), hi=float(np.exp(b + z * se)), p=p))
    return dict(rows=rows, n=int(res.nobs), k_params=len(res.params),
                llr=float(res.llr), llr_p=float(res.llr_pvalue),
                llr_df=int(res.df_model), prsquared=float(res.prsquared),
                converged=True)


def spearman_pair(a, b):
    """Spearman correlation for a pair of ordinal items (pairwise-complete).
    Returns dict(rho, p, n) or None if fewer than 3 complete pairs."""
    a = pd.to_numeric(pd.Series(a), errors="coerce")
    b = pd.to_numeric(pd.Series(b), errors="coerce")
    d = pd.concat([a, b], axis=1).dropna()
    if len(d) < 3:
        return None
    res = pg.corr(d.iloc[:, 0], d.iloc[:, 1], method="spearman").iloc[0]
    pcol = "p_val" if "p_val" in res.index else "p-val"
    return dict(rho=float(res["r"]), p=float(res[pcol]), n=int(res["n"]))


def cronbach(items_df):
    """Cronbach's alpha (95% CI) for a complete-case wide item DataFrame
    (columns = items, 0/1 or numeric-coded responses). Returns
    dict(alpha, lo, hi, n, k) or None if fewer than 2 items or <3 complete
    rows (alpha is undefined/unstable below that)."""
    d = items_df.dropna()
    if d.shape[1] < 2 or len(d) < 3:
        return None
    alpha, ci = pg.cronbach_alpha(data=d)
    return dict(alpha=float(alpha), lo=float(ci[0]), hi=float(ci[1]),
                n=len(d), k=d.shape[1])


def bh_fdr(pvals, alpha=0.05):
    """Benjamini-Hochberg FDR correction across a secondary/exploratory test
    family. `pvals` is a list of raw p-values (order preserved). Returns a
    list of (q, reject) pairs aligned to the input order."""
    if not pvals:
        return []
    reject, q = pg.multicomp(list(pvals), alpha=alpha, method="fdr_bh")
    return list(zip((float(x) for x in q), (bool(x) for x in reject)))


def md_table(headers, rows):
    """Render a markdown table from headers + list-of-rows."""
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join(["---"] * len(headers)) + " |"]
    for r in rows:
        out.append("| " + " | ".join("" if c is None else str(c) for c in r) + " |")
    return "\n".join(out)
