#include <stdlib.h>

#include <cmath>

#include "../gmx_lapack.h"

#include "gromacs/utility/real.h"

#include "lapack_limits.h"


void F77_FUNC(dlagts, DLAGTS)(int*    job,
                              int*    n,
                              double* a,
                              double* b,
                              double* c__,
                              double* d__,
                              int*    in,
                              double* y,
                              double* tol,
                              int*    info)
{
    int    i__1;
    double d__1, d__2, d__4, d__5;

    int    k;
    double ak, eps, temp, pert, absak, sfmin;
    double bignum, minval;
    --y;
    --in;
    --d__;
    --c__;
    --b;
    --a;

    *info = 0;
    if (abs(*job) > 2 || *job == 0)
    {
        *info = -1;
    }
    else if (*n < 0)
    {
        *info = -2;
    }
    if (*info != 0)
    {
        return;
    }

    if (*n == 0)
    {
        return;
    }
    eps    = GMX_DOUBLE_EPS;
    minval = GMX_DOUBLE_MIN;
    sfmin  = minval / eps;

    bignum = 1. / sfmin;

    if (*job < 0)
    {
        if (*tol <= 0.)
        {
            *tol = std::abs(a[1]);
            if (*n > 1)
            {
                d__1 = *tol;
                d__2 = std::abs(a[2]);
                d__1 = (d__1 > d__2) ? d__1 : d__2;
                d__2 = std::abs(b[1]);
                *tol = (d__1 > d__2) ? d__1 : d__2;
            }
            i__1 = *n;
            for (k = 3; k <= i__1; ++k)
            {
                d__4 = *tol;
                d__5 = std::abs(a[k]);
                d__4 = (d__4 > d__5) ? d__4 : d__5;
                d__5 = std::abs(b[k - 1]);
                d__4 = (d__4 > d__5) ? d__4 : d__5;
                d__5 = std::abs(d__[k - 2]);
                *tol = (d__4 > d__5) ? d__4 : d__5;
            }
            *tol *= eps;
            if (std::abs(*tol) < GMX_DOUBLE_MIN)
            {
                *tol = eps;
            }
        }
    }

    if (1 == abs(*job))
    {
        i__1 = *n;
        for (k = 2; k <= i__1; ++k)
        {
            if (in[k - 1] == 0)
            {
                y[k] -= c__[k - 1] * y[k - 1];
            }
            else
            {
                temp     = y[k - 1];
                y[k - 1] = y[k];
                y[k]     = temp - c__[k - 1] * y[k];
            }
        }
        if (*job == 1)
        {
            for (k = *n; k >= 1; --k)
            {
                if (k <= *n - 2)
                {
                    temp = y[k] - b[k] * y[k + 1] - d__[k] * y[k + 2];
                }
                else if (k == *n - 1)
                {
                    temp = y[k] - b[k] * y[k + 1];
                }
                else
                {
                    temp = y[k];
                }
                ak    = a[k];
                absak = std::abs(ak);
                if (absak < 1.)
                {
                    if (absak < sfmin)
                    {
                        if (std::abs(absak) < GMX_DOUBLE_MIN || std::abs(temp) * sfmin > absak)
                        {
                            *info = k;
                            return;
                        }
                        else
                        {
                            temp *= bignum;
                            ak *= bignum;
                        }
                    }
                    else if (std::abs(temp) > absak * bignum)
                    {
                        *info = k;
                        return;
                    }
                }
                y[k] = temp / ak;
            }
        }
        else
        {
            for (k = *n; k >= 1; --k)
            {
                if (k + 2 <= *n)
                {
                    temp = y[k] - b[k] * y[k + 1] - d__[k] * y[k + 2];
                }
                else if (k + 1 == *n)
                {
                    temp = y[k] - b[k] * y[k + 1];
                }
                else
                {
                    temp = y[k];
                }
                ak = a[k];

                pert = *tol;
                if (ak < 0)
                    pert *= -1.0;
            L40:
                absak = std::abs(ak);
                if (absak < 1.)
                {
                    if (absak < sfmin)
                    {
                        if (std::abs(absak) < GMX_DOUBLE_MIN || std::abs(temp) * sfmin > absak)
                        {
                            ak += pert;
                            pert *= 2;
                            goto L40;
                        }
                        else
                        {
                            temp *= bignum;
                            ak *= bignum;
                        }
                    }
                    else if (std::abs(temp) > absak * bignum)
                    {
                        ak += pert;
                        pert *= 2;
                        goto L40;
                    }
                }
                y[k] = temp / ak;
            }
        }
    }
    else
    {

        if (*job == 2)
        {
            i__1 = *n;
            for (k = 1; k <= i__1; ++k)
            {
                if (k >= 3)
                {
                    temp = y[k] - b[k - 1] * y[k - 1] - d__[k - 2] * y[k - 2];
                }
                else if (k == 2)
                {
                    temp = y[k] - b[k - 1] * y[k - 1];
                }
                else
                {
                    temp = y[k];
                }
                ak    = a[k];
                absak = std::abs(ak);
                if (absak < 1.)
                {
                    if (absak < sfmin)
                    {
                        if (std::abs(absak) < GMX_DOUBLE_MIN || std::abs(temp) * sfmin > absak)
                        {
                            *info = k;
                            return;
                        }
                        else
                        {
                            temp *= bignum;
                            ak *= bignum;
                        }
                    }
                    else if (std::abs(temp) > absak * bignum)
                    {
                        *info = k;
                        return;
                    }
                }
                y[k] = temp / ak;
            }
        }
        else
        {
            i__1 = *n;
            for (k = 1; k <= i__1; ++k)
            {
                if (k >= 3)
                {
                    temp = y[k] - b[k - 1] * y[k - 1] - d__[k - 2] * y[k - 2];
                }
                else if (k == 2)
                {
                    temp = y[k] - b[k - 1] * y[k - 1];
                }
                else
                {
                    temp = y[k];
                }
                ak = a[k];

                pert = *tol;
                if (ak < 0)
                    pert *= -1.0;

            L70:
                absak = std::abs(ak);
                if (absak < 1.)
                {
                    if (absak < sfmin)
                    {
                        if (std::abs(absak) < GMX_DOUBLE_MIN || std::abs(temp) * sfmin > absak)
                        {
                            ak += pert;
                            pert *= 2;
                            goto L70;
                        }
                        else
                        {
                            temp *= bignum;
                            ak *= bignum;
                        }
                    }
                    else if (std::abs(temp) > absak * bignum)
                    {
                        ak += pert;
                        pert *= 2;
                        goto L70;
                    }
                }
                y[k] = temp / ak;
            }
        }

        for (k = *n; k >= 2; --k)
        {
            if (in[k - 1] == 0)
            {
                y[k - 1] -= c__[k - 1] * y[k];
            }
            else
            {
                temp     = y[k - 1];
                y[k - 1] = y[k];
                y[k]     = temp - c__[k - 1] * y[k];
            }
        }
    }

    return;
}
