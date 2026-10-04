/*
 * day1_eq_temp_base.c
 * 第1回: 地球のエネルギー収支モデル（0次元モデル）
 *
 * 放射平衡の式  S(1-a)/4 = eps * sigma * T^4  を解いて
 * 平衡温度 T を1回だけ計算する、最も単純な version。
 */
#include <stdio.h>
#include <math.h>

int main(void)
{
    double S       = 1361.0;            /* 太陽定数 [W/m^2] */
    double albedo  = 0.30;              /* アルベド（無次元） */
    double epsilon = 1.0;               /* 放射率（無次元） */
    double sigma   = 5.670374419e-8;    /* シュテファン・ボルツマン定数 [W/(m^2 K^4)] */

    double T = pow(S * (1.0 - albedo) / (4.0 * epsilon * sigma), 0.25);

    printf("S = %.1f W/m^2, albedo = %.2f, epsilon = %.2f\n", S, albedo, epsilon);
    printf("-> 平衡温度 T = %.2f K (%.2f C)\n", T, T - 273.15);

    return 0;
}
