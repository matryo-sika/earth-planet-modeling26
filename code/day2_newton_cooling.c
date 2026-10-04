/*
 * day2_newton_cooling.c
 * 第2回: Euler法の確認用テンプレート
 *
 * ニュートンの冷却則  dT/dt = -k (T - T_env)  を
 * 陽的Euler法（前進差分）で数値的に解く、最も単純な例。
 * この構造（forループで t, T を少しずつ更新していく）を
 * このあとの課題でそのまま使い回す。
 *
 * 改造課題: dt（時間刻み）を大きくしてみるとどうなるか確認しよう。
 *           ある程度以上大きくすると、Tが振動したり発散したりする
 *           （数値不安定）ことを確認する。
 */
#include <stdio.h>

int main(void)
{
    double T     = 350.0;   /* 初期温度 [K] */
    double T_env = 300.0;   /* 周囲の温度 [K] */
    double k     = 0.05;    /* 冷却係数 [1/s] */
    double dt    = 1.0;     /* 時間刻み [s] （ここを変えて安定性を確認） */
    double t_end = 200.0;   /* 計算を終了する時刻 [s] */

    FILE *fp = fopen("cooling.dat", "w");
    if (fp == NULL) {
        fprintf(stderr, "output file cannot be opened.\n");
        return 1;
    }

    fprintf(fp, "# t[s]  T[K]\n");
    for (double t = 0.0; t <= t_end; t += dt) {
        fprintf(fp, "%.3f %.6f\n", t, T);

        double dTdt = -k * (T - T_env);   /* f(T) = dT/dt */
        T = T + dt * dTdt;                /* Euler法の更新式: T_{n+1} = T_n + dt * f(T_n) */
    }

    fclose(fp);
    printf("cooling.dat を出力しました。\n");
    return 0;
}
