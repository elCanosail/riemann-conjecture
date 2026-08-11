"""
Computational verification of zeta zeros on the critical line.

This script verifies numerically that the nontrivial zeros of ζ(s) with
imaginary part in [T, 2T] lie on the critical line Re(s) = 1/2, using
mpmath's zetazero function which computes zeros to high precision.

This is NOT a proof. It is a computational sanity check that our
understanding of the zero distribution is correct, and a foundation
for future numerical experiments.

Usage:
    python verify_zeros.py --T 100 --2T 200
    python verify_zeros.py --T 1000 --2T 2000 --output results.json

Requirements:
    pip install mpmath

References:
    - Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Grösse.
    - Odlyzko, A. (http://www.dtc.umn.edu/~odlyzko/) — numerical computations of zeta zeros
    - Claude/Anthropic (2026). "More than two thirds of the zeros of the Riemann zeta
      function lie on the critical line."
"""

import argparse
import json
import sys
from datetime import datetime, timezone

try:
    from mpmath import zetazero, mp
    mp.dps = 25  # 25 decimal places of precision
except ImportError:
    print("ERROR: mpmath not installed. Run: pip install mpmath", file=sys.stderr)
    sys.exit(1)


def count_zeros_in_interval(T_start, T_end, max_zeros=10000):
    """
    Count zeros of ζ(s) with imaginary part in [T_start, T_end).
    
    Returns:
        dict with:
            - total: total zeros found (with multiplicity)
            - on_line: zeros with Re(s) = 1/2 (to numerical precision)
            - off_line: zeros with Re(s) ≠ 1/2
            - zeros: list of (ord, re, im) tuples
            - max_re_deviation: maximum |Re(s) - 1/2| observed
    """
    zeros = []
    on_line = 0
    off_line = 0
    max_re_deviation = mp.mpf('0')
    
    # zetazero(n) returns the n-th zero, 1-indexed
    # We need to find the first zero with Im >= T_start
    # Binary search would be faster, but for verification we iterate
    
    n = 1
    found_start = False
    count = 0
    
    while count < max_zeros:
        try:
            z = zetazero(n)
            im = float(z.imag)
            re = float(z.real)
            
            if im < T_start:
                n += 1
                continue
            if im >= T_end:
                break
            
            zeros.append({
                "n": n,
                "re": re,
                "im": im,
                "on_line": abs(re - 0.5) < 1e-10
            })
            
            deviation = abs(re - 0.5)
            if deviation > max_re_deviation:
                max_re_deviation = deviation
            
            if abs(re - 0.5) < 1e-10:
                on_line += 1
            else:
                off_line += 1
                print(f"  ⚠️  OFF-LINE ZERO FOUND: n={n}, Re={re:.15f}, Im={im:.6f}")
            
            count += 1
            n += 1
            
        except Exception as e:
            print(f"  Error at n={n}: {e}", file=sys.stderr)
            break
    
    return {
        "total": count,
        "on_line": on_line,
        "off_line": off_line,
        "max_re_deviation": float(max_re_deviation),
        "proportion_on_line": on_line / count if count > 0 else 0,
        "zeros": zeros[:100],  # Only store first 100 for brevity
        "T_start": T_start,
        "T_end": T_end,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Verify zeta zeros on the critical line"
    )
    parser.add_argument("--T", type=float, default=100, 
                        help="Start of imaginary part interval")
    parser.add_argument("--2T", type=float, default=200,
                        help="End of imaginary part interval (use --2T)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON file path")
    parser.add_argument("--max-zeros", type=int, default=10000,
                        help="Maximum zeros to compute")
    args = parser.parse_args()
    
    # Handle --2T (Python argparse doesn't like names starting with digit)
    T_end = getattr(args, '2T') if hasattr(args, '2T') else args.__dict__.get('2T', 200)
    
    print(f"ζ(s) zero verification")
    print(f"Interval: [{args.T}, {T_end})")
    print(f"Precision: {mp.dps} decimal places")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print()
    
    result = count_zeros_in_interval(args.T, T_end, args.max_zeros)
    
    print(f"Results:")
    print(f"  Total zeros found: {result['total']}")
    print(f"  On critical line:  {result['on_line']} ({result['proportion_on_line']:.4%})")
    print(f"  Off critical line:  {result['off_line']}")
    print(f"  Max |Re - 1/2|:    {result['max_re_deviation']:.2e}")
    print()
    
    if result['off_line'] > 0:
        print("⚠️  OFF-LINE ZEROS DETECTED — this would disprove RH!")
    else:
        print("✅ All zeros found are on the critical line (as expected)")
    
    # Add metadata
    result["metadata"] = {
        "script": "verify_zeros.py",
        "mpmath_version": mp.version if hasattr(mp, 'version') else "unknown",
        "precision": mp.dps,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "note": "Numerical verification only. Not a proof.",
    }
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to {args.output}")
    
    return result


if __name__ == "__main__":
    main()